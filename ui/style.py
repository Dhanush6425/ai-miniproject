import streamlit as st


def apply_styles():
    st.markdown(
        """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

    /* ---------- GLOBAL ---------- */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        font-size: 95%;
    }

    /* ---------- MAIN HEADER ---------- */
    .main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 600;
        letter-spacing: -0.5px;
        color: white;
        margin-bottom: 0;
    }

    .sub-title {
        text-align: center;
        color: #aaa;
        margin-bottom: 1.5rem;
        font-weight: 300;
    }

    /* ---------- ANSWER CARD ---------- */
    .answer-card {
        background: linear-gradient(135deg, #1a1f35 0%, #141824 100%);
        border-left: 4px solid #4361ee;
        padding: 14px 16px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 3px 16px rgba(67,97,238,0.08);
        transition: 0.2s;
    }

    .answer-card:hover {
        box-shadow: 0 6px 22px rgba(67,97,238,0.18);
    }

    /* ---------- BADGES ---------- */
    .badge {
        display: inline-block;
        background: linear-gradient(90deg, #4361ee, #7b5ea7);
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 500;
        margin-bottom: 6px;
    }

    .upload-badge {
        display: inline-block;
        background: linear-gradient(90deg, #0ea47a, #0d7a5c);
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 500;
        margin-bottom: 6px;
    }

    /* ---------- QUESTION ---------- */
    .question-header {
        font-size: 1rem;
        font-weight: 600;
        color: #e0e4ff;
        margin-bottom: 4px;
        padding-bottom: 4px;
        border-bottom: 1px solid #2a2f4a;
    }

    /* ---------- CONTEXT ---------- */
    .context-card {
        background: #0e1122;
        border: 1px solid #2a2f4a;
        padding: 10px 12px;
        border-radius: 8px;
        font-family: 'DM Mono', monospace;
        font-size: 0.75rem;
        color: #9aa3c2;
        margin-top: 8px;
    }

    /* ---------- TIMESTAMP ---------- */
    .timestamp {
        font-size: 0.65rem;
        color: #666;
        text-align: right;
        margin-top: 3px;
    }

    /* ---------- EMPTY STATE ---------- */
    .empty-state {
        text-align: center;
        padding: 50px 20px;
        color: #666;
    }

    .empty-state .icon {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }

    /* ---------- UPLOAD PANEL ---------- */
    .upload-panel {
        background: linear-gradient(135deg, #0f1f18 0%, #0a1510 100%);
        border: 1px solid #1a4a35;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 16px;
    }

    /* ---------- MEETING SELECTOR ---------- */
    .meeting-selector-panel {
        background: linear-gradient(135deg, #1a1228 0%, #110e1c 100%);
        border: 1px solid #2e1f4a;
        border-radius: 12px;
        padding: 14px 16px;
        margin-bottom: 16px;
    }

    /* ---------- MODE LABEL ---------- */
    .mode-label {
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: #0ea47a;
        margin-bottom: 6px;
    }

    /* =========================================================
       🔥 SIDEBAR FULL CONTROL
    ========================================================= */

   /* ---------- SIDEBAR HEADER ---------- */
.sidebar-header {
    text-align: center;
    padding: 12px 0 18px 0;
}

.sidebar-icon {
    font-size: 1.8rem;
}

.sidebar-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-top: 4px;
}

.sidebar-subtitle {
    font-size: 0.75rem;
    color: #9aa3c2;
    margin-top: 2px;
}
    /* ---------- SCROLLBAR ---------- */
    ::-webkit-scrollbar {
        width: 6px;
    }

    ::-webkit-scrollbar-thumb {
        background: #333;
        border-radius: 10px;
    }

    </style>
    """,
        unsafe_allow_html=True,
    )
