import streamlit as st
import pandas as pd

def show_results(data: pd.DataFrame):
    if "error" in data.columns:
        st.error(f"❌ Error: {data['error'][0]}")
    elif data.empty:
        st.warning("⚠️ No results found.")
    else:
        st.dataframe(data, use_container_width=True)