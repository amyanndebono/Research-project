
from bs4 import BeautifulSoup
from pip import main
import requests
from tkinter import * 
from tkinter import ttk 

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

root = Tk()
root.title('Covid regulations')
root.geometry("700x700")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH , expand=-1)

scroll_barY = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scroll_barX = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
scroll_barY.pack(side=RIGHT, fill=Y)
scroll_barX.pack(side=BOTTOM, fill=X)


my_canvas.configure(yscrollcommand=scroll_barY)
my_canvas.configure(xscrollcommand=scroll_barX)

my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="n")



def scrape(url ):
  result = requests.get(url)
  doc = BeautifulSoup(result.text, "html.parser")
  para = doc.find_all("p")
  info=[]
  for text in para: 
    info.append(text.get_text())
  
  combined_info ="\n".join(info)
  
  myLabel.config( text = combined_info)

def remove_text():
  myLabel.config(text="")

def show():
  if(clicked.get() == 'Malta' ):
    
    scrape(MaltaUrl)
  
  elif (clicked.get() == 'Italy'):
   
    #remove_text()
  # myLabel =Label(second_frame, text="").pack()
    scrape(italyURL)

  elif(clicked.get() == 'France'): 
     scrape(FranceURL)

  elif(clicked.get() == 'Austria'): 
   scrape(AustriaURL)

  elif(clicked.get() == 'Germany'): 
    scrape(germanyUrl)

  elif (clicked.get() == 'England'):
   scrape(UkURL)

  elif (clicked.get() == 'Spain'): 
    scrape(spainURL,myLabel)

  elif (clicked.get() == 'Portugal'):
   scrape(portugalURL)

  elif (clicked.get() == 'Switzerland'):
   scrape(switzerlandUrl)

  elif (clicked.get() == 'Poland'): 
    scrape(polandURL)
  else: 
    print("Invalid choice")

  
options = ["Malta", "Italy", "Germany", "France", "Austria", 
"England", "Spain", "Portugal", "Switzerland","Poland"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(second_frame, clicked, *options )

drop.pack()

showButton = Button(second_frame, text="Show Covid Regulations", command=show)
showButton.pack()
clearButton = Button(second_frame,text="Clear text to select a different country", command=remove_text)
clearButton.pack()

myLabel =Label(second_frame, text="")
myLabel.pack()

root.mainloop()

