import streamlit as st


st.set_page_config(
		page_title="Terra Atlas | Earth Terrain",
		page_icon="🌍",
		layout="wide",
		initial_sidebar_state="collapsed",
)
st.markdown(
		"""
		<style>
		@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap');

		:root {
				--ink: #e8f0f3;
				--muted: #91a6b0;
				--line: rgba(165, 194, 205, 0.18);
				--mint: #9dcac2;
				--gold: #d3a875;
		}

		html, body, [data-testid="stAppViewContainer"] {
				background: #07131d;
				color: var(--ink);
				font-family: 'DM Sans', sans-serif;
		}
		[data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer {
				visibility: hidden;
				height: 0;
		}
		[data-testid="stAppViewContainer"] > .main {
				background:
						radial-gradient(ellipse at 53% 47%, rgba(12, 49, 68, 0.42), transparent 43%),
						#07131d;
		}
		.block-container {
				max-width: 1440px;
				padding: 0 clamp(20px, 5vw, 76px) 20px;
		}
		.atlas-header {
				min-height: 76px;
				display: flex;
				align-items: center;
				justify-content: space-between;
				gap: 20px;
				border-bottom: 1px solid var(--line);
				color: var(--ink);
		}
		.atlas-brand {
				display: flex;
				align-items: center;
				gap: 12px;
				font-size: 13px;
				font-weight: 600;
				letter-spacing: 2px;
				white-space: nowrap;
		}
		.brand-mark {
				width: 28px;
				height: 28px;
				display: grid;
				place-items: center;
				border: 1px solid #78b5bb;
				border-radius: 50%;
				color: #a9d8d1;
				font-family: Georgia, serif;
				font-size: 15px;
				letter-spacing: 0;
		}
		.brand-light { color: #77909e; font-weight: 400; }
		.header-meta, .eyebrow, .coordinate-label, .panel-kicker,
		.legend-row, .panel-foot, .globe-caption, .page-footer {
				font-size: 9px;
				letter-spacing: 1.4px;
		}
		.header-meta { color: #a9bec6; }
		.header-date { color: #8398a4; text-align: right; }
		.signal-dot {
				display: inline-block;
				width: 6px;
				height: 6px;
				margin-right: 8px;
				border-radius: 50%;
				background: #81cbb2;
				box-shadow: 0 0 10px rgba(129, 203, 178, 0.6);
				vertical-align: 1px;
		}
		.hero-copy { padding: 60px 0 30px; }
		.eyebrow { color: #91bfc0; }
		.eyebrow span { margin-right: 10px; color: var(--gold); }
		.hero-title {
				margin: 24px 0 17px;
				color: #e4eef0;
				font-family: 'Playfair Display', Georgia, serif;
				font-size: clamp(36px, 4vw, 54px);
				font-weight: 400;
				line-height: 1.08;
		}
		.hero-title em { color: var(--mint); font-weight: 400; }
		.intro {
				max-width: 290px;
				color: var(--muted);
				font-size: 12px;
				line-height: 1.9;
		}
		.coordinates {
				display: grid;
				gap: 15px;
				margin-top: 40px;
				padding-top: 18px;
				border-top: 1px solid var(--line);
		}
		.coordinate-row { display: flex; justify-content: space-between; gap: 8px; }
		.coordinate-label { color: #728794; font-size: 8px; }
		.coordinate-value { color: #bed0d4; font-size: 9px; letter-spacing: .8px; }
		.panel { margin-top: 35px; padding-top: 18px; border-top: 1px solid rgba(157, 202, 194, .48); }
		.panel-kicker { display: flex; justify-content: space-between; color: #91bfc0; }
		.panel-kicker span { color: #718996; }
		.panel-title { margin: 22px 0 10px; color: #e0eaed; font: 400 20px 'Playfair Display', Georgia, serif; }
		.panel-description { color: var(--muted); font-size: 11px; line-height: 1.8; }
		.legend { display: grid; gap: 17px; margin: 27px 0; }
		.legend-row { display: grid; grid-template-columns: 9px 1fr auto; align-items: center; gap: 8px; color: #90a5ad; font-size: 8px; }
		.legend-row b { color: #c5d5d8; font-size: 9px; font-weight: 500; letter-spacing: .3px; white-space: nowrap; }
		.swatch { width: 7px; height: 7px; border-radius: 50%; }
		.swatch-high { background: #d6bd8b; }
		.swatch-mid { background: #76a783; }
		.swatch-low { background: #286d8b; }
		.panel-foot { display: flex; justify-content: space-between; gap: 8px; padding-top: 15px; border-top: 1px solid var(--line); color: #728794; font-size: 8px; }
		.panel-foot b { color: #b6c8cc; font-size: 8px; font-weight: 500; text-align: right; }
		[data-testid="stHorizontalBlock"] { align-items: center; gap: clamp(14px, 2.8vw, 42px); }
		[data-testid="stColumn"] { min-width: 0; }
		.page-footer {
				display: flex;
				justify-content: space-between;
				gap: 14px;
				padding: 18px 0 12px;
				border-top: 1px solid var(--line);
				color: #748a96;
				font-size: 8px;
		}
		.footer-divider { padding: 0 6px; color: #9dcac2; }
		.footer-arrow { padding-left: 5px; color: #d3a875; }

		@media (max-width: 850px) {
				.block-container { padding: 0 22px 18px; }
				[data-testid="stHorizontalBlock"] { flex-wrap: wrap; }
				[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
						flex: 1 1 100%;
						width: 100%;
				}
				.hero-copy { padding: 34px 0 0; }
				.coordinates { grid-template-columns: repeat(3, 1fr); gap: 10px; }
				.coordinate-row { display: grid; gap: 5px; }
				.panel { margin: 0 0 30px; }
				.atlas-header { min-height: 64px; }
				.header-meta { display: none; }
		}
		@media (max-width: 480px) {
				.block-container { padding-right: 16px; padding-left: 16px; }
				.hero-title { font-size: 38px; }
				.header-date { font-size: 8px; }
				.page-footer { flex-wrap: wrap; }
		}
		</style>
		""",
		unsafe_allow_html=True,
)

