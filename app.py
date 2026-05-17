from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

import streamlit as st


# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Nicolas Mayeur — Data Engineer specialized in Machine Learning on GCP",
    layout="wide",
)

PRESENTATION_TEXT = """I build end-to-end machine learning systems that transform raw data into scalable, production-ready solutions.
With a background in economics and machine learning engineering, I focus on designing robust data pipelines, ensuring data quality, and deploying models in cloud environments such as Google Cloud Platform (GCP). My approach combines data engineering, MLOps practices, and business understanding to deliver reliable and high-impact data products.
I am particularly motivated by challenges related to scalability, system performance, and turning data into a real competitive advantage."""

CV_FR_PATH = Path("assets/cv/CV_MAYEUR_Nicolas.pdf")
CV_EN_PATH = Path("assets/cv/cv_en.pdf")

PROJECT_IMAGES: Dict[str, List[Path]] = {
    "project_1": [
        Path("assets/cv/slide/project2/projet2slide1.png"),
        Path("assets/cv/slide/project2/projet2slide2.png"),
        Path("assets/cv/slide/project2/projet2slide3.png"),
        Path("assets/cv/slide/project2/projet2slide4.png"),
        Path("assets/cv/slide/project2/projet2slide5.png"),
        Path("assets/cv/slide/project2/projet2slide6.png"),
        Path("assets/cv/slide/project2/projet2slide7.png"),
        Path("assets/cv/slide/project2/projet2slide8.png"),
        Path("assets/cv/slide/project2/projet2slide9.png"),
        Path("assets/cv/slide/project2/projet2slide10.png"),
    ],
    "project_2": [
        Path("assets/cv/slide/projet1/projet1slide1.png"),
        Path("assets/cv/slide/projet1/projet1slide2.png"),
        Path("assets/cv/slide/projet1/projet1slide3.png"),
        Path("assets/cv/slide/projet1/projet1slide4.png"),
        Path("assets/cv/slide/projet1/projet1slide5.png"),
        Path("assets/cv/slide/projet1/projet1slide6.png"),
        Path("assets/cv/slide/projet1/projet1slide7.png"),
        Path("assets/cv/slide/projet1/projet1slide8.png"),
        Path("assets/cv/slide/projet1/projet1slide9.png"),
    ],
    "project_3": [
        Path("assets/cv/slide/Project_3_Slide_1.png"),
        Path("assets/cv/slide/Project_3_Slide_2.png"),
        Path("assets/cv/slide/Project_3_Slide_3.png"),
    ],
}

PROJECT_LINKS = {
    "project_1": "https://featurestore-ddtx8txqfrtjrnlozeybu5.streamlit.app/Pipeline_Monitoring",
    "project_2": "https://mlpricingoptimization-kxjlxkbc2fllxyyh46ndaj.streamlit.app/",
    "project_3": "https://aiagentformonitoringinsight-mltbbbymjfxuwjlzz2dl8q.streamlit.app/",
}

PROJECT_TITLES = {
    "project_1": "GCP Feature Store (Lakehouse)",
    "project_2": "ML Pricing Optimisation",
    "project_3": "AI Agent for Monitoring Insight",
}

PROJECT_NUMS = {
    "project_1": "01",
    "project_2": "02",
    "project_3": "03",
}

# Tags grouped by category: (category_label, color_key, [tags])
# color_key: "blue" | "teal" | "violet"
PROJECT_BADGE_GROUPS: Dict[str, List[tuple]] = {
    "project_1": [
        ("Data Engineering", "blue",   ["BigQuery", "dbt", "Lakehouse", "GCS", "Data Modeling"]),
        ("ML Systems",       "teal",   ["Feature Store", "Time Series ML", "Feature Engineering", "Monitoring"]),
        ("Cloud & MLOps",    "violet", ["Cloud Run", "CI/CD", "Docker", "GitHub Actions"]),
    ],
    "project_2": [
        ("ML Systems",       "teal",   ["Random Forest", "SHAP", "ML Pipelines", "Feature Engineering"]),
        ("Cloud & MLOps",    "violet", ["FastAPI", "Docker", "Streamlit"]),
    ],
    "project_3": [
        ("ML Systems",       "teal",   ["LLM", "RAG", "Agent", "ML Pipelines"]),
        ("Cloud & MLOps",    "violet", ["Vertex AI", "GCP", "CI/CD"]),
    ],
}

