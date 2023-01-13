import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize empty lists to store the data
names = []
prices = []

# The base URL for the website
base_url = "https://www.jumia.com.ng/catalog/?q=android+phones&page="

# A loop to scrape all pages
for page in range(1, 20):
    # Construct the full URL
    url = base_url + str(page)

    # Use requests to get the HTML content of the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the phone names and prices using BeautifulSoup
    for item in soup.find_all("div", {"class": "info"}):
        names.append(item.find("h3", {"class": "name"}).text)
        prices.append(item.find("div", {"class": "prc"}).text)

# Create a dataframe from the extracted data
data = {"Name": names, "Price": prices}
df = pd.DataFrame(data)

# Show the first 5 rows of the dataframe
print(df.head())
