import requests
import json

url = "https://maps.googleapis.com/maps/api/geocode/json"
address = raw_input("Enter address")
querystring = {"address":address}

headers = {
    'cache-control': "no-cache",
    'postman-token': "68c36178-0a23-05f9-d242-e33503239341"
    }

response = requests.request("POST", url, headers=headers, params=querystring)
data =  json.loads(response.text)
print "Latitude :" , data['results'][0]['geometry']['location']['lat']
print "Longitude :" , data['results'][0]['geometry']['location']['lng']
