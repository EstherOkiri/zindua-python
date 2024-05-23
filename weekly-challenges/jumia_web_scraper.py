import requests
from bs4 import BeautifulSoup
import re

url = "https://www.jumia.co.ke/mlp-top-deals/"

top_deals = requests.get(url)
print(top_deals)

soup = BeautifulSoup(top_deals.content,'html.parser')

product_info = soup.find_all("h3", class_="name")
print(product_info)

for product in product_info
