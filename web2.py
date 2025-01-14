import requests

url = 'https://randomuser.me/api/'

response = requests.get(url).json()
user = {}
user['name'] = response['results'][0]['name']['first']
user['surname'] = response['results'][0]['name']['last']
user['country'] = response['results'][0]['location']['country']
user['city'] = response['results'][0]['location']['city']
user['age'] = response['results'][0]['dob']['age']
for key,value in user.items():
    print(key,':',value)