IMAGE_DISPLAY_WIDTH = 1100


# =========================
# HELPERS
# =========================
def inject_css(css: str) -> None:
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def truncate_text(text: str, max_chars: int = 320) -> str:
    text = text.strip()
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut + "\u2026"


def toggle_presentation() -> None:
    st.session_state.presentation_expanded = not st.session_state.presentation_expanded


def render_section_label(label: str, num: str = "") -> None:
    num_html = f'<span class="section-num">{num}</span>' if num else ""
    st.markdown(
        f'<div class="section-label">{num_html}'
        f'<span class="section-text">{label}</span>'
        f'<span class="section-line"></span></div>',
        unsafe_allow_html=True,
    )


def render_badge_groups(groups: List[tuple]) -> str:
    """Render grouped skill badges as HTML."""
    html = '<div class="badge-groups">'
    for category, color, tags in groups:
        badges = "".join(
            f'<span class="badge badge-{color}">{t}</span>' for t in tags
        )
        html += (
            f'<div class="badge-group">'
            f'<span class="badge-category">{category}</span>'
            f'<div class="badge-row">{badges}</div>'
            f'</div>'
        )
    html += "</div>"
    return html


def render_image_frame(image_path: Path, caption: Optional[str] = None) -> None:
    st.markdown('<div class="image-frame">', unsafe_allow_html=True)
    st.image(str(image_path), width=IMAGE_DISPLAY_WIDTH)
    if caption:
        st.markdown(
            f'<div class="carousel-counter">{caption}</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)


def render_project_carousel(
    container_key: str,
    title: str,
    num: str,
    images: List[Path],
    key_prefix: str,
    url: Optional[str] = None,
    badge_groups: Optional[List[tuple]] = None,
) -> None:
    with st.container(key=container_key):
        badges_html = render_badge_groups(badge_groups) if badge_groups else ""

        st.markdown(
            f'<div class="project-header">'
            f'<span class="project-num">{num}</span>'
            f'<div class="project-title">{title}</div>'
            f'</div>'
            f'{badges_html}',
            unsafe_allow_html=True,
        )

        if url:
            _, col, _ = st.columns([2, 1.5, 2])
            with col:
                st.link_button("View project \u2192", url, width="stretch")

        valid = [img for img in images if img.exists()]

        if not valid:
            st.markdown('<div class="empty-box">No image available</div>', unsafe_allow_html=True)
            return

        if len(valid) == 1:
            render_image_frame(valid[0])
            return

        state_key = f"{key_prefix}_idx"
        if state_key not in st.session_state:
            st.session_state[state_key] = 0

        left, center, right = st.columns([1, 10, 1])

        with left:
            if st.button("\u2190", key=f"{key_prefix}_prev"):
                st.session_state[state_key] = (st.session_state[state_key] - 1) % len(valid)
        with right:
            if st.button("\u2192", key=f"{key_prefix}_next"):
                st.session_state[state_key] = (st.session_state[state_key] + 1) % len(valid)
        with center:
            idx = st.session_state[state_key]
            render_image_frame(valid[idx], f"{idx + 1} / {len(valid)}")


# =========================
# SESSION
# =========================
if "presentation_expanded" not in st.session_state:
    st.session_state.presentation_expanded = False


# =========================
# CSS — ELECTRIC BLUE
# =========================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;900&family=Space+Mono:wght@400;700&display=swap');

.stApp {
    background: #F0F4FF;
    color: #0F1A3E;
}

div.block-container {
    max-width: 1160px;
    padding-top: 0;
    padding-bottom: 5rem;
}

header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    -webkit-font-smoothing: antialiased;
}

