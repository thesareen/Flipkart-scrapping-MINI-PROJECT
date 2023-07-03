import requests
from bs4 import BeautifulSoup
url="https://www.flipkart.com/search?q=mobile+phone+5g"
data=requests.get(url)
convert=data.content
soup=BeautifulSoup(data.content,'html.parse')
print(soup) #extracted required data
text=soup.get_text()
print(text)

