from bs4 import BeautifulSoup
import requests

url = "https://www.gov.uk/foreign-travel-advice/malta/entry-requirements"

results =requests.get(url)
doc = BeautifulSoup(results.text, "html.parser")

parent =doc.find_all("p")

print(parent)