/* === HERO === */
.st-key-hero_box {
    background: #2D5BE3;
    margin-left: -1rem;
    margin-right: -1rem;
    padding: 3.5rem 4rem 3.2rem;
    position: relative;
    overflow: hidden;
}

.st-key-hero_box::before {
    content: "";
    position: absolute;
    top: -60px; right: -60px;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: rgba(255,255,255,0.06);
    pointer-events: none;
}

.st-key-hero_box::after {
    content: "";
    position: absolute;
    bottom: -80px; right: 160px;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: rgba(255,255,255,0.04);
    pointer-events: none;
}

.hero-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.5);
    margin-bottom: 0.9rem;
}

.hero-name {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(2.4rem, 4vw, 3.6rem);
    font-weight: 900;
    color: #ffffff;
    letter-spacing: -1.5px;
    line-height: 1.05;
    margin-bottom: 1.2rem;
}

.st-key-hero_box a[data-testid="stLinkButton"] {
    display: inline-flex !important;
    width: auto !important;
    min-height: 44px !important;
    padding: 0.5rem 1.4rem !important;
    border-radius: 8px !important;
    border: 1.5px solid rgba(255,255,255,0.6) !important;
    background: rgba(255,255,255,0.12) !important;
    color: #ffffff !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px;
    text-transform: none;
    text-decoration: none !important;
    box-shadow: none !important;
    margin-top: 1.2rem;
    transition: all 0.18s !important;
}

.st-key-hero_box a[data-testid="stLinkButton"]:hover {
    background: rgba(255,255,255,0.22) !important;
    border-color: #ffffff !important;
    transform: none;
    box-shadow: none !important;
}

/* === SECTION LABELS === */
.section-label {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin: 2.2rem 0 1.1rem;
}

.section-num {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    font-weight: 700;
    color: #2D5BE3;
    letter-spacing: 1px;
}

.section-text {
    font-family: 'Outfit', sans-serif;
    font-size: 0.76rem;
    font-weight: 600;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #3A5BD9;
    white-space: nowrap;
}

.section-line {
    flex: 1;
    height: 1.5px;
    background: #C5D1F7;
}

/* === CARDS === */
.st-key-about_box,
.st-key-cv_box,
.st-key-project_1_box,
.st-key-project_2_box,
.st-key-project_3_box {
    background: #ffffff;
    border: 1px solid #D4DCFA;
    border-radius: 12px;
    padding: 1.8rem 2rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.st-key-about_box:hover,
.st-key-cv_box:hover {
    border-color: #2D5BE3;
    box-shadow: 0 4px 24px rgba(45,91,227,0.08);
}

.st-key-project_1_box,
.st-key-project_2_box,
.st-key-project_3_box {
    border-left: 3px solid #2D5BE3;
}

.st-key-project_1_box:hover,
.st-key-project_2_box:hover,
.st-key-project_3_box:hover {
    border-color: #2D5BE3;
    box-shadow: 0 4px 24px rgba(45,91,227,0.08);
}

/* === PRESENTATION TEXT === */
.presentation-text {
    font-family: 'Outfit', sans-serif;
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.9;
    color: #3A4A7A;
    margin-bottom: 1.2rem;
    max-width: 74ch;
}

/* === PROJECT HEADER === */
.project-header {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 1rem;
}

.project-num {
    font-family: 'Space Mono', monospace;
    font-size: 1.8rem;
    font-weight: 700;
    color: #C5D1F7;
    line-height: 1;
    flex-shrink: 0;
}

.project-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #0F1A3E;
    letter-spacing: -0.3px;
    line-height: 1.2;
}

/* === HERO BADGES (white-on-blue variant) === */
.st-key-hero_box .badge-groups {
    margin-bottom: 0;
    margin-top: 0.2rem;
}

