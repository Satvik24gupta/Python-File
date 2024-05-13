# #Create a program that uses a web scraping library to extract data from a website and then stores it in a database
# import requests
# from bs4 import BeautifulSoup
# import html5lib
# import sqlite3

# # Send a GET request to the website
# url = "https://www.youtube.com"
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Extract the data from the website
#     titles = soup.find_all('h2', class_='title')
#     descriptions = soup.find_all('p', class_='description')

#     # Create a connection to the SQLite database
#     conn = sqlite3.connect('data.db')
#     c = conn.cursor()

#     # Create a table if it doesn't exist
#     c.execute('''CREATE TABLE IF NOT EXISTS data
#                  (title TEXT, description TEXT)''')

#     # Insert the extracted data into the database
#     for title, description in zip(titles, descriptions):
#         c.execute("INSERT INTO data VALUES (?, ?)",
#                   (title.text, description.text))

#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()

#     print("Data extracted and stored in the database successfully.")
# else:
#     print("Failed to retrieve the website content.")





import requests
from bs4 import BeautifulSoup
import mysql.connector

# MySQL connection details
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="Prog16"
)

# Create a cursor object
cursor = db.cursor()

# Create a table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS website_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        description VARCHAR(255),
        link VARCHAR(2550)
    )
""")

# URL to scrape
# url = "https://www.example.com"
# url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
url = "https://en.wikipedia.org/wiki/Amitabh_Bachchan"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# print("Abc")
# Find the desired data
# for item in soup.find_all("div", class_="item"):
for item in soup.find_all("div"):
    # title = item.find("h2").text.strip()
    title = item.find("title")
    # description = item.find("p").text.strip()
    description = item.find("p")
    # link = item.find("a")["href"]
    link = item.find("a")
    
    # if(title!=None):
    #     title=item.find("h2").text.strip()
    #     # print(title)
    
    # if(description!=None):
    #     description = item.find("p").text.strip()
    
    # if(link!=None):
    #     # link = item.find("a")["href"]
    #     link = item.find("a")

    if(title!=None and description!=None and link!=None):
        title=item.find("h2").text.strip()
        description = item.find("p").text.strip()
        link = item.find("a")


    # Insert data into the database
    # sql = "INSERT INTO website_data (title, description, link) VALUES (%s, %s, %s)".format(title, description, link)

    # title='asd'
    # description='br'
    # link='et'


    sql = "INSERT INTO website_data (title, description, link) VALUES ('{}', '{}', '{}')".format(title, description, link)
    print(sql)
    # values = (title, description, link)
    cursor.execute(sql)

# Commit the changes and close the connection
print("xyz")
db.commit()
db.close()
print("123")