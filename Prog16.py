#Create a program that uses a web scraping library to extract data from a website and then stores it in a database
import requests
from bs4 import BeautifulSoup
import sqlite3

# Send a GET request to the website
url = "https://www.youtube.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the data from the website
    titles = soup.find_all('h2', class_='title')
    descriptions = soup.find_all('p', class_='description')

    # Create a connection to the SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS data
                 (title TEXT, description TEXT)''')

    # Insert the extracted data into the database
    for title, description in zip(titles, descriptions):
        c.execute("INSERT INTO data VALUES (?, ?)",
                  (title.text, description.text))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Data extracted and stored in the database successfully.")
else:
    print("Failed to retrieve the website content.")
