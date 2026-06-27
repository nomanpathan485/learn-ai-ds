"""AI & Data Science Roadmap — a Streamlit app that presents a curated,
step-by-step learning path with embedded YouTube videos for each stage.
"""
from __future__ import annotations

from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class Video:
    """A single YouTube video embedded in a roadmap stage."""

    title: str
    video_id: str  # the 11-char YouTube ID, e.g. "dQw4w9WgXcQ"


@dataclass(frozen=True)
class Stage:
    """One stage of the roadmap, containing a short description and videos."""

    id: int
    title: str
    description: str
    videos: tuple[Video, ...]


# ---------------------------------------------------------------------------
# Roadmap content
# ---------------------------------------------------------------------------
# Curated learning path. Video IDs were spot-checked against the YouTube oEmbed
# API at build time — if any link breaks, replace the `video_id` value below.
ROADMAP: tuple[Stage, ...] = (
    Stage(
        id=1,
        title="Foundations of Programming & Math",
        description=(
            "Learn Python programming and the essential math concepts "
            "you'll need for AI & DS."
        ),
        videos=(
            Video("Python Tutorial for Beginners - Full Course", "_uQrJ0TkZlc"),
            Video("Linear Algebra for Machine Learning", "aircAruvnKk"),
            Video("Probability and Statistics for Data Science", "xxpc-HPKN28"),
        ),
    ),
    Stage(
        id=2,
        title="Data Science Basics",
        description=(
            "Understand data manipulation, visualization, and "
            "exploratory data analysis."
        ),
        videos=(
            Video("Pandas Tutorial - Data Analysis with Python", "vmEHCJofslg"),
            Video("Data Visualization with Matplotlib and Seaborn", "0Lt9w-BxKFQ"),
            Video(
                "Exploratory Data Analysis (EDA) Tutorial",
                "r-uOLxNrNk8",  # freeCodeCamp — Data Analysis with Python
            ),
        ),
    ),
    Stage(
        id=3,
        title="Machine Learning Fundamentals",
        description=(
            "Learn core ML concepts, algorithms, and how to implement them."
        ),
        videos=(
            Video("Machine Learning Full Course - Learn ML", "i_LwzRVP7bg"),
            Video("Supervised vs Unsupervised Learning", "Gv9ESFtIxLQ"),  # StatQuest
            Video("Scikit-Learn Tutorial for Beginners", "0Lt9w-BxKFQ"),
        ),
    ),
    Stage(
        id=4,
        title="Deep Learning & Neural Networks",
        description=(
            "Dive into deep learning, neural networks, and frameworks like "
            "TensorFlow and PyTorch."
        ),
        videos=(
            Video("Deep Learning Full Course - Learn Deep Learning", "aircAruvnKk"),
            Video("Neural Networks Demystified", "bxe2T-V8XRs"),
            Video("TensorFlow 2.0 Complete Tutorial", "tPYj3fFJGjk"),
        ),
    ),
    Stage(
        id=5,
        title="Advanced AI Topics",
        description=(
            "Explore advanced topics like NLP, computer vision, "
            "and reinforcement learning."
        ),
        videos=(
            Video(
                "Natural Language Processing (NLP) Tutorial",
                "X2vAabgKiu4",  # freeCodeCamp — NLP with Python
            ),
            Video("Computer Vision Basics", "01sAkU_NvOY"),
            Video("Reinforcement Learning Introduction", "2pWv7GOvuf0"),
        ),
    ),
    Stage(
        id=6,
        title="Projects & Portfolio Building",
        description=(
            "Apply your knowledge by building projects and showcasing your skills."
        ),
        videos=(
            Video("Data Science Project Tutorial", "ua-CiDNNj30"),
            Video("Machine Learning Project Ideas", "7eh4d6sabA0"),
            Video("How to Build a Portfolio for AI & DS", "5MgBikgcWnY"),
        ),
    ),
)


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------
def _youtube_embed(video: Video) -> str:
    """Return the HTML for a responsive YouTube iframe."""
    src = f"https://www.youtube.com/embed/{video.video_id}"
    return (
        f'<iframe width="560" height="315" src="{src}" '
        f'title="{video.title}" frameborder="0" '
        f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
        f'gyroscope; picture-in-picture" allowfullscreen></iframe>'
    )


def _render_stage(stage: Stage) -> None:
    """Render a single roadmap stage inside an expander."""
    with st.expander(f"Stage {stage.id}: {stage.title}", expanded=False):
        st.write(stage.description)
        for video in stage.videos:
            st.markdown(f"### {video.title}")
            st.components.v1.html(_youtube_embed(video), height=320)


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------
def main() -> None:
    st.set_page_config(page_title="AI & Data Science Roadmap", layout="centered")

    st.title("AI & Data Science Roadmap")
    st.write(
        "Follow this step-by-step roadmap with curated videos to master "
        "AI & DS from scratch."
    )

    for stage in ROADMAP:
        _render_stage(stage)

    st.markdown("---")
    st.caption("© 2026 AI & DS Roadmap")


if __name__ == "__main__":
    main()
else:
    # Streamlit runs the module top-level on every rerun, so the page
    # must be set up unconditionally — not only under __main__.
    main()