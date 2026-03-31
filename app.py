#streamlit app
from dotenv import load_dotenv # type: ignore
load_dotenv() # load all environment variables

import streamlit as st # type: ignore
import os
import sqlite3

import google.generativeai as genai # type: ignore
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#function to load google model and provide sql query as response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('models/gemini-2.5-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

#function to retrieve query from database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=["""You are an expert AI assistant specializing in converting natural language questions into SQL queries.

The SQL database is named STUDENT and contains the following columns:

NAME (VARCHAR)

CLASS (VARCHAR)

SECTION (VARCHAR)

MARKS (INT)

Follow these guidelines when generating SQL queries:

Ensure the output contains only the SQL query—do not include explanations, formatting marks, or extra text.

Use proper SQL syntax while maintaining accuracy and efficiency.

If the query involves filtering, apply appropriate WHERE clauses.

If an aggregation is required (e.g., counting records, averaging values), use functions like COUNT(), AVG(), etc.

Examples:
Question: "How many student records are present?"
SQL Query: SELECT COUNT(*) FROM STUDENT;

Question: "List all students in the Data Science class."
SQL Query: SELECT * FROM STUDENT WHERE CLASS = "Data Science";"""]


##Streamlit app
#Set page configuration with a title and icon

st.set_page_config(page_title="SQL Query Generator", page_icon=":guardsman:", layout="wide")
st.markdown("Akash's Gemini App - AI Powered SQL Query Generator")
st.markdown("Ask any question and I'll generate the SQL query for you!")

#User input
question=st.text_input("Enter your query here:", key="input")
submit=st.button("Generate SQL Query")
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"STUDENT.db")
    st.subheader("The response is:")
    for row in response:
        print(row)
        st.subheader(row)
        
