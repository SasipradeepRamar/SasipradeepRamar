import sqlite3
from googleapiclient.discovery import build

# YouTube API key
API_KEY = 'your_api_key_here'

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to fetch video details and insert into database
def fetch_and_store_video_data(video_id, cursor):
    video_response = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    video = video_response['items'][0]

    # Extract relevant data
    video_title = video['snippet']['title']
    views = video['statistics']['viewCount']
    likes = video['statistics'].get('likeCount', 0)
    dislikes = video['statistics'].get('dislikeCount', 0)

    # Insert into database
    cursor.execute("INSERT INTO videos (video_id, title, views, likes, dislikes) VALUES (?, ?, ?, ?, ?)",
                   (video_id, video_title, views, likes, dislikes))

# Initialize SQLite database
conn = sqlite3.connect('youtube_data.db')
cursor = conn.cursor()

# Create videos table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS videos
                  (video_id TEXT PRIMARY KEY, title TEXT, views INTEGER, likes INTEGER, dislikes INTEGER)''')

# Example video IDs
video_ids = ['video_id_1', 'video_id_2', 'video_id_3']

# Fetch and store data for each video
for video_id in video_ids:
    fetch_and_store_video_data(video_id, cursor)

# Commit changes and close connection
conn.commit()
conn.close()
