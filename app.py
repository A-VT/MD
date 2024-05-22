from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import re
import requests
import json

# Load the pre-trained model and tokenizer
model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Initialize the NER pipeline
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

# Function to merge word pieces
def merge_word_pieces(words):
    merged = []
    for word in words:
        if word.startswith('##'):
            if merged:
                merged[-1] += word[2:]
        else:
            merged.append(word)
    return merged

# Function to extract qualifications and locations from text
def extract_info(text):
    ner_results = nlp(text)
    qualifications = []
    locations = []
    buffer = []

    degree_keywords = ['PhD', 'Master', 'Bachelor', 'Degree', 'Doctorate']
    subject_keywords = ['Science', 'Engineering', 'Arts', 'Artificial Intelligence', 'Computer Science']

    for entity in ner_results:
        if entity['entity'] == 'B-LOC' or entity['entity'] == 'I-LOC':
            locations.append(entity['word'])
        elif entity['entity'] == 'B-MISC' or entity['entity'] == 'I-MISC':
            if any(keyword in entity['word'] for keyword in degree_keywords + subject_keywords):
                buffer.append(entity['word'])
            elif buffer:
                qualifications.extend(buffer)
                buffer = []
        else:
            if buffer:
                qualifications.extend(buffer)
                buffer = []

    qualifications = merge_word_pieces(qualifications)
    locations = merge_word_pieces(locations)

    degree_pattern = r'\b(?:' + '|'.join(degree_keywords) + r')\b'
    subject_pattern = r'\b(?:' + '|'.join(subject_keywords) + r')\b'
    additional_qualifications = re.findall(degree_pattern, text, re.IGNORECASE)
    additional_subjects = re.findall(subject_pattern, text, re.IGNORECASE)

    qualifications.extend(additional_qualifications)
    qualifications.extend(additional_subjects)

    qualifications = list(set([q.title() for q in qualifications]))
    locations = list(set([loc.title() for loc in locations]))

    return qualifications, locations

# Function to search for job listings based on qualifications and location
def search_job_listings(qualifications, location):
    careerjet_key = '0db138870e02f87744edfc80882408a8'
    userip = '89.114.187.78'  # Example IP
    keywords = ' '.join(qualifications)  # Use qualifications as keywords
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0'

    url = f"http://public.api.careerjet.net/search?keywords={keywords}&location={location}&user_ip={userip}&user_agent={user_agent}&sort=salary"

    response = requests.get(url)
    data = response.json()

    return data

# Example text
text = """
Dr. John Smith is a senior researcher in Artificial Intelligence at MIT. 
He holds a PhD in Computer Science from Stanford University. 
Previously, he worked at Google in California.
"""

# Extract qualifications and locations from text
qualifications, locations = extract_info(text)

# Search for job listings based on qualifications and location
for location in locations:
    job_listings = search_job_listings(qualifications, location)
    print(f"Job listings in {location}:")
    for job in job_listings['jobs']:
        print(job['title'], "-", job['company'], "-", job['salary'], "-", job['locations'])
    print()