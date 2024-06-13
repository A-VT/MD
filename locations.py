import re

COUNTRIES = [
    "United States", "Canada", "Mexico", "Brazil", "Argentina",
    "United Kingdom", "France", "Germany", "Italy", "Spain",
    "China", "Japan", "India", "Russia", "Australia",
    "South Africa", "Egypt", "Nigeria", "Kenya", "Saudi Arabia",
    "South Korea", "Indonesia", "Vietnam", "Philippines", "Turkey",
    "Pakistan", "Bangladesh", "Iran", "Thailand", "Malaysia"
]

CONTINENTS = [
    "Africa", "Antarctica", "Asia", "Europe", "North America",
    "Oceania", "South America"
]

CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa",
    "London", "Paris", "Berlin", "Madrid", "Rome",
    "Beijing", "Shanghai", "Tokyo", "Mumbai", "Delhi",
    "Sydney", "Melbourne", "Brisbane", "Perth", "Auckland"
]

DISTRICTS = [
    "Brooklyn", "Manhattan", "Queens", "Bronx", "Staten Island",
    "Central", "Western", "Eastern", "Southern", "Northern",
    "Downtown", "Midtown", "Uptown", "East Side", "West Side",
    "California"
]

def normalize_string(s):
    return re.sub(r'[^\w\s]', '', s).strip().lower()

def is_country_or_location(name):
    normalized_name = normalize_string(name)
    
    normalized_countries = [normalize_string(country) for country in COUNTRIES]
    normalized_continents = [normalize_string(continent) for continent in CONTINENTS]
    normalized_cities = [normalize_string(city) for city in CITIES]
    normalized_districts = [normalize_string(district) for district in DISTRICTS]
    
    if normalized_name in normalized_countries:
        return True
    elif normalized_name in normalized_continents:
        return True
    elif normalized_name in normalized_cities:
        return True
    elif normalized_name in normalized_districts:
        return True
    else:
        return False