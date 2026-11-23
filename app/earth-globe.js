'use client';

import { useEffect, useRef } from 'react';
import * as THREE from 'three';

const continents = [
    [[-168, 70], [-145, 72], [-125, 60], [-115, 48], [-96, 50], [-82, 25], [-98, 15], [-112, 28], [-130, 48], [-155, 58]],
    [[-81, 12], [-66, 10], [-50, -2], [-44, -20], [-54, -40], [-70, -55], [-76, -30], [-80, -8]],
    [[-11, 72], [30, 70], [42, 55], [28, 42], [38, 30], [20, 10], [10, -5], [30, -35], [17, -35], [-2, -15], [-15, 5], [-18, 35], [-8, 52]],
    [[28, 70], [65, 75], [105, 72], [145, 60], [170, 52], [155, 40], [130, 35], [120, 20], [105, 5], [80, 8], [65, 25], [45, 28], [35, 45]],
    [[112, -11], [130, -10], [153, -20], [151, -39], [134, -44], [115, -33]],
    [[-52, 83], [-25, 78], [-37, 60], [-54, 60], [-64, 72]],
    [[46, -13], [50, -18], [49, -25], [45, -23]],
    [[-180, -70], [-120, -73], [-60, -75], [0, -72], [60, -74], [120, -72], [180, -70], [180, -90], [-180, -90]],
];

function isLand(longitude, latitude) {
    return continents.some((polygon) => {
        let inside = false;
        for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i, i += 1) {
            const [xi, yi] = polygon[i];
            const [xj, yj] = polygon[j];
            const crosses = (yi > latitude) !== (yj > latitude)
                && longitude < ((xj - xi) * (latitude - yi)) / (yj - yi) + xi;
            if (crosses) inside = !inside;
        }
        return inside;
    });
}

function terrainNoise(longitude, latitude) {
    const x = longitude * Math.PI / 180;
    const y = latitude * Math.PI / 180;
    return (
        Math.sin(x * 7 + Math.sin(y * 5)) * 0.42
        + Math.sin(y * 13 + x * 3) * 0.28
        + Math.sin(x * 23 - y * 17) * 0.18
        + Math.cos(x * 41 + y * 29) * 0.12
    );
}

function createTerrainTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 256;
    const context = canvas.getContext('2d');
    const image = context.createImageData(canvas.width, canvas.height);

    for (let y = 0; y < canvas.height; y += 1) {
        const latitude = 90 - (y / (canvas.height - 1)) * 180;
        for (let x = 0; x < canvas.width; x += 1) {
            const longitude = (x / (canvas.width - 1)) * 360 - 180;
            const variation = terrainNoise(longitude, latitude);
            const land = isLand(longitude, latitude);
            const elevation = variation + (latitude > 55 || latitude < -55 ? -0.08 : 0);
            let color;

            if (land) {
                if (elevation > 0.36) color = [226, 218, 179];
                else if (elevation > 0.12) color = [150, 177, 112];
                else if (elevation > -0.2) color = [89, 143, 104];
                else color = [52, 111, 92];
            } else {
                const depth = Math.max(0, Math.min(1, (variation + 1) / 2));
                color = [Math.round(12 + depth * 14), Math.round(54 + depth * 33), Math.round(91 + depth * 42)];
            }

            const offset = (y * canvas.width + x) * 4;
            image.data[offset] = color[0];
            image.data[offset + 1] = color[1];
            image.data[offset + 2] = color[2];
            image.data[offset + 3] = 255;
        }
    }

    context.putImageData(image, 0, 0);
    const texture = new THREE.CanvasTexture(canvas);
    texture.colorSpace = THREE.SRGBColorSpace;
    texture.anisotropy = 4;
    return texture;
}

function createStars() {
    const positions = new Float32Array(900 * 3);
    for (let i = 0; i < positions.length; i += 1) {
        positions[i] = (Math.random() - 0.5) * 45;
    }
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    const material = new THREE.PointsMaterial({ color: 0x9ab8d2, size: 0.035, transparent: true, opacity: 0.75 });
    return new THREE.Points(geometry, material);
}