.st-key-hero_box .badge-category {
    color: rgba(255,255,255,0.45);
}

.st-key-hero_box .badge-blue {
    color: #ffffff;
    background: rgba(255,255,255,0.12);
    border-color: rgba(255,255,255,0.25);
}

.st-key-hero_box .badge-teal {
    color: #9FE1CB;
    background: rgba(13,148,120,0.25);
    border-color: rgba(159,225,203,0.35);
}

.st-key-hero_box .badge-violet {
    color: #C8C2F2;
    background: rgba(83,74,183,0.3);
    border-color: rgba(200,194,242,0.35);
}

/* === SKILL BADGES === */
.badge-groups {
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    margin-bottom: 1.2rem;
}

.badge-group {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    flex-wrap: wrap;
}

.badge-category {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #8899CC;
    white-space: nowrap;
    min-width: 110px;
}

.badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
}

.badge {
    font-family: 'Space Mono', monospace;
    font-size: 0.63rem;
    font-weight: 400;
    letter-spacing: 0.3px;
    border-radius: 4px;
    padding: 0.2rem 0.55rem;
    border: 1px solid;
}

.badge-blue {
    color: #1A3ABF;
    background: #EBF0FF;
    border-color: #B8C8F8;
}

.badge-teal {
    color: #0F6E56;
    background: #E0FAF3;
    border-color: #9FE1CB;
}

.badge-violet {
    color: #4A35A8;
    background: #EEECFD;
    border-color: #C8C2F2;
}

/* === IMAGE FRAME === */
.carousel-counter {
    text-align: center;
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 2px;
    color: #A0AECF;
    margin-top: 0.8rem;
}

.image-frame {
    margin: 1rem 0 0.5rem;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #D4DCFA;
    background: #F8F9FF;
}

.image-frame [data-testid="stImage"] img {
    border-radius: 0 !important;
    width: 100%;
    height: auto;
    display: block;
    opacity: 0.97;
    transition: opacity 0.2s;
}

.image-frame:hover [data-testid="stImage"] img { opacity: 1; }

button[title="View fullscreen"],
button[aria-label="View fullscreen"] { display: none !important; }
[data-testid="stImage"] button { display: none !important; }

/* === EMPTY STATE === */
.empty-box {
    border: 1px dashed #C5D1F7;
    border-radius: 8px;
    padding: 2rem;
    text-align: center;
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 1.5px;
    color: #A0AECF;
}

/* === NAV BUTTONS === */
.stButton > button {
    min-height: 44px;
    border-radius: 8px !important;
    border: 1.5px solid #C5D1F7 !important;
    background: #ffffff !important;
    color: #2D5BE3 !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    box-shadow: none !important;
    transition: all 0.15s !important;
    width: 100%;
}

.stButton > button:hover {
    border-color: #2D5BE3 !important;
    background: #EBF0FF !important;
    color: #1A3ABF !important;
}

