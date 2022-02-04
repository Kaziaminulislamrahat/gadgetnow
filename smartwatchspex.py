import requests
from bs4 import BeautifulSoup as bs
import random
import pandas as pd


url="https://www.smartwatchspex.com/montblanc-summit-2/"
headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

response=requests.get(url,headers=headers)
soup=bs(response.text,"html.parser")
#title scrape
title=soup.find("h1", {"class":"aps-main-title"}).text
#table Left data scrape
table_left=[]

for h3 in soup.find_all("strong",{"class":"aps-term"}):
    table_left.extend(h3)
#table right data scrape
table_right=[]
for h4 in soup.find_all("span",{"class":"aps-1co"}):
    table_right.extend(h4)

#two list merge with a dictionary
merge_list=dict(zip(table_left,table_right))

#Delete buy key from Dictionary
del merge_list['Buy']

#Brand Name Key and Value Collect for Dictionary
brand=soup.find("span",attrs={"class":"aps-product-brand"}).text
brand_dict={}
brand_dict["Brand Name"]=brand.replace("Brand:","")

#joint two dictionary
merge_data={**brand_dict,**merge_list}

#Value Manupulation when Blank
for key, value in merge_data.items():
      if value == '-':
           merge_data[key] = ' information not available'

#Random Module use for more unique
start_1 = ["This", "The", "Do you know", "You know"]
start_2 = ["unique ", "exclusive ", "different ", "great "]


#Notification data validation
notification=[]
if merge_data.get("Activity Alert") =="Yes": notification.append("Activity Alert")
if merge_data.get("SMS") =="Yes": notification.append("SMS")
if merge_data.get("Email") =="Yes": notification.append("Email")
if merge_data.get("Incoming Call Alert") =="Yes": notification.append("Incoming Call Alert")
if merge_data.get("Calendar Reminder") =="Yes": notification.append("Calendar Reminder")
if merge_data.get("Weather Forecast") =="Yes": notification.append("Weather Forecast")

#List to string Convert for Notification
notification_string= ','.join(map(str, notification))

#Sensor data validation
sensor=[]
if merge_data.get("Accelerometer") =="Yes": sensor.append("Accelerometer")
if merge_data.get("Gyro") =="Yes": sensor.append("Gyro")
if merge_data.get("Heart Rate") =="Yes": sensor.append("Heart Rate")
if merge_data.get("Light") =="Yes": sensor.append("Light")
if merge_data.get("Compass/Magnetometer") =="Yes": sensor.append("Compass/Magnetometer")
if merge_data.get("Vibration/Haptics engine") =="Yes": sensor.append("Vibration/Haptics engine")

#List to string Convert for Sensor
sensor_string= ','.join(map(str, sensor))

#Sound data validation
sound=[]
if merge_data.get("Speaker") =="Yes": sound.append("Speaker")
if merge_data.get("Microphone") =="Yes": sound.append("Microphone")


#List to string Convert for sound
sound_string= ','.join(map(str, sound))