st.markdown(
		"""
		<div class="atlas-header">
			<div class="atlas-brand"><span class="brand-mark">T</span><span>TERRA<span class="brand-light">/ATLAS</span></span></div>
			<div class="header-meta"><span class="signal-dot"></span>PROCEDURAL TERRAIN MODEL</div>
			<div class="header-date">EARTH SYSTEMS <span>·</span> 2026</div>
		</div>
		""",
		unsafe_allow_html=True,
)

left, center, right = st.columns([0.86, 1.5, 0.8], gap="medium")

with left:
		st.markdown(
				"""
				<section class="hero-copy">
					<div class="eyebrow"><span>01</span> PLANETARY OVERVIEW</div>
					<h1 class="hero-title">One planet.<br><em>Endless terrain.</em></h1>
					<p class="intro">Explore Earth's living surface, from ocean basins to the highest continental ranges.</p>
					<div class="coordinates">
						<div class="coordinate-row"><span class="coordinate-label">REFERENCE</span><strong class="coordinate-value">WGS 84</strong></div>
						<div class="coordinate-row"><span class="coordinate-label">SURFACE</span><strong class="coordinate-value">TOPOGRAPHIC</strong></div>
						<div class="coordinate-row"><span class="coordinate-label">INTERACTION</span><strong class="coordinate-value">DRAG TO ROTATE</strong></div>
					</div>
				</section>
				""",
				unsafe_allow_html=True,
		)

