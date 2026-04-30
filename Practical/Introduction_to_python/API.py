import requests
url='https://catfact.ninja/fact'
#Get information from the url and store in reponse variable
response=requests.get(url)
print(response.json())
print(response.json()["fact"])
print(response)

