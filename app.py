from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

import streamlit as st


# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Portfolio",
    layout="wide",
)

PAGE_TITLE = "Data Scientist - Spécialisation MLOps"

PRESENTATION_TEXT = """My drive to transform raw data into intelligent systems, shaped by a dual background 
in economics and machine learning engineering, pushes me to go far beyond prototyping. 
Passionate about designing robust data pipelines, motivated by the challenges of scalability and production performance, 
and committed to a rigorous MLOps approach in cloud environments such as GCP, 
my goal is to contribute to organizations that turn data into a true competitive advantage from business framing to production deployment.
"""

CV_FR_PATH = Path("assets/cv/CV_MAYEUR_Nicolas.pdf")
CV_EN_PATH = Path("assets/cv/cv_en.pdf")

PROJECT_IMAGES: Dict[str, List[Path]] = {
    "project_1": [
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
    "project_2": [
        Path("assets/cv/slide/Project_2_Slide_1.png"),
        Path("assets/cv/slide/Project_2_Slide_2.png"),
    ],
    "project_3": [
        Path("assets/cv/slide/Project_3_Slide_1.png"),
        Path("assets/cv/slide/Project_3_Slide_2.png"),
        Path("assets/cv/slide/Project_3_Slide_3.png"),
    ],
}

PROJECT_LINKS = {
    "project_1": "https://mlpricingoptimization-kxjlxkbc2fllxyyh46ndaj.streamlit.app/",
    "project_2": "https://featurestore-fgjbmprebhrkn39kwrkpcq.streamlit.app/",
    "project_3": "https://aiagentformonitoringinsight-mltbbbymjfxuwjlzz2dl8q.streamlit.app/",
}

PROJECT_TITLES = {
    "project_1": "ML Pricing optimisation",
    "project_2": "Feature Store",
    "project_3": "AI agent for monitoring insight",
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


def truncate_text(text: str, max_chars: int = 500) -> str:
    text = text.strip()
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut + "…"


def toggle_presentation() -> None:
    st.session_state.presentation_expanded = not st.session_state.presentation_expanded


def render_section_label(label: str) -> None:
    st.markdown(
        f'<div class="section-label">{label}</div>',
        unsafe_allow_html=True,
    )


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
    images: List[Path],
    key_prefix: str,
    url: Optional[str] = None,
) -> None:
    with st.container(key=container_key):
        st.markdown(f'<div class="project-title">{title}</div>', unsafe_allow_html=True)

        if url:
            _, col, _ = st.columns([1, 2, 1])
            with col:
                st.link_button("Open project", url, width="stretch")

        valid = [img for img in images if img.exists()]

        if not valid:
            st.markdown(
                '<div class="empty-box">No image available</div>',
                unsafe_allow_html=True,
            )
            return

        if len(valid) == 1:
            render_image_frame(valid[0])
            return

        state_key = f"{key_prefix}_idx"
        if state_key not in st.session_state:
            st.session_state[state_key] = 0

        left, center, right = st.columns([1, 8, 1])

        with left:
            if st.button("←", key=f"{key_prefix}_prev"):
                st.session_state[state_key] = (
                    st.session_state[state_key] - 1
                ) % len(valid)

        with right:
            if st.button("→", key=f"{key_prefix}_next"):
                st.session_state[state_key] = (
                    st.session_state[state_key] + 1
                ) % len(valid)

        with center:
            idx = st.session_state[state_key]
            render_image_frame(valid[idx], f"Image {idx + 1} / {len(valid)}")


# =========================
# SESSION
# =========================
if "presentation_expanded" not in st.session_state:
    st.session_state.presentation_expanded = False


# =========================
# CSS : DARK FUTURIST
# =========================
CSS = """
/* =========================
   GLOBAL APP
========================= */
.stApp {
    background:
        radial-gradient(circle at 12% 12%, rgba(0, 255, 247, 0.08), transparent 20%),
        radial-gradient(circle at 88% 10%, rgba(129, 71, 255, 0.10), transparent 18%),
        radial-gradient(circle at 50% 100%, rgba(0, 180, 255, 0.07), transparent 24%),
        linear-gradient(180deg, #02050b 0%, #050913 40%, #070d19 100%);
    color: #f3f8ff;
}

/* faint cyber grid */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    background:
        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 42px 42px;
    mask-image: linear-gradient(to bottom, rgba(255,255,255,0.25), transparent 65%);
    -webkit-mask-image: linear-gradient(to bottom, rgba(255,255,255,0.25), transparent 65%);
    opacity: 0.18;
    z-index: 0;
}

div.block-container {
    max-width: 1280px;
    padding-top: 2rem;
    padding-bottom: 3rem;
    position: relative;
    z-index: 1;
}

header[data-testid="stHeader"] {
    background: transparent;
}

html, body, [class*="css"] {
    font-family: "Inter", "Segoe UI", sans-serif;
}

/* =========================
   TYPO / LABELS
========================= */
.section-label {
    text-align: center;
    font-size: 1.02rem;
    font-weight: 800;
    letter-spacing: 2.6px;
    text-transform: uppercase;
    color: #8ef8ff;
    margin: 0.15rem 0 1rem 0;
    text-shadow:
        0 0 8px rgba(0, 245, 255, 0.28),
        0 0 24px rgba(123, 44, 255, 0.10);
    position: relative;
}

.section-label::after {
    content: "";
    display: block;
    width: 140px;
    height: 1px;
    margin: 0.8rem auto 0 auto;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(0,245,255,0.9),
        rgba(123,44,255,0.8),
        transparent
    );
    box-shadow: 0 0 12px rgba(0,245,255,0.25);
}

/* =========================
   TITLE BOX
========================= */
.st-key-title_box {
    position: relative;
    overflow: hidden;
    border-radius: 24px;
    padding: 34px 28px;
    margin-bottom: 2.2rem;
    background:
        linear-gradient(135deg, rgba(10, 16, 28, 0.94), rgba(14, 22, 39, 0.88)),
        rgba(255,255,255,0.02);
    border: 1px solid rgba(119, 221, 255, 0.14);
    box-shadow:
        0 16px 48px rgba(0,0,0,0.48),
        0 0 24px rgba(0,245,255,0.08),
        0 0 42px rgba(123,44,255,0.08),
        inset 0 1px 0 rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
    transition: all 0.28s ease;
}

.st-key-title_box::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(
            110deg,
            transparent 0%,
            rgba(255,255,255,0.04) 18%,
            transparent 36%
        );
    pointer-events: none;
}

.st-key-title_box:hover {
    transform: translateY(-2px);
    border-color: rgba(0,245,255,0.22);
    box-shadow:
        0 18px 56px rgba(0,0,0,0.54),
        0 0 32px rgba(0,245,255,0.12),
        0 0 50px rgba(123,44,255,0.10),
        inset 0 1px 0 rgba(255,255,255,0.07);
}

.st-key-title_box h1 {
    margin: 0;
    text-align: center;
    font-size: 2.15rem;
    font-weight: 900;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    color: #f7fbff;
    text-shadow:
        0 0 10px rgba(0,245,255,0.22),
        0 0 28px rgba(123,44,255,0.14);
}

/* =========================
   PANELS / CARDS
========================= */
.st-key-presentation_box,
.st-key-cv_box,
.st-key-project_1_box,
.st-key-project_2_box,
.st-key-project_3_box {
    position: relative;
    overflow: hidden;
    border-radius: 22px;
    padding: 24px;
    margin-bottom: 1.6rem;
    background:
        linear-gradient(180deg, rgba(8, 13, 24, 0.95), rgba(6, 10, 18, 0.98));
    border: 1px solid rgba(140, 214, 255, 0.10);
    box-shadow:
        0 16px 38px rgba(0,0,0,0.44),
        0 0 18px rgba(0,245,255,0.05),
        inset 0 1px 0 rgba(255,255,255,0.04);
    backdrop-filter: blur(8px);
    transition: all 0.25s ease;
}

.st-key-presentation_box::before,
.st-key-cv_box::before,
.st-key-project_1_box::before,
.st-key-project_2_box::before,
.st-key-project_3_box::before {
    content: "";
    position: absolute;
    top: 0;
    left: 18px;
    right: 18px;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(0,245,255,0.45),
        rgba(123,44,255,0.32),
        transparent
    );
    opacity: 0.9;
}

.st-key-presentation_box:hover,
.st-key-cv_box:hover,
.st-key-project_1_box:hover,
.st-key-project_2_box:hover,
.st-key-project_3_box:hover {
    transform: translateY(-3px);
    border-color: rgba(0,245,255,0.16);
    box-shadow:
        0 20px 48px rgba(0,0,0,0.52),
        0 0 24px rgba(0,245,255,0.08),
        0 0 36px rgba(123,44,255,0.07),
        inset 0 1px 0 rgba(255,255,255,0.05);
}

/* =========================
   TEXT
========================= */
.presentation-text {
    font-size: 1.02rem;
    line-height: 1.85;
    color: #d9e8fb;
    margin-bottom: 1rem;
}

/* =========================
   PROJECT TITLES (FUTURIST)
========================= */
.project-title {
    text-align: center;
    font-size: 1.25rem;
    font-weight: 900;
    letter-spacing: 1px;
    margin-bottom: 1.2rem;

    background: linear-gradient(
        90deg,
        #8ef8ff,
        #a88bff,
        #8ef8ff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 10px rgba(0,245,255,0.35),
        0 0 22px rgba(123,44,255,0.25);

    position: relative;
}

.project-title::after {
    content: "";
    display: block;
    width: 120px;
    height: 2px;
    margin: 0.6rem auto 0 auto;

    background: linear-gradient(
        90deg,
        transparent,
        rgba(0,245,255,0.9),
        rgba(123,44,255,0.9),
        transparent
    );

    box-shadow:
        0 0 10px rgba(0,245,255,0.4),
        0 0 20px rgba(123,44,255,0.3);
}

.carousel-counter {
    text-align: center;
    color: #91a7cb;
    margin-top: 0.85rem;
    font-size: 0.92rem;
    letter-spacing: 0.3px;
}

/* =========================
   IMAGE FRAME
========================= */
.image-frame {
    padding: 1rem;
    margin: 1rem 0 1.5rem 0;
    border-radius: 22px;
    background: linear-gradient(
        180deg,
        rgba(255,255,255,0.025),
        rgba(255,255,255,0.012)
    );
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow:
        0 25px 60px rgba(0,0,0,0.52),
        inset 0 1px 0 rgba(255,255,255,0.05);
}

.image-frame [data-testid="stImage"] {
    border-radius: 18px;
    overflow: hidden;
}

.image-frame [data-testid="stImage"] img {
    border-radius: 18px !important;
    width: 100%;
    height: auto;
    box-shadow: 0 18px 40px rgba(0,0,0,0.50) !important;
    filter: none !important;
    transform: none !important;
}

/* hide fullscreen */
button[title="View fullscreen"],
button[aria-label="View fullscreen"] {
    display: none !important;
    visibility: hidden !important;
    pointer-events: none !important;
}

[data-testid="stImage"] button {
    display: none !important;
}

/* =========================
   EMPTY STATE
========================= */
.empty-box {
    border: 1px dashed rgba(255,255,255,0.10);
    border-radius: 16px;
    padding: 1rem;
    text-align: center;
    color: #94a7c3;
    background: rgba(255,255,255,0.02);
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.03);
}

/* =========================
   BUTTONS
========================= */
.stButton > button,
.stDownloadButton > button {
    width: 100%;
    min-height: 50px;
    border-radius: 14px !important;
    border: 1px solid rgba(144, 223, 255, 0.14) !important;
    background:
        linear-gradient(180deg, rgba(13, 20, 36, 0.98), rgba(8, 13, 24, 0.98)) !important;
    color: #f6fbff !important;
    font-weight: 800 !important;
    letter-spacing: 0.25px;
    box-shadow:
        0 10px 24px rgba(0,0,0,0.34),
        0 0 14px rgba(0,245,255,0.05),
        inset 0 1px 0 rgba(255,255,255,0.05);
    transition: all 0.22s ease !important;
}

/* =========================
   PROJECT BUTTON (FUTURIST CTA)
========================= */
a[data-testid="stLinkButton"] {
    position: relative;
    overflow: hidden;

    display: inline-flex !important;
    justify-content: center;
    align-items: center;

    width: 100% !important;
    min-height: 52px !important;

    padding: 0.6rem 1rem !important;
    border-radius: 16px !important;

    border: 1px solid rgba(0,245,255,0.35) !important;

    background:
        linear-gradient(180deg, rgba(10,18,32,0.95), rgba(6,10,20,0.95)) !important;

    color: #e9fbff !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px;

    text-decoration: none !important;

    box-shadow:
        0 10px 26px rgba(0,0,0,0.45),
        0 0 18px rgba(0,245,255,0.12),
        inset 0 1px 0 rgba(255,255,255,0.06);

    transition: all 0.25s ease !important;
}

a[data-testid="stLinkButton"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;

    background: linear-gradient(
        90deg,
        transparent,
        rgba(0,245,255,0.25),
        transparent
    );

    transition: left 0.5s ease;
}

a[data-testid="stLinkButton"]:hover::before {
    left: 100%;
}

a[data-testid="stLinkButton"]:hover {
    transform: translateY(-2px);

    border-color: rgba(0,245,255,0.7) !important;
    color: #ffffff !important;

    box-shadow:
        0 16px 34px rgba(0,0,0,0.5),
        0 0 28px rgba(0,245,255,0.25),
        0 0 40px rgba(123,44,255,0.15),
        inset 0 1px 0 rgba(255,255,255,0.08);
}

div[data-testid="column"] .stButton > button {
    min-height: 56px;
    font-size: 1.08rem !important;
}

/* =========================
   STREAMLIT TEXT
========================= */
.stCaption {
    color: #7d93b3 !important;
}

p, li, span, div {
    color: inherit;
}
"""
inject_css(CSS)


# =========================
# TITLE
# =========================
_, col, _ = st.columns([0.5, 8, 0.5])
with col:
    with st.container(key="title_box"):
        st.markdown(f"<h1>{PAGE_TITLE}</h1>", unsafe_allow_html=True)


# =========================
# PRESENTATION
# =========================
_, col, _ = st.columns([0.5, 8, 0.5])
with col:
    render_section_label("Presentation")

    with st.container(key="presentation_box"):
        text = (
            PRESENTATION_TEXT
            if st.session_state.presentation_expanded
            else truncate_text(PRESENTATION_TEXT)
        )
        st.markdown(f'<div class="presentation-text">{text}</div>', unsafe_allow_html=True)
        st.button(
            "Less" if st.session_state.presentation_expanded else "More",
            key="presentation_toggle",
            on_click=toggle_presentation,
        )


# =========================
# CV
# =========================
_, col, _ = st.columns([0.5, 8, 0.5])
with col:
    render_section_label("My CVs")

    with st.container(key="cv_box"):
        c1, c2 = st.columns(2)

        with c1:
            if CV_FR_PATH.exists():
                st.download_button(
                    "CV FR",
                    read_bytes(CV_FR_PATH),
                    "CV_MAYEUR_Nicolas.pdf",
                    mime="application/pdf",
                )
            else:
                st.caption("Coming Soon")

        with c2:
            if CV_EN_PATH.exists():
                st.download_button(
                    "CV EN",
                    read_bytes(CV_EN_PATH),
                    "CV_MAYEUR_Nicolas_EN.pdf",
                    mime="application/pdf",
                )
            else:
                st.caption("CV ENG : Coming Soon")


# =========================
# PROJECTS
# =========================
_, col, _ = st.columns([0.5, 8, 0.5])
with col:
    render_section_label("Projects")

    render_project_carousel(
        "project_1_box",
        PROJECT_TITLES["project_1"],
        PROJECT_IMAGES["project_1"],
        "p1",
        PROJECT_LINKS["project_1"],
    )

    render_project_carousel(
        "project_2_box",
        PROJECT_TITLES["project_2"],
        PROJECT_IMAGES["project_2"],
        "p2",
        PROJECT_LINKS["project_2"],
    )

    render_project_carousel(
        "project_3_box",
        PROJECT_TITLES["project_3"],
        PROJECT_IMAGES["project_3"],
        "p3",
        PROJECT_LINKS["project_3"],
    )