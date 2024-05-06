import requests
from careerjet_api_client import CareerjetAPIClient


cj  =  CareerjetAPIClient("en_GB");

indeed_api_key = 'd1qQ1qZJb4hjSYcumJR3MDbcrTEqErPO5aPLqwZjqv6Rgg5efiQeTCRxspdQk8yC'
indeed_keywords = 'data scientist'
indeed_location = 'portugal'

indeed_url = f'https://public.api.careerjet.net/search?apikey={api_key}&keywords={query}&location={location}&sort=salary'

#response = requests.get(indeed_url)
#indeed_data = response.json()
#print(indeed_data)

careerjet_query = {
                        'location'    : indeed_location,
                        'keywords'    : indeed_keywords,
                        'affid'       : '0db138870e02f87744edfc80882408a8',
                        'user_ip'     : '0.0.0.0',
                        'url'         : f'http://www.example.com/jobsearch?q={indeed_keywords}&l={indeed_location}',
                        'user_agent'  : 'Mozilla/125.0.3 Gecko/20100101 Firefox/31.0'
                    }
try:
    careerjet_result_json = cj.search(careerjet_query);
except Exception as e:
    print(e)

print(careerjet_result_json)

