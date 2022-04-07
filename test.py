from bs4 import BeautifulSoup
import requests
import webbrowser 
import time 
# with open('home.html','r')  as html_file: 
#     content = html_file.read()
    
#     soup = BeautifulSoup(content , 'html.parser')

#     To get a specific tag you can use the following 
#     tags = soup.h1

#     to change the value of a tag 
#     tags.string = "hello"

#     to find all tags 

#     tags = soup.find_all('h1')


#     to get the content inside of the tag use .string 
#     print(tags.findall('a'))



url = 'https://www.newegg.com/GIGABYTE-GeForce-RTX-3080-Ti-GV-N308TGAMING-OC-12GD/p/14-932-436'

result = requests.get(url)
doc = BeautifulSoup(result.text , "html.parser" )


#price = doc.find_all(text = "$")
#parent = price[0].parent
#strong = parent.find("strong")
#print(strong.string)

#html_content =f"<html> <head> </head> <body><p>The price for  Gaming GeForce RTX 3080 is{strong.string} </p></body> </html>"

#with open("index.html", "w") as html_file:
 #   html_file.write(html_content)
