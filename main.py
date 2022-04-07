from bs4 import BeautifulSoup
import requests

italyURL ='https://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=english&id=5412&area=nuovoCoronavirus&menu=vuoto'
result = requests.get(italyURL)
doc = BeautifulSoup(result.text, "html.parser")

#Attempting to access paragraph by first finding the word and the retrieving the parent. 
#rules =  doc.find_all(text="rules")

#Attempting to pass through the paragraph diectly 
#para = doc.find('p').find_next('The rules')
para = doc.find_all("p")

for text in para:
  print(text.get_text())

#print(para)


#Attempting to access p from div 

#allDiv = doc.find_all('p')
#for x in allDiv: 
  #allPara = x.find('p')#.find_next(text ='rules')
  #print(x)
 # rules = x.find_all(text = "rules")
  
#print(rules)
