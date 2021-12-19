import requests
from bs4 import BeautifulSoup as bs
import csv 

url="https://www.smartwatchspex.com/matrix-powerwatch-2-luxe/"
response=requests.get(url)
soup=bs(response.text,"html.parser")
#title scrape
title=soup.find("h1", {"class":"aps-main-title"}).text
print(title)
#table Left data scrape
table_left=[]

for h3 in soup.find_all("strong",{"class":"aps-term"}):
    table_left.extend(h3)
    #table_left.pop(0)
    #table_left.extend(h3)
    #print(h3)
#table Left data scrape
table_right=[]
for h4 in soup.find_all("span",{"class":"aps-1co"}):
    table_right.extend(h4)
    #table_right.pop(0)
    #table_right.extend(h4)

#print(table_right,table_left)
#two list merge with a dictionary
merge_data=dict(zip(table_left,table_right))
del merge_data['Buy']
#print(merge_data)


with open("kazikalko14.csv", "a+", newline="",encoding=("utf8")) as f:
	writer = csv.writer(f)
	writer.writerow(merge_data)
	#writer.writerow(table_right)