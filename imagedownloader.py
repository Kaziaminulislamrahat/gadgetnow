import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.smartwatchspex.com/matrix-powerwatch-2-premium/") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('img'):
    print(item['src'])

