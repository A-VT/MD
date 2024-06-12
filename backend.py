import re
import requests
import json
from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_together import ChatTogether
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# environment variables
import os 
from dotenv import load_dotenv

import fitz  # PyMuPDF

# Load the pre-trained model and tokenizer
load_dotenv()
API_KEY = os.getenv("API_KEY")

llm = ChatTogether(
    together_api_key=API_KEY,
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
)

class Person(BaseModel):
    """The skill from a candidate's CV."""

    # ^ Doc-string for the entity Person.
    # This doc-string is sent to the LLM as the description of the schema Person,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    name: Optional[str] = Field(default=None, description="The name of the person")
    skills: Optional[list] = Field(default=None, description="The hard/soft skills acquired by the candidate")
    experiences: Optional[list] = Field(default=None, description="level of experience in a particular field")
    locations: Optional[list] = Field(default=None, description="The cities or contry where the person has worked or studied")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "If you do not know the value of an attribute asked to extract, "
            "Never return the examples placeholder, try to use it as a reference only."
            "return null for the attribute's value.",
        ),
        # Please see the how-to about improving performance with
        # reference examples.
        # MessagesPlaceholder('examples'),
        ("human", "{text}"),
    ]
)

runnable = prompt | llm.with_structured_output(schema=Person)

def clean_text(text):

    # Remove URLs (both with and without www)
    text = re.sub(r'https?://\S+\.\w+|http?\S+\.\w+|www\.\S+\.\w+|\S+\.\w+/\S+', '', text)
    
    text = re.sub(r'[+\-\[\]]', '', text)

    # Remove emails
    text = re.sub(r'\S+@\S+', '', text)
 
    # Remove dates in various formats (e.g., MM/DD/YYYY, YYYY-MM-DD)
    text = re.sub(r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b', '', text)
    text = re.sub(r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    text = re.sub(r'(?m)^[^\s\r]{0,2}.$', '', text)

    # Remove consecutive newline characters
    text = re.sub(r'\n{2,}', ' ', text)
    
    return text

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

def getMeSomeJuicyAnswers(text):
    results = []
    cv_text = clean_text(text)
    result = runnable.invoke({"text": cv_text})
    print("Skills:", result.skills)
    print("Experiences:", result.experiences)
    print("Locations:", result.locations)
    #for location in result.locations:
    #    job_listings = search_job_listings(result.skills, location)
    #    print(f"Job listings in {location}:")
    #    
    #    results = job_listings['jobs']
        

        #for job in job_listings['jobs']:
        #    results.append([job['title'], job['company'], job['salary'], job['locations']])
        #    #print(job['title'], "-", job['company'], "-", job['salary'], "-", job['locations'])
    
    #for debug purposes - delete later
    with open("./resultsDump.juson", "w") as json_file:
        json.dump(results, json_file)

    return results



# Example text
text = """
Dr. John Smith is a senior researcher in Artificial Intelligence at MIT. 
He holds a PhD in Computer Science from Stanford University. 
Previously, he worked at Google in California.
"""
getMeSomeJuicyAnswers(text)