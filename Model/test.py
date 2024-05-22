from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import re

# Load the pre-trained model and tokenizer
model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Initialize the NER pipeline
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

# Input text
text = """
Dr. John Smith is a senior researcher in Artificial Intelligence at MIT. 
He holds a PhD in Computer Science from Stanford University. 
Previously, he worked at Google in Mountain View, California.
"""

# Perform NER
ner_results = nlp(text)

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

# Extract qualifications and locations
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

# Merge word pieces for qualifications and locations
qualifications = merge_word_pieces(qualifications)
locations = merge_word_pieces(locations)

# Use regex to find specific qualifications and subjects in text
degree_pattern = r'\b(?:' + '|'.join(degree_keywords) + r')\b'
subject_pattern = r'\b(?:' + '|'.join(subject_keywords) + r')\b'
additional_qualifications = re.findall(degree_pattern, text, re.IGNORECASE)
additional_subjects = re.findall(subject_pattern, text, re.IGNORECASE)

qualifications.extend(additional_qualifications)
qualifications.extend(additional_subjects)

# Remove duplicates and format
qualifications = list(set([q.title() for q in qualifications]))
locations = list(set([loc.title() for loc in locations]))

print("Qualifications:", ", ".join(qualifications))
print("Locations:", ", ".join(locations))
