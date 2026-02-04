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

    .app-subtitle {
        color: #2c2c2c !important;
        font-family: "Georgia", serif;
        font-weight: 600;
        margin: 18px 0 6px;
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

if "po_description" not in st.session_state:
    st.session_state["po_description"] = ""
if "supplier" not in st.session_state:
    st.session_state["supplier"] = ""
if "result_raw" not in st.session_state:
    st.session_state["result_raw"] = None
if "result_json" not in st.session_state:
    st.session_state["result_json"] = None
if "result_error" not in st.session_state:
    st.session_state["result_error"] = None

def apply_sample(description: str, supplier_value: str) -> None:
    st.session_state["po_description"] = description
    st.session_state["supplier"] = supplier_value

st.markdown("<h3 class='app-subtitle'>Sample inputs</h3>", unsafe_allow_html=True)
st.caption("Click to prefill the form with an example.")
sample_col_1, sample_col_2 = st.columns(2)
with sample_col_1:
    st.button(
        "Office chairs",
        on_click=apply_sample,
        args=("Purchase of office chairs", "Staples"),
        use_container_width=True
    )
with sample_col_2:
    st.button(
        "Audit services",
        on_click=apply_sample,
        args=("Annual audit services for FY2025", "Deloitte"),
        use_container_width=True
    )

with st.form("po-classifier-form"):
    po_description = st.text_area(
        "PO Description",
        height=140,
        placeholder="e.g., Purchase of office chairs",
        help="Include key item/service details, quantities, or contract terms.",
        key="po_description"
    )
    st.caption(f"{len(po_description.strip())} characters")
    supplier = st.text_input(
        "Supplier (optional)",
        placeholder="e.g., Staples",
        key="supplier"
    )
    submit_disabled = not po_description.strip()
    submitted = st.form_submit_button("Classify PO", disabled=submit_disabled)

if submitted:
    description_value = po_description.strip()
    supplier_value = supplier.strip() or "Not provided"
    if not description_value:
        st.warning("Please enter a PO description.")
    else:
        with st.spinner("Classifying..."):
            try:
                result = classify_po(description_value, supplier_value)
            except Exception as exc:
                st.session_state["result_raw"] = None
                st.session_state["result_json"] = None
                st.session_state["result_error"] = ("exception", exc)
            else:
                st.session_state["result_raw"] = result
                try:
                    st.session_state["result_json"] = json.loads(result)
                    st.session_state["result_error"] = None
                except Exception:
                    st.session_state["result_json"] = None
                    st.session_state["result_error"] = ("json", "Invalid model response")

if (
    st.session_state["result_raw"] is not None
    or st.session_state["result_json"] is not None
    or st.session_state["result_error"] is not None
):
    st.markdown("<h3 class='app-subtitle'>Result</h3>", unsafe_allow_html=True)
    if st.session_state["result_error"]:
        error_type, error_detail = st.session_state["result_error"]
        if error_type == "exception":
            st.error("Something went wrong while classifying the PO.")
            st.exception(error_detail)
        else:
            st.error("Invalid model response")
    if st.session_state["result_json"] is not None:
        st.json(st.session_state["result_json"])
    if st.session_state["result_raw"] is not None:
        with st.expander("Show raw model response"):
            st.text(st.session_state["result_raw"])

st.markdown("</div>", unsafe_allow_html=True)
