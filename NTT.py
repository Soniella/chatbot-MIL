import spacy
from spacy.matcher import Matcher

# Load the small English model
nlp = spacy.load('en_core_web_sm')

# Process a text
doc = nlp("She ate the pizza\
she ate pizza\
Abracadabra danced a song")


for token in doc:
    if(token.pos_!="AUX" and token.pos_!="DET" and token.pos_!="ADP"):
        print(token.text)


"""
matcher=Matcher(nlp.vocab)
pattern1=[{"POS":"PRON"}, {"POS":"VERB"}, {"POS":"DET","OP":"?"},{'POS': 'NOUN'}]
pattern2=[{"POS":"PROPN"}, {"POS":"VERB"}, {"POS":"DET","OP":"?"},{'POS': 'NOUN'}]
matcher.add("Initial",None,pattern1, pattern2)
matcher.add("Initial2",None,pattern2)

matches=matcher(doc)

"""

"""# Iterate over the tokens
for x in matches:
    # Print the text and the predicted part-of-speech tag
    if((token.pos_=="NOUN" or token.pos_=="PRON") and token.dep_=="nsubj"):
    print(token.text)"""

"""
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    #test_span = nlp(matched_span)
    print(matched_span.text)
"""
