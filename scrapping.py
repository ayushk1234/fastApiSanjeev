import requests
import html5lib
from bs4 import BeautifulSoup

url = "https://codewithharry.com";
result = requests.get(url);
htmlContent = result.content
# print(htmlContent)
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())

title = soup.title
# print(type(title))
paras = soup.findAll('p')
anchor = soup.findAll('a')
alllink = set()
for a in anchor :
    print(a.get('href'))

    # print(a)
para = soup.find('p')['class']
# print(para)

# print(soup.findAll('p',class_ ="mt-2"))
# print(soup.find('p').get_text())


