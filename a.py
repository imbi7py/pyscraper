import requests
from bs4 import BeautifulSoup
import sys

result = requests.get("https://www.udemy.com/courses/search/?src=ukw&q=python")
boom = result.content
soup = BeautifulSoup(boom,'lxml')
links = soup.findAll("div")
# for link in links:
#     print(link)
#     print(link.attrs['href'])
print(links)
