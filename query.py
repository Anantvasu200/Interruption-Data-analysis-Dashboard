import mysql.connector
import streamlit as st

# CONNECTION
conn=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    db="mydb"
)

c=conn.cursor()

# Fetching data
def view_all_data():
    c.execute("select * from working_dataset_2 ORDER BY id asc")
    data = c.fetchall()
    return data


