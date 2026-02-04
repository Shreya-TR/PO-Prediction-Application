import streamlit as st
import json
from classifier import classify_po

st.set_page_config(page_title="PO Category Classifier", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: #f7f4ef;
    }

    .app-card {
        max-width: 760px;
        margin: 0 auto;
        padding: 24px 28px 20px;
        background: #ffffff;
        border: 1px solid #e7e2d7;
        border-radius: 14px;
        box-shadow: 0 10px 32px rgba(0, 0, 0, 0.08);
    }

    .app-title {
        color: #2c2c2c !important;
        font-family: "Georgia", serif;
        font-weight: 600;
        margin-bottom: 4px;
    }

    .stCaption {
        color: #2c2c2c !important;
    }

    label, .stTextInput label, .stTextArea label {
        color: #2c2c2c !important;
        font-weight: 600;
    }

    textarea, input {
        color: #1f1f1f !important;
        background: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #d7d1c6 !important;
        padding: 10px 12px !important;
        font-size: 15px !important;
    }

    textarea::placeholder, input::placeholder {
        color: #6a6a6a !important;
        opacity: 1;
    }

    .stButton > button {
        width: 100%;
        background: #1f6f5b;
        color: #ffffff;
        padding: 12px 14px;
        font-weight: 600;
        border-radius: 12px;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='app-card'>", unsafe_allow_html=True)

st.markdown("<h1 class='app-title'>PO L1-L2-L3 Classifier</h1>", unsafe_allow_html=True)
st.caption("Paste a PO description and (optionally) a supplier. Get structured category output.")

po_description = st.text_area(
    "PO Description",
    height=140,
    placeholder="e.g., Purchase of office chairs"
)
supplier = st.text_input(
    "Supplier (optional)",
    placeholder="e.g., Staples"
)

if st.button("Classify"):
    if not po_description.strip():
        st.warning("Please enter a PO description.")
    else:
        with st.spinner("Classifying..."):
            result = classify_po(po_description, supplier)

        try:
            st.json(json.loads(result))
        except Exception:
            st.error("Invalid model response")
            st.text(result)

st.markdown("</div>", unsafe_allow_html=True)
