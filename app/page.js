
import EarthGlobe from './earth-globe';

export default function HomePage() {
    return (
        <main className="earth-dashboard">
            <header className="topbar">
                <a className="brand" href="#" aria-label="Terra home">
                    <span className="brand-mark">T</span>
                    <span>TERRA<span className="brand-light">/ATLAS</span></span>
                </a>
                <div className="topbar-status"><span className="status-dot" /> PROCEDURAL TERRAIN MODEL</div>
                <div className="topbar-date">EARTH SYSTEMS <span>·</span> 2026</div>
            </header>

            <section className="hero">
                <div className="hero-copy">
                    <div className="eyebrow"><span>01</span> PLANETARY OVERVIEW</div>
                    <h1>One planet.<br /><em>Endless terrain.</em></h1>
                    <p className="intro">Explore Earth’s living surface, from ocean basins to the highest continental ranges.</p>
                    <div className="coordinates">
                        <div><span className="coordinate-label">REFERENCE</span><strong>WGS 84</strong></div>
                        <div><span className="coordinate-label">SURFACE</span><strong>TOPOGRAPHIC</strong></div>
                        <div><span className="coordinate-label">INTERACTION</span><strong>DRAG TO ROTATE</strong></div>
                    </div>
                </div>

                <div className="globe-stage">
                    <div className="orbit orbit-one" />
                    <div className="orbit orbit-two" />
                    <div className="globe-halo" />
                    <EarthGlobe />
                    <div className="globe-caption"><span className="status-dot" /> EARTH / 01</div>
                    <div className="globe-crosshair">+</div>
                </div>

                <aside className="terrain-panel">
                    <div className="panel-kicker">SURFACE PROFILE <span>01—06</span></div>
                    <h2>Global relief</h2>
                    <p>Land elevation and ocean depth, rendered as a color-banded terrain model.</p>
                    <div className="legend">
                        <div className="legend-row"><span className="swatch swatch-high" /><span>HIGH RELIEF</span><b>8,849 m</b></div>
                        <div className="legend-row"><span className="swatch swatch-mid" /><span>LAND MASS</span><b>0 m</b></div>
                        <div className="legend-row"><span className="swatch swatch-low" /><span>OCEAN FLOOR</span><b>−10,994 m</b></div>
                    </div>
                    <div className="panel-foot"><span>MODEL TYPE</span><b>ILLUSTRATIVE / LOW-RES</b></div>
                </aside>
            </section>

            <footer className="page-footer">
                <span>THE BLUE PLANET <span className="footer-divider">/</span> TERRAIN STUDY</span>
                <span>ROTATE THE GLOBE TO EXPLORE <span className="footer-arrow">↗</span></span>
            </footer>
        </main>
    );
}

