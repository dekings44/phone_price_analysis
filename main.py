#importing the libraries needed 
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


#Declaring the headers 
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

url = 'https://www.konga.com/search?search=phones&page=1'

res = requests.get(url, headers = headers)

print(res)

soup = BeautifulSoup(res.text, 'html.parser')


phone_desc = soup.find_all('div', {'class': 'af885_1iPzH'})
print(phone_desc)
disc = [name.text for name in phone_desc]
print(disc)