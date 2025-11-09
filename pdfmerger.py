import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

st.title("📚 PDF Merger")
st.write("Upload up to 100 PDF files to merge them into one.")

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if len(uploaded_files) > 100:
        st.error("⚠️ You can upload a maximum of 100 files.")
    else:
        if st.button("Merge PDFs"):
            merger = PdfMerger()
            for file in uploaded_files:
                merger.append(file)

            merged_pdf = BytesIO()
            merger.write(merged_pdf)
            merger.close()
            merged_pdf.seek(0)

            st.success("✅ PDFs merged successfully!")
            st.download_button(
                label="📥 Download Merged PDF",
                data=merged_pdf,
                file_name="merged.pdf",
                mime="application/pdf"
            )

