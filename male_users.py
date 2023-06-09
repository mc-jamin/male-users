#Installing the requests module using pip
#Then importing the requets module

import requests

count=0
url="https://randomuser.me/api"
users=[]

if len(users)<100:
    res= requests.get(url).json()
    gender = res["results"][0]["gender"]
    if gender =="male":
        users.append(res)
    count = count + 1
    url = f"https://randomuser.me/api/?page={count}"
for male in users:
    print (male)
