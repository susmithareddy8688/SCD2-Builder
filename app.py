import streamlit as st
import pandas as pd
from src import scd2_processor as sp
from src import llm_helper as lh
st.title("AI Powered SCD2 Builder")
source_file = st.file_uploader("Upload Source CSV")
target_file = st.file_uploader("Upload Target CSV")
if source_file is not None and target_file is not None:
    source = pd.read_csv(source_file)
    target = pd.read_csv(target_file)
    target["Effective_To"]=(
        target["Effective_To"]
        .fillna("")
        .astype(str)
    )
    source.columns=source.columns.str.strip()
    target.columns=target.columns.str.strip()
    st.write("Source Data")
    st.dataframe(source)
    st.write("Target Data")
    st.dataframe(target)
    st.write("Source Columns:",source.columns.tolist())
    st.write("Target Columns:",target.columns.tolist())


    if st.button("Generate SCD2"):
        result,changes=sp.process_scd2(source,target)

        explanation = lh.explain_changes(changes)

        st.success("SCD2 Processing Completed")

        st.subheader("Output Data")
        st.dataframe(result)

        st.subheader("AI Explanation")
        st.text(explanation)