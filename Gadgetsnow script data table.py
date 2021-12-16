from bs4 import BeautifulSoup
import requests
import csv

url="https://www.gadgetsnow.com/smartwatch/Noise-ColorFit-Pro-3-155-Inch-LCD-Display-White-Watch"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")
list=[]
for th in soup.find_all("th"):
    #print(tr.get_text())
     
   list.extend(th)
list_td=[]

for td in soup.find_all("td"):
     
   list_td.extend(td)

with open("kazikalko123.csv", "a+", newline="",encoding=("utf8")) as f:
	writer = csv.writer(f)
	writer.writerow(list)
	writer.writerow(list_td)

    






