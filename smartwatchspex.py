import requests
from bs4 import BeautifulSoup as bs
import csv 
import random

url="https://www.smartwatchspex.com/xiaomi-mi-band-hrx-edition-specs/"
response=requests.get(url)
soup=bs(response.text,"html.parser")
#title scrape
title=soup.find("h1", {"class":"aps-main-title"}).text
#print(title)
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
#dictionary data access single item
#test_dict=merge_data["Chipset"]
#print(test_dict)
#test gadgetnow style content create, here test first paragraph
#p1="This " + merge_data["Device Name"] +" is a unique combination of style and functionality that keeps you ahead of time with its unique features."
start_1 = ["This", "The", "Do you know", "You know"]
start_2 = ["unique ", "exclusive ", "different ", "great "]

m_p2= random.choice(start_1) +" "+ merge_data["Device Name"] +" is a " + random.choice(start_2) + "style and functionality that keeps you ahead of time with its "+random.choice(start_2)+"features."


#m_p3=


print(m_p2)




#export as a csv file
'''with open("kazikalko14.csv", "a+", newline="",encoding=("utf8")) as f:
	writer = csv.writer(f)
	writer.writerow(merge_data)
	#writer.writerow(table_right)'''