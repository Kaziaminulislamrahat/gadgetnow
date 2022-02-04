from os import write
import requests
from bs4 import BeautifulSoup as bs

url="https://mddailyrecord.com/sitemap-pt-post-2022-01.xml"
response=requests.get(url)
#print(response)
soup=bs(response.text, "html.parser")
#print(soup)
all_url=soup.find_all("loc")
#print(all_url)
for loc in all_url:
    with open("dailyrecord.csv", "a+") as file:
        file. writelines(loc.text+ "\n")

print("Done Boss")