#Content Generation Part
first_sentence= random.choice(start_1) +" "+ merge_data.get("Device Name","None") +" is a " + random.choice(start_2) + "style and functionality that keeps you ahead of time with its "+random.choice(start_2)+"features."
general= merge_data.get("Device Name","none") + " release date was "+ merge_data.get("Release","none")+"." + merge_data.get("Ideal for (Gender)","everybody") + " can wear this "+ merge_data.get("Device Type","none")+"."
display= merge_data["Device Name"] + " has "+ merge_data.get("Screen Size","none")+ " "+ merge_data.get("Type","none")+ " display"+ ".It's screen resolution is "+ merge_data.get("Screen Resolution","None")+ " "+ "and pixel density"+ merge_data.get("Pixel Density","none")+ ".For screen protection, you will find here "+ merge_data.get("Screen Protection","none")+"."
body= merge_data.get("Device Name","none") + " "+ merge_data.get("Device Type","none")+ " is "+merge_data.get("Shape","none")+ " shape."+merge_data.get("brandname","none")+" gives "+merge_data.get("Case/Bezel","none")+ " and, it's case dimensions are "+ merge_data.get("Case Dimensions","none")+ "."+ merge_data.get("Strap Material","none")+ " strap and it's size is "+ merge_data.get("Strap/Band Size","none")+"."+merge_data.get("Colors","none")+ " variant available. "+merge_data.get("Device Name","none")+" weight is "+merge_data.get("Weight","none")+"."
platform= merge_data.get("brandname","none") + " used "+ merge_data.get("Operating System","none")+"." + merge_data.get("brandname","none")+ " used "+ merge_data.get("Chipset","none") +" chipset."+ merge_data.get("CPU","none") +" CPU and "+ merge_data.get("GPU","none")+" used for this "+merge_data.get("Device Type","none")+ "."
memory= merge_data.get("Device Name","None") + " has "+ merge_data.get("RAM","none")+" ram."+ merge_data.get("brandname","None")+ " provides "+ merge_data.get("Internal Memory","no internal memory.")+ " internal memory and "+ merge_data.get("SD Card Slot","no extra memory card you can use.")+" you can use extra memory card."
network_conectivity= merge_data.get("brandname","None") + " offer "+ merge_data.get("Sim","none")+" sim card."+ merge_data.get("Device Name","None")+ " has bluetooth "+ merge_data.get("Bluetooth","None")+", WiFi " +merge_data.get("WiFi","WiFi")+". "+ merge_data.get("NFC","None information found related to")+", NFC available in this gadget."+merge_data.get("USB","None information found related to ")+" USB and "+merge_data.get("Radio","None information found related to ")+" radio."
activity_tracker= merge_data.get("brandname","None") + " gives for tracking purpose features "+" distance,"+ merge_data.get("Distance","no")+ " heart rate,"+ merge_data.get("Heart Rate","no")+" step tracking, "+ merge_data.get("Steps","no")+" calories consumption " + merge_data.get("Calories Consumption","no ")+" and sleep tracker "+merge_data.get("Sleep","none")+ "."
control= "For controlling purpose the"+merge_data.get("brandname","none")+" "+ merge_data.get("Device Type","none")+" I am discussing now. "+ merge_data.get("Touch","none")+", you will get touch screen facility. A smartwatch screen customization is important here,you will get "+ merge_data.get("Watchface","no")+" watchface. "+merge_data.get("Voice Command"," Not available ")+" voice command you can use this "+merge_data.get("Device Type","Not")+"."+merge_data.get("Personal Assistant","No personal assistant ")+" is available for you."
notifications=notification_string+" "+merge_data.get("Device Name","None")+ " gives this notifications. "
sensors=merge_data.get("Device Name","none")+ " gives these "+merge_data.get("Device Type","none")+" sensors " +sensor_string+ "."
sounds="Sound purpose you will get "+ sound_string
battery=merge_data.get("Device Name", "None")+" has "+merge_data.get("Capacity", "None")+ " battery."+ "The battery life "+merge_data.get("Battery Life","none")+"."



#Content Print Part
#print(first_sentence,"\n",general,"\n",display,"\n",body,"\n",platform,"\n",memory,"\n",network_conectivity,"\n",control,"\n",notifications,"\n",sensors,"\n",sounds,"\n",battery)

#Pandas table creation
'''df = pd.DataFrame(table_right,table_left)
print(df)'''

#table insert trying
'''for x in table_right:
      for y in table_left:
          xyz=("<td>",x,"</td>","<td>", y,"</td>")
          joined_string = "".join(xyz)'''
          
#wordpress Post Section

import pybase64 #libary module change
#Authenticate
user = "SBauto"  # the user in which the auth. token is given
pythonapp = '9Bfc ZtB0 AEvK M6HR XySh jdCn'  # paste here your auth. token
url = 'https://tech4urhand.com/wp-json/wp/v2'  # the url of the wp access location
token = pybase64.standard_b64encode((user + ':' + pythonapp).encode('utf-8'))  # we have to encode the usr and pw
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}


wp_title = title+" "+"specification & Reviews"
slug = wp_title
status = 'publish'
contents = ("<!-- wp:paragraph --><p>"+first_sentence+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+general+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+display+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+body+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+platform+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+memory+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+network_conectivity+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+control+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+notifications+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+sensors+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+sounds+"</p><!-- /wp:paragraph -->"+
            "<!-- wp:paragraph --><p>"+battery+"</p><!-- /wp:paragraph -->"
                )


def wp_table(dictionary):
    s=['<!-- wp:table --><figure class="wp-block-table"><table><tbody>']
    for key, value in dictionary.items():
        s.append('<tr><td>'+key+'</td>')
        s.append('<td>'+value+'</td>')
        s.append('</tr>')
    s.append('</tbody></table></figure><!-- /wp:table -->')
    return ''.join(s)
test_bal=contents+(wp_table(merge_data))    


#print(contents)

post = {'title': wp_title,
           'slug': slug,
           'status': status,
           'content':test_bal,
           'categories':'1',
           'author': '1',
           'format': 'standard',

           }
send_post = requests.post(url + '/posts', headers=headers, json=post)
print(send_post)

