import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    st.error("DB connection string not available. Check the .env file")
    st.stop()

engine = create_engine(DB_URL)

def get_engine():
    return engine