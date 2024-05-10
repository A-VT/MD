import requests

careerjet_key = '0db138870e02f87744edfc80882408a8'
userip = '89.114.187.78'
keywords = 'data scientist'
location = 'new york'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0'

url = f"http://public.api.careerjet.net/search?keywords={keywords}&location={location}&user_ip={userip}&user_agent={user_agent}&sort=salary"

response = requests.get(url)
data = response.json()

print(data)


#http://public.api.careerjet.net/search?apikey=0db138870e02f87744edfc80882408a8&keywords=data&location=portugal&sort=salary

