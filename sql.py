from dotenv import load_dotenv

load_dotenv() # load all environment variables from .env

import streamlit as st
import os
import sqlite3
import google.generativeai as genai




## Configure Gen Ai KEy

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load google gemini model and give query as  response

def get_gemini_response(question, prompt):
        print("gemini_response executing")
        model = genai.GenerativeModel("gemini-pro")
        gemini_response=model.generate_content([prompt[0],question]) 
        return gemini_response.text 

#function to retrieve query from the database


def read_sql_query(sql,db):
        print("read_sql_query executiong")
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute(sql)
        rows= cur.fetchall()
        conn.close()
        for row in rows:
            print(row)
        return(rows)



### Define your prompt

prompt =[
    """ You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns NAME, CLASS
SECTION \n\nFor example, In Example 1 How many entries of records are present?,
the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
/n Example 2 - How many student study in DataScience class, the query will be
select * from student where class = "DataScience";
Also the sql query should be without back tick signs and sql (```sql )
"""
]



### Streamlit  App

st.set_page_config(page_title="Convert Text to SQL Query")
st.header("Gemini App to convert you Text to SQL Query")
question = st.text_input("Input",key="input")

submit=st.button("Ask the Question")

# if submit is clicked
if submit:
       response = get_gemini_response(question,prompt)
       print(response)
        # Clean up the SQL response
       cleaned_response = response.replace("```sql", "").replace("```", "").strip()
       print("Cleaned Response:", cleaned_response)
       sql_response = read_sql_query(cleaned_response,"student.db")
       st.subheader("The Response is: ")
       for row in sql_response:
              st.write(row)

submit_all = st.button("Run Selecit * Query")
if submit_all:
       query="Select * from student"
       sql_response_all = read_sql_query(query,"student.db")
       st.subheader("All Recores are: ")
       for row in sql_response_all:
              st.write(row)