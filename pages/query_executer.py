import pandas as pd
from pages.db_connect import get_engine
engine = get_engine()
import sqlalchemy

def get_table_schema(engine, table_name="countries"):
    query = f"""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = '{table_name}';
    """
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text(query))
        columns = [row[0] for row in result]
    return columns

def execute_sql(query: str) -> pd.DataFrame:
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            df = pd.read_sql(query, con=conn)
            trans.commit()
            return df
        except Exception as e:
            trans.rollback()
            return pd.DataFrame({"error": [str(e)]})