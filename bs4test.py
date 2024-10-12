from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

page = requests.get(url, headers = headers)

# print(page.text)

soap = BeautifulSoup(page.text, 'html.parser')

# print(type(soap))
# print(soap.title)
# print(soap.title.string.strip())
# print(soap.find_all('a'))

# print(soap.find(class_="product_pod").find('h3').string)

# print(soap.find_all(class_="product_pod"))


# ENCONTRA OS TÍTULOS
#for title in soap.find_all(class_="product_pod"):
#    print(title.find("h3").string)


# ENCONTRA OS TÍTULOS E PREÇOS
for title in soap.find_all(class_="product_pod"):
    print("Título: " + title.find("h3").string +"\nPreço: "+ title.find(class_="price_color").string.replace("Â£",""))