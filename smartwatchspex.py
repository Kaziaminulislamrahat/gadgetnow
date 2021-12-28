import requests
from bs4 import BeautifulSoup as bs
import csv 
import random

url="https://www.smartwatchspex.com/amazfit-verge-lite/"
headers = {'user-agent': 'my-app/0.0.1'}
response=requests.get(url,headers=headers)
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
merge_list=dict(zip(table_left,table_right))
del merge_list['Buy']
brand=soup.find("span",attrs={"class":"aps-product-brand"}).text
brand_dict={}
brand_dict["brandname"]=brand.replace("Brand:","")
merge_data={**merge_list, **brand_dict}

for key, value in merge_data.items():
      if value == '-':
           merge_data[key] = ' information not available'

#dictionary data access single item
#test_dict=merge_data["Chipset"]
#print(merge_data)
#test gadgetnow style content create, here test first paragraph
#p1="This " + merge_data["Device Name"] +" is a unique combination of style and functionality that keeps you ahead of time with its unique features."
start_1 = ["This", "The", "Do you know", "You know"]
start_2 = ["unique ", "exclusive ", "different ", "great "]

m_first_sentence= random.choice(start_1) +" "+ merge_data["Device Name"] +" is a " + random.choice(start_2) + "style and functionality that keeps you ahead of time with its "+random.choice(start_2)+"features."
m_general= merge_data["Device Name"] + " release date was "+ merge_data["Release"]+"." + merge_data["Ideal for (Gender)"] + " can wear this "+ merge_data["Device Type"]+"."
m_display= merge_data["Device Name"] + " has "+ merge_data["Screen Size"]+ " "+ merge_data["Type"]+ " display"+ ".It's screen resolution is "+ merge_data["Screen Resolution"]+ " "+ "and pixel density"+ merge_data["Pixel Density"]+ ".For screen protection, you will find here "+ merge_data["Screen Protection"]+"."
m_body= merge_data["Device Name"] + " "+ merge_data["Device Type"]+ " is "+merge_data["Shape"]+ " shape."+merge_data["brandname"]+" gives "+merge_data["Case/Bezel"]+ " and, it's case dimensions are "+ merge_data["Case Dimensions"]+ "."+ merge_data["Strap Material"]+ " strap and it's size is "+ merge_data["Strap/Band Size"]+".Only "+merge_data["Colors"]+ " variant available. "+merge_data["Device Name"]+" weight is "+merge_data["Weight"]+"."
#m_release_date= merge_data["Device Name"] + " release date was "+ merge_data["Release"]
#m_release_date= merge_data["Device Name"] + " release date was "+ merge_data["Release"]


print(m_first_sentence,m_general,m_display,m_body)