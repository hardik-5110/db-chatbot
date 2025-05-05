from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from datetime import datetime
from pages.chat_history import add_to_chat_history, clear_chat_history, init_chat_history
from pages.display_result import show_results
from pages.nlp_to_sql import query_generator
from pages.query_executer import execute_sql
from pages.pdf_exporter import export_text_to_pdf


st.set_page_config(page_title="chats", page_icon="💬", layout="wide")

st.markdown("""
    <div style="font-weight:bold; font-size:2.5rem; text-align: left;">
        <span style="color: blue;">DB</span>-ChatBot
    </div>
""", unsafe_allow_html=True)


# sidebar for chat history
init_chat_history(st.session_state)

st.sidebar.title("🗂️ Chat History")

for chat in reversed(st.session_state.chat_history):
    st.sidebar.markdown(f"🕒 *{chat['timestamp']}*")
    st.sidebar.markdown(f"🧑‍💬 **You:** {chat['question']}")
    st.sidebar.markdown(f"🧠 **SQL:**\n```\n{chat['generated_sql']}\n```")


if st.sidebar.button("🧹 Clear Chat"):
    clear_chat_history(st.session_state)



user_input = st.chat_input("Say something")
if user_input:
    st.write(f"**You:** {user_input}")
    generated_sql = query_generator(user_input)
    st.write(f"**SQL Query**\n{generated_sql}")
    
    st.write(f"Executing SQL: {generated_sql}")
    
    fetched_data = execute_sql(generated_sql)
    show_results(fetched_data)
    add_to_chat_history(st.session_state, user_input, generated_sql)



if st.session_state.chat_history:
    if st.button("📄 Get Chat in PDF"):
        combined_md = "\n\n---\n\n".join(f"🕒 {chat['timestamp']}\n🧑‍💬 You: {chat['question']}\n\n🧠 SQL:\n{chat['generated_sql']}"
        for chat in st.session_state.chat_history)
        export_text_to_pdf(combined_md, "chat_output.pdf")
        with open("chat_output.pdf", "rb") as f:
            st.download_button("Download PDF", f, file_name="chat_output.pdf", mime="application/pdf")

