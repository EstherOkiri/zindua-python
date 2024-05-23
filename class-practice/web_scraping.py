#requests allows you to send http requests over the internet.
#beautiful soup -allows us to parse html/xml content of a website to extract data
import requests
from bs4 import BeautifulSoup

url = "https://zinduaschool.com/blog"
url1 = "https://www.jumia.co.ke/bestselling-books/?q=books#catalog-listing"

response = requests.get(url)
print(response)

response1 = requests.get(url1)

soup = BeautifulSoup(response.content, 'html.parser')
soup1 = BeautifulSoup(response1.content, 'html.parser')

#soup comes with a number of methods
#headings = soup.find_all('h2')#get all h2 tags from the url
book_names = soup1.find_all("div",class_="info")

#headings = soup.find_all("div", class = "info")("h3", class_="name") try this with jumia site

#for heading in headings:
#    print (heading.text)#get all text

for book in book_names:
    print(book.text)