with center:
		st.html(
				"""
					<style>
						* { box-sizing: border-box; }
						.atlas-globe-stage { position: relative; width: min(100%, 500px); aspect-ratio: 1; margin: auto; }
						canvas { display: block; width: 100%; height: 100%; cursor: grab; touch-action: none; }
						canvas:active { cursor: grabbing; }
						.caption { position: absolute; bottom: 8%; left: 3%; color: #91aab3; font: 8px 'DM Sans', sans-serif; letter-spacing: 1.4px; pointer-events: none; }
						.caption span { display: inline-block; width: 5px; height: 5px; margin-right: 7px; border-radius: 50%; background: #81cbb2; box-shadow: 0 0 9px #81cbb2; vertical-align: 1px; }
						.crosshair { position: absolute; top: 8%; right: 12%; color: rgba(180, 214, 215, .55); font: 18px sans-serif; pointer-events: none; }
					</style>
					<div class="atlas-globe-stage">
						<canvas id="globe" width="480" height="480" aria-label="Interactive topographic globe of Earth"></canvas>
						<div class="caption"><span></span>EARTH / 01</div>
						<div class="crosshair">+</div>
					</div>
					<script>
						const canvas = document.getElementById('globe');
						const ctx = canvas.getContext('2d');
						const size = canvas.width;
						const center = size / 2;
						const radius = 158;
						const polygons = [
							[[-168,70],[-145,72],[-125,60],[-115,48],[-96,50],[-82,25],[-98,15],[-112,28],[-130,48],[-155,58]],
							[[-81,12],[-66,10],[-50,-2],[-44,-20],[-54,-40],[-70,-55],[-76,-30],[-80,-8]],
							[[-11,72],[30,70],[42,55],[28,42],[38,30],[20,10],[10,-5],[30,-35],[17,-35],[-2,-15],[-15,5],[-18,35],[-8,52]],
							[[28,70],[65,75],[105,72],[145,60],[170,52],[155,40],[130,35],[120,20],[105,5],[80,8],[65,25],[45,28],[35,45]],
							[[112,-11],[130,-10],[153,-20],[151,-39],[134,-44],[115,-33]],
							[[-52,83],[-25,78],[-37,60],[-54,60],[-64,72]],
							[[46,-13],[50,-18],[49,-25],[45,-23]],
							[[-180,-70],[-120,-73],[-60,-75],[0,-72],[60,-74],[120,-72],[180,-70],[180,-90],[-180,-90]]
						];

						const map = document.createElement('canvas');
						map.width = 720;
						map.height = 360;
						const mapCtx = map.getContext('2d');
						mapCtx.fillStyle = '#fff';
						mapCtx.fillRect(0, 0, map.width, map.height);
						const mask = document.createElement('canvas');
						mask.width = map.width;
						mask.height = map.height;
						const maskCtx = mask.getContext('2d');
						maskCtx.fillStyle = '#fff';
						for (const polygon of polygons) {
							maskCtx.beginPath();
							polygon.forEach(([lon, lat], index) => {
								const x = (lon + 180) / 360 * map.width;
								const y = (90 - lat) / 180 * map.height;
								if (index === 0) maskCtx.moveTo(x, y); else maskCtx.lineTo(x, y);
							});
							maskCtx.closePath();
							maskCtx.fill();
						}
						const maskData = maskCtx.getImageData(0, 0, map.width, map.height).data;
						const terrain = mapCtx.createImageData(map.width, map.height);
						for (let y = 0; y < map.height; y += 1) {
							for (let x = 0; x < map.width; x += 1) {
								const i = (y * map.width + x) * 4;
								const n = Math.sin(x * 0.035 + Math.sin(y * 0.05)) * 0.42
									+ Math.sin(y * 0.09 + x * 0.018) * 0.32
									+ Math.sin(x * 0.12 - y * 0.08) * 0.26;
								let color;
								if (maskData[i + 3] > 0) {
									color = n > 0.32 ? [218, 198, 151] : n > 0.05 ? [138, 169, 112] : n > -0.3 ? [80, 139, 103] : [50, 105, 88];
								} else {
									const depth = Math.max(0, Math.min(1, (n + 1) / 2));
									color = [12 + depth * 14, 54 + depth * 33, 91 + depth * 42];
								}
								terrain.data[i] = color[0];
								terrain.data[i + 1] = color[1];
								terrain.data[i + 2] = color[2];
								terrain.data[i + 3] = 255;
							}
						}
						mapCtx.putImageData(terrain, 0, 0);
						const mapData = mapCtx.getImageData(0, 0, map.width, map.height).data;
						const frame = ctx.createImageData(size, size);
						const stars = Array.from({ length: 110 }, () => [Math.random() * size, Math.random() * size, Math.random() * 1.1 + 0.25]);
						let rotation = -0.35;
						let dragging = false;
						let previousX = 0;
						let previousY = 0;
						let lastFrame = 0;

						function render(time) {
							requestAnimationFrame(render);
							if (time - lastFrame < 32) return;
							lastFrame = time;
							if (!dragging) rotation += 0.0014;
							const pixels = frame.data;
							for (let y = 0; y < size; y += 1) {
								const ny = (y - center) / radius;
								for (let x = 0; x < size; x += 1) {
									const nx = (x - center) / radius;
									const d = nx * nx + ny * ny;
									const out = (y * size + x) * 4;
									if (d > 1) { pixels[out + 3] = 0; continue; }
									const z = Math.sqrt(1 - d);
									let lon = Math.atan2(nx, z) - rotation;
									lon = ((lon + Math.PI) % (2 * Math.PI) + 2 * Math.PI) % (2 * Math.PI) - Math.PI;
									const lat = Math.asin(-ny);
									const tx = Math.floor((lon / (2 * Math.PI) + 0.5) * map.width);
									const ty = Math.max(0, Math.min(map.height - 1, Math.floor((0.5 - lat / Math.PI) * map.height)));
									const source = (ty * map.width + Math.max(0, Math.min(map.width - 1, tx))) * 4;
									const light = Math.max(0.28, Math.min(1.12, 0.42 + nx * -0.25 + (-ny) * 0.2 + z * 0.68));
									pixels[out] = mapData[source] * light;
									pixels[out + 1] = mapData[source + 1] * light;
									pixels[out + 2] = mapData[source + 2] * light;
									pixels[out + 3] = 255;
								}
							}
							ctx.clearRect(0, 0, size, size);
							for (const [x, y, alpha] of stars) {
								ctx.fillStyle = `rgba(174, 204, 218, ${alpha * 0.65})`;
								ctx.fillRect(x, y, 1.2, 1.2);
							}
							ctx.save();
							ctx.translate(center, center);
							ctx.rotate(-0.45);
							ctx.strokeStyle = 'rgba(146, 190, 197, .15)';
							ctx.lineWidth = 1;
							ctx.beginPath();
							ctx.ellipse(0, 0, radius * 1.42, radius * 0.58, 0, 0, Math.PI * 2);
							ctx.stroke();
							ctx.restore();
							const glow = ctx.createRadialGradient(center, center, radius * 0.78, center, center, radius * 1.35);
							glow.addColorStop(0, 'rgba(51, 133, 153, .15)');
							glow.addColorStop(1, 'rgba(51, 133, 153, 0)');
							ctx.fillStyle = glow;
							ctx.beginPath();
							ctx.arc(center, center, radius * 1.35, 0, Math.PI * 2);
							ctx.fill();
							ctx.putImageData(frame, 0, 0);
							ctx.beginPath();
							ctx.arc(center, center, radius, 0, Math.PI * 2);
							ctx.strokeStyle = 'rgba(134, 194, 196, .42)';
							ctx.lineWidth = 1;
							ctx.stroke();
						}

						canvas.addEventListener('pointerdown', (event) => {
							dragging = true;
							previousX = event.clientX;
							previousY = event.clientY;
							canvas.setPointerCapture(event.pointerId);
						});
						canvas.addEventListener('pointermove', (event) => {
							if (!dragging) return;
							rotation += (event.clientX - previousX) * 0.009;
							previousX = event.clientX;
							previousY = event.clientY;
						});
						const stopDragging = () => { dragging = false; };
						canvas.addEventListener('pointerup', stopDragging);
						canvas.addEventListener('pointercancel', stopDragging);
						requestAnimationFrame(render);
					</script>
				""",
				unsafe_allow_javascript=True,
		)

with right:
		st.markdown(
				"""
				<section class="panel">
					<div class="panel-kicker">SURFACE PROFILE <span>01—06</span></div>
					<h2 class="panel-title">Global relief</h2>
					<p class="panel-description">Land elevation and ocean depth, rendered as a color-banded terrain model.</p>
					<div class="legend">
						<div class="legend-row"><span class="swatch swatch-high"></span><span>HIGH RELIEF</span><b>8,849 m</b></div>
						<div class="legend-row"><span class="swatch swatch-mid"></span><span>LAND MASS</span><b>0 m</b></div>
						<div class="legend-row"><span class="swatch swatch-low"></span><span>OCEAN FLOOR</span><b>−10,994 m</b></div>
					</div>
					<div class="panel-foot"><span>MODEL TYPE</span><b>ILLUSTRATIVE / LOW-RES</b></div>
				</section>
				""",
				unsafe_allow_html=True,
		)

st.markdown(
		"""
		<div class="page-footer">
			<span>THE BLUE PLANET <span class="footer-divider">/</span> TERRAIN STUDY</span>
			<span>ROTATE THE GLOBE TO EXPLORE <span class="footer-arrow">↗</span></span>
		</div>
		""",
		unsafe_allow_html=True,
)
