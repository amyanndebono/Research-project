from turtle import clear
from unittest import result
from bs4 import BeautifulSoup
import requests


germanyUrl = 'https://www.auswaertiges-amt.de/en/visa-service/EinreiseUndAufenthalt'
MaltaUrl = "https://www.gov.uk/foreign-travel-advice/malta/entry-requirements"
italyURL ='https://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=english&id=5412&area=nuovoCoronavirus&menu=vuoto'
FranceURL ='https://www.interieur.gouv.fr/covid-19-international-travel'
AustriaURL = 'https://www.gov.uk/foreign-travel-advice/austria/entry-requirements'
UkURL = 'https://www.gov.uk/guidance/travel-to-england-from-another-country-during-coronavirus-covid-19'
spainURL = 'https://www.dfa.ie/travel/travel-advice/a-z-list-of-countries/spain/'
portugalURL = 'https://www.visitportugal.com/en/content/covid-19-measures-implemented-portugal'
switzerlandUrl = 'https://www.swissinfo.ch/eng/covid-19_coronavirus--the-situation-in-switzerland/45592192'
polandURL = 'https://www.swissinfo.ch/eng/covid-19_coronavirus--the-situation-in-switzerland/45592192'

def scrape(url):
  result = requests.get(url)
  doc = BeautifulSoup(result.text, "html.parser")
  para = doc.find_all("p")

  for text in para: 
    print(text.get_text())

print("Select 1 for Malta")
print("Select 2 for Italy")
print("Select 3 for France")
print("Select 4 for Austria")
print("Select 5 for Germany")
print("Select 6 for UK")
print("7- spain")
print ("8-portugal")
print ("9-switzerland ")
print("10-poland")

choice =input()

if(choice == '1' ):
  scrape(MaltaUrl)

elif (choice == '2'):
   scrape(italyURL)

elif(choice == '3'): 
  scrape(FranceURL)

elif(choice == '4'): 
   scrape(AustriaURL)

elif(choice == '5'): 
  scrape(germanyUrl)

elif (choice == '6'):
  scrape(UkURL)

elif (choice == '7'): 
  scrape(spainURL)

elif (choice == '8'):
  scrape(portugalURL)

elif (choice == '9'):
  scrape(switzerlandUrl)

elif (choice == '10'): 
  scrape(polandURL)
else: 
 print("Invalid choice")