import streamlit as st
import sqlite3

# Function to connect to SQLite database
def connect_db():
    return sqlite3.connect('youtube_data.db')

# Function to fetch video data from database
def fetch_video_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos")
    data = cursor.fetchall()
    conn.close()
    return data

# Streamlit code for dashboard
st.title('YouTube Data Dashboard')

# Fetch data from database
videos = fetch_video_data()

# Display data in a table
st.write("## Video Data")
st.table(videos)
