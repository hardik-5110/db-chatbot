import os
import streamlit as st
from datetime import datetime

def init_chat_history(session_state):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def add_to_chat_history(session_state, user_input, generated_sql):
    session_state.chat_history.append({
        "question": user_input,
        "generated_sql": generated_sql,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def clear_chat_history(session_state):
    session_state.chat_history = []