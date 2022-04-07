from bs4 import BeautifulSoup
import requests
import re 

#url = "https://www.gov.uk/foreign-travel-advice/malta/entry-requirements"

italyUrl = "https://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=english&id=5412&area=nuovoCoronavirus&menu=vuoto"

results =requests.get(italyUrl)
doc = BeautifulSoup(results.text, "html.parser")

rules = doc.find_all(text="rules")

print(rules)

#allPara = doc.find_all("p")
#for x in allPara:
   # print(x.prettify())
 #   allTraveller = x.find_all(text ="All travellers")
    
#parent = allTraveller[0].parent
#print(parent)

#print(allTraveller)

