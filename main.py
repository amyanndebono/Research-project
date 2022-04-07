from bs4 import BeautifulSoup
import requests

def Malta(): 
  MaltaUrl = "https://www.gov.uk/foreign-travel-advice/malta/entry-requirements"
  result = requests.get(MaltaUrl)
  doc = BeautifulSoup(result.text, "html.parser")

  para = doc.find_all("p")

  for text in para: 
    print(text.get_text())


def italy(): 
  italyURL ='https://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=english&id=5412&area=nuovoCoronavirus&menu=vuoto'
  result = requests.get(italyURL)
  doc = BeautifulSoup(result.text, "html.parser")

  para = doc.find_all("p")

  for text in para:
    print(text.get_text())

print("Select 1 for Malta")
print("Select 2 for Italy")

choice =input()

if(choice == '1' ):
  Malta()

elif (choice == '2'):
  italy()

else: 
  print("Invalid choice")