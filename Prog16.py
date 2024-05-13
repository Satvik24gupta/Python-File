#Create a program that uses a web scraping library to extract data from a website and then stores it in a database
import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to scrape data from the website
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting relevant data
    name = soup.find('h1', class_='firstHeading').text.strip()
    paragraphs = soup.find_all('p')
    content = "\n".join([p.text for p in paragraphs])
    
    return name, content

# Function to create database connection and store data
def create_database(name, content):
    try:
        conn = sqlite3.connect('wiki_data.db')
        cursor = conn.cursor()
        
        # Create table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS TaylorSwift
                     (id INTEGER PRIMARY KEY, name TEXT, content TEXT)''')
        
        # Insert data into the table
        cursor.execute("INSERT INTO TaylorSwift (name, content) VALUES (?, ?)", (name, content))
        
        conn.commit()
        conn.close()
        print("Data scraped and stored successfully!")
    except Exception as e:
        print("Error storing data in the database:", e)

# Main function
def main():
    url = "https://en.wikipedia.org/wiki/Taylor_Swift"
    name, content = scrape_website(url)
    create_database(name, content)

if __name__ == "__main__":
    main()
