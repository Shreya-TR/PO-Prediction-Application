import streamlit as st
import json
from classifier import classify_po

st.set_page_config(page_title="PO Category Classifier", layout="centered")

st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background: linear-gradient(135deg, #f7f4ef 0%, #f0f7f5 100%);
    }

    /* Main card */
    .app-card {
        max-width: 760px;
        margin: 0 auto;
        padding: 28px 32px 22px;
        background: #ffffff;
        border: 1px solid #e7e2d7;
        border-radius: 18px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
    }

    /* Titles */
    h1 {
        font-family: "Georgia", serif;
        font-weight: 600;
        color: #2c2c2c;
        letter-spacing: 0.2px;
        margin-bottom: 6px;
    }

    /* Inputs */
    textarea, input {
        border-radius: 10px !important;
        border: 1px solid #d7d1c6 !important;
        padding: 10px 12px !important;
        font-size: 15px !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background: #1f6f5b;
        color: white;
        padding: 12px 14px;
        font-weight: 600;
        border-radius: 12px;
        border: none;
        transition: transform 0.06s ease;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        background: #1a5f4e;
    }

    /* Result box */
    .result-box {
        background: #f7fbfa;
        border: 1px dashed #c9ded8;
        border-radius: 12px;
        padding: 14px;
        margin-top: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='app-card'>", unsafe_allow_html=True)

st.title("PO L1–L2–L3 Classifier")
st.caption("Paste a PO description and (optionally) a supplier. Get structured category output.")

po_description = st.text_area("PO Description", height=140, placeholder="e.g., Purchase of office chairs for new workspace")
supplier = st.text_input("Supplier (optional)", placeholder="e.g., Staples, Steelcase")

if st.button("Classify"):
    if not po_description.strip():
        st.warning("Please enter a PO description.")
    else:
        with st.spinner("Classifying..."):
            result = classify_po(po_description, supplier)

        try:
            parsed = json.loads(result)
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.json(parsed)
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception:
            st.error("Invalid model response")
            st.text(result)

st.markdown("</div>", unsafe_allow_html=True)
