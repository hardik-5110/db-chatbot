import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <div style="text-align: center;">
        <h1 style="color:#4A90E2;">👋 Welcome to DB-ChatBot</h1>
        <p style="font-size:1.2rem;">Your AI-powered assistant to convert natural language into SQL and fetch data from your database.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

if st.button("🚀 Start Chatting with DB"):
    st.switch_page("pages/chat.py")
