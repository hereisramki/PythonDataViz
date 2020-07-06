import mysql.connector
import json
import requests
import ssl
import urllib.request, urllib.parse, urllib.error

cou = 0
count = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

db = mysql.connector.connect(
    host="localhost", # If not change it
    user="root",      # If not change it
    passwd="Your_Password",  #Updte Yours
    database ="covid", # Or Enter your database name
    auth_plugin="mysql_native_password" # If not needed you can comment it
    )
mycursor = db.cursor()

url = input("Enter json data site url :")
response = urllib.request.urlopen(url, context=ctx).read().decode()
js = json.loads(response)

print("Available data in this site: \t",end='')
print(len(js["raw_data"]))
h = len(js["raw_data"])
for i in range(h):
    age = js["raw_data"][i]["agebracket"]
    pn = js["raw_data"][i]["entryid"]
    gen = js["raw_data"][i]["gender"]
    city = js["raw_data"][i]["detectedcity"]
    state = js["raw_data"][i]["detectedstate"]
    date = js["raw_data"][i]["dateannounced"]
    try:
       
        mycursor.execute("INSERT INTO covid.`table1` (`PNo`, `Age`, `Gender`, `City`, `State`, `Date`) values (%s, %s, %s, %s, %s, %s)", (pn, age, gen, city, state, date))
        db.commit()
        count += 1

    except:
        
        # print("Already exists in Database")
        cou += 1
        
print("Total No. of Data that already exists is", cou)
print(f'{count} new entries added to database')
db.close()
    
