from indeed import IndeedClient
#import MySQL Python Library
import pymysql



clientIndeed = IndeedClient(publisher = ************3506)
parameters_Indeed = {'q' : "python developer",
              'l' : "Austin",
              'sort' : "date",
              'fromage' : "5",
              'limit' : "25",
              'filter' : "1",
              'userip' : "192.186.176.550:60409",
              'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
             }


#our main function
def get_offers(params):

    search_results = clientIndeed.search(**search_params)

    for elm in search_results['results']:
                
        offer = (elm['jobtitle'], 
                 elm['formattedLocation'], 
                 elm['snippet'], 
                 elm['url'], 
                 elm['indeedApply'], 
                 elm['jobkey'], 
                 elm['date'])


get_offers(parameters_Indeed)