export default function EarthGlobe() {
    const hostRef = useRef(null);

    useEffect(() => {
        const host = hostRef.current;
        if (!host) return undefined;

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(36, 1, 0.1, 100);
        camera.position.set(0, 0, 3.55);

        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
        renderer.outputColorSpace = THREE.SRGBColorSpace;
        renderer.setClearColor(0x000000, 0);
        host.appendChild(renderer.domElement);

        scene.add(new THREE.AmbientLight(0x9ab8d7, 1.15));
        const sunlight = new THREE.DirectionalLight(0xffedcf, 2.4);
        sunlight.position.set(-4, 2.5, 5);
        scene.add(sunlight);

        const earthGroup = new THREE.Group();
        scene.add(earthGroup);
        const texture = createTerrainTexture();
        const geometry = new THREE.SphereGeometry(1, 96, 64);
        const positions = geometry.attributes.position;
        const uvs = geometry.attributes.uv;

        for (let i = 0; i < positions.count; i += 1) {
            const longitude = uvs.getX(i) * 360 - 180;
            const latitude = uvs.getY(i) * 180 - 90;
            const land = isLand(longitude, latitude);
            const relief = land ? Math.max(0, terrainNoise(longitude, latitude)) * 0.012 : 0;
            const vertex = new THREE.Vector3().fromBufferAttribute(positions, i).normalize().multiplyScalar(1 + relief);
            positions.setXYZ(i, vertex.x, vertex.y, vertex.z);
        }
        geometry.computeVertexNormals();

        const earthMaterial = new THREE.MeshStandardMaterial({
            map: texture,
            roughness: 0.92,
            metalness: 0.02,
        });
        earthGroup.add(new THREE.Mesh(geometry, earthMaterial));
        scene.add(createStars());

        const resize = () => {
            const { width, height } = host.getBoundingClientRect();
            if (!width || !height) return;
            renderer.setSize(width, height, false);
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
        };
        const resizeObserver = new ResizeObserver(resize);
        resizeObserver.observe(host);
        resize();

        let dragging = false;
        let previousX = 0;
        let previousY = 0;
        const onPointerDown = (event) => {
            dragging = true;
            previousX = event.clientX;
            previousY = event.clientY;
            renderer.domElement.setPointerCapture(event.pointerId);
        };
        const onPointerMove = (event) => {
            if (!dragging) return;
            earthGroup.rotation.y += (event.clientX - previousX) * 0.006;
            earthGroup.rotation.x += (event.clientY - previousY) * 0.004;
            earthGroup.rotation.x = Math.max(-1.1, Math.min(1.1, earthGroup.rotation.x));
            previousX = event.clientX;
            previousY = event.clientY;
        };
        const onPointerUp = () => { dragging = false; };
        renderer.domElement.addEventListener('pointerdown', onPointerDown);
        renderer.domElement.addEventListener('pointermove', onPointerMove);
        renderer.domElement.addEventListener('pointerup', onPointerUp);
        renderer.domElement.addEventListener('pointercancel', onPointerUp);

        let frameId;
        const animate = () => {
            frameId = window.requestAnimationFrame(animate);
            if (!dragging) earthGroup.rotation.y += 0.0007;
            renderer.render(scene, camera);
        };
        animate();

        return () => {
            window.cancelAnimationFrame(frameId);
            resizeObserver.disconnect();
            renderer.domElement.removeEventListener('pointerdown', onPointerDown);
            renderer.domElement.removeEventListener('pointermove', onPointerMove);
            renderer.domElement.removeEventListener('pointerup', onPointerUp);
            renderer.domElement.removeEventListener('pointercancel', onPointerUp);
            geometry.dispose();
            texture.dispose();
            earthMaterial.dispose();
            scene.traverse((object) => {
                if (object.isPoints) {
                    object.geometry.dispose();
                    object.material.dispose();
                }
            });
            renderer.dispose();
            host.removeChild(renderer.domElement);
        };
    }, []);

    return <div className="earth-canvas" ref={hostRef} role="img" aria-label="Interactive low-resolution topographic globe of Earth" />;
}
