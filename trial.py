import spacy
nlp= spacy.load("en_core_web_sm")

doc = nlp(u"Tesla is looking at buying U.S.A. startup for $6 million")

for token in doc:
    print(token.text,token.pos_)