.st-key-about_box .stButton > button {
    min-height: 36px;
    font-size: 0.8rem !important;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

/* === DOWNLOAD BUTTONS === */
.stDownloadButton > button {
    width: 100%;
    min-height: 54px;
    border-radius: 8px !important;
    border: 1.5px solid #C5D1F7 !important;
    background: #ffffff !important;
    color: #0F1A3E !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: none !important;
    transition: all 0.18s !important;
}

.stDownloadButton > button:hover {
    border-color: #2D5BE3 !important;
    background: #EBF0FF !important;
    color: #2D5BE3 !important;
}

/* === LINK BUTTON === */
a[data-testid="stLinkButton"] {
    display: inline-flex !important;
    justify-content: center;
    align-items: center;
    width: 100% !important;
    min-height: 48px !important;
    padding: 0.5rem 1.2rem !important;
    border-radius: 8px !important;
    border: none !important;
    background: #2D5BE3 !important;
    color: #ffffff !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    text-decoration: none !important;
    box-shadow: 0 4px 14px rgba(45,91,227,0.25) !important;
    transition: all 0.18s !important;
}

a[data-testid="stLinkButton"]:hover {
    background: #1A3ABF !important;
    box-shadow: 0 6px 20px rgba(45,91,227,0.35) !important;
    transform: translateY(-1px);
}

p, li, span, div { color: inherit; }
.stCaption { color: #A0AECF !important; }
"""
inject_css(CSS)


# =========================
# HERO
# =========================
with st.container(key="hero_box"):
    hero_badge_groups = [
        ("Data Engineering", "blue",   ["BigQuery", "dbt", "Lakehouse", "GCS", "Data Modeling"]),
        ("ML Systems",       "teal",   ["Feature Store", "Time Series ML", "ML Pipelines", "Feature Engineering", "Monitoring"]),
        ("Cloud & MLOps",    "violet", ["Cloud Run", "CI/CD", "Docker", "GitHub Actions", "Infrastructure Design"]),
    ]
    badges_html = render_badge_groups(hero_badge_groups)
    st.markdown(
        '<div class="hero-eyebrow">Portfolio — Nicolas Mayeur</div>'
        '<div class="hero-name">Data Engineer<br>with ML expertise</div>'
        f'{badges_html}',
        unsafe_allow_html=True,
    )
    st.link_button("View GitHub repos \u2192", "https://github.com/MYR-Nicolas", type="primary")


# =========================
# ABOUT
# =========================
_, col, _ = st.columns([0.3, 9, 0.3])
with col:
    render_section_label("About", "00 —")
    with st.container(key="about_box"):
        text = (
            PRESENTATION_TEXT
            if st.session_state.presentation_expanded
            else truncate_text(PRESENTATION_TEXT)
        )
        st.markdown(f'<div class="presentation-text">{text}</div>', unsafe_allow_html=True)
        label = "Show less" if st.session_state.presentation_expanded else "Read more"
        st.button(label, key="presentation_toggle", on_click=toggle_presentation)


# =========================
# CV
# =========================
_, col, _ = st.columns([0.3, 9, 0.3])
with col:
    render_section_label("Curriculum Vitæ", "01 —")
    with st.container(key="cv_box"):
        c1, c2 = st.columns(2)
        with c1:
            if CV_FR_PATH.exists():
                st.download_button(
                    "Download CV — FR",
                    read_bytes(CV_FR_PATH),
                    "CV_MAYEUR_Nicolas.pdf",
                    mime="application/pdf",
                )
            else:
                st.caption("Coming soon")
        with c2:
            if CV_EN_PATH.exists():
                st.download_button(
                    "Download CV — EN",
                    read_bytes(CV_EN_PATH),
                    "CV_MAYEUR_Nicolas_EN.pdf",
                    mime="application/pdf",
                )
            else:
                st.caption("Coming soon")


# =========================
# PROJECTS
# =========================
_, col, _ = st.columns([0.3, 9, 0.3])
with col:
    render_section_label("Selected Projects", "02 —")

    render_project_carousel(
        "project_1_box",
        PROJECT_TITLES["project_1"],
        PROJECT_NUMS["project_1"],
        PROJECT_IMAGES["project_1"],
        "p1",
        PROJECT_LINKS["project_1"],
        PROJECT_BADGE_GROUPS["project_1"],
    )

    render_project_carousel(
        "project_2_box",
        PROJECT_TITLES["project_2"],
        PROJECT_NUMS["project_2"],
        PROJECT_IMAGES["project_2"],
        "p2",
        PROJECT_LINKS["project_2"],
        PROJECT_BADGE_GROUPS["project_2"],
    )

    render_project_carousel(
        "project_3_box",
        PROJECT_TITLES["project_3"],
        PROJECT_NUMS["project_3"],
        PROJECT_IMAGES["project_3"],
        "p3",
        PROJECT_LINKS["project_3"],
        PROJECT_BADGE_GROUPS["project_3"],
    )