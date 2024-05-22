import requests

indeed_api_id = 'ed0e0159eb41df9e708902bd3a99a9995504df8eeddd9650563ca3542de87044'
indeed_api_key = 'IdAeP3H7m0T94STmrk7ogHI3mMq0LkZGFssN6UsqN4CNqipnFlCH0UcdwrqrVX8F'
user_ip = "89.114.187.78"
useragent = "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"

parameters = {
    'q': "python developer",
    'l': "Austin, TX",
    'sort': "date",
    'fromage': "5",
    'limit': "25",
    'filter': "1",
    'userip': user_ip,
    'useragent': useragent,
    'publisher': indeed_api_id  # Include your publisher data here
}


#params_ = {
#    'q' : "python",
#    'l' : "portugal",
#    'userip' : "89.114.187.78",
#    'useragent' : "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
#    'publisher' : indeed_api_key
#}

endpoint = "http://api.indeed.com/ads/apisearch"

r = requests.get(endpoint, params = parameters)

for l in r:
    print(l)

print(r)