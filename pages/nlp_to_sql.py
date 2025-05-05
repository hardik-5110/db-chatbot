import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from pages.query_executer import get_table_schema  
from sqlalchemy import create_engine
from pages.db_connect import get_engine
engine = get_engine()  

load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")




def query_generator(user_question):
    # Fetch actual schema
    columns = get_table_schema(engine)
    schema_str = ", ".join(columns)

    # Enhanced prompt with schema context
    prompt = f"""
You are a SQL expert. Use the table 'countries' with the following columns:
{schema_str}

Return ONLY the raw SQL query for the following request. No explanations, no markdown, just the SQL:
{user_question}
"""

    try:
        response = model.generate_content(prompt)

        sql_query = response.text.strip()
        if sql_query.startswith("```sql"):
            sql_query = sql_query.replace("```sql", "").strip()
        if sql_query.endswith("```"):
            sql_query = sql_query[:-3].strip()

        return sql_query
    except Exception as e:
        return f"Error: {str(e)}"
