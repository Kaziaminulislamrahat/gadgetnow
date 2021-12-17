import requests
from bs4 import BeautifulSoup as bs 

url="https://www.smartwatchspex.com/matrix-powerwatch-2-luxe/"
response=requests.get(url)
soup=bs(response.text,"lxml")
#title scrape
title=soup.find("h1", {"class":"aps-main-title"}).text
print(title)
#table data scrape
table_spec=[]
table_h3=soup.find_all("h3", {"class":"aps-group-title"})
test_table=table_spec.extend(table_h3)
table_raw=table_spec.remove('<h3 class="aps-group-title">')
table_final=table_spec.extend(table_raw) 
for h3 in table_spec:
    print(h3)