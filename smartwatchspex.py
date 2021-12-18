import requests
from bs4 import BeautifulSoup as bs 

url="https://www.smartwatchspex.com/matrix-powerwatch-2-luxe/"
response=requests.get(url)
soup=bs(response.text,"html.parser")
#title scrape
title=soup.find("h1", {"class":"aps-main-title"}).text
print(title)
#table Left data scrape
table_left=[]
table_h3_a=soup.find_all("strong", {"class":"aps-term"})
test_table_a=table_left.extend(table_h3_a)
#print(table_left)
#for h3 in table_left:
    #print(h3)
#table Left data scrape
table_right=[]
table_h3_b=soup.find_all("span", {"class":"aps-1co"})
test_table_b=table_right.extend(table_h3_b)
#print(table_right)
#two list merge with a dictionary
merge_data=dict(zip(table_left, table_right))
print(merge_data)




