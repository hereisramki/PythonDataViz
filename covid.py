# FOR DB_SQlite USERS
import json
import requests
import pprint
import ssl
import urllib.request, urllib.parse, urllib.error
import sqlite3


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cum = sqlite3.connect('covid_data_new.sqlite')
cur = cum.cursor()

url = input("Enter data site url :")
response = urllib.request.urlopen(url, context=ctx).read().decode()
js = json.loads(response)
print(len(js))
print(len(js["raw_data"]))
h = len(js["raw_data"])
for i in range(h):
    j = js["raw_data"][i]["agebracket"]
    pn = js["raw_data"][i]["patientnumber"]
    kk = js["raw_data"][i]["detectedstate"]
    tp = js["raw_data"][i]["typeoftransmission"]
    try:
        cur.execute('''SELECT ID FROM Data1 WHERE PNo=?''',(pn,))
        da = cur.fetchone()[0]
        print("Found in database at ID no. ",da)
        continue
    except:
        cur.execute('''INSERT OR IGNORE INTO Data1 (PNo, State, Age, Type_of_transmission) VALUES(?, ?, ?, ?)''',(pn, kk, j, tp,) )
    cum.commit()
#https://api.covid19india.org/raw_data4.json
