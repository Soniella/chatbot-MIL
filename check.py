import spacy
from spacy.matcher import Matcher

# Load the small English model
nlp = spacy.load('en_core_web_sm')

# Process a text\

f=open("qanda.txt","r")
print(f.read())
doc = nlp(f.read())
