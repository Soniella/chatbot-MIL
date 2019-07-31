import nltk
#nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

i=0
while(i<10):
    inp= input("Say what you have to say :) :  ")

    if(sid.polarity_scores(inp)["compound"])>=0:
        print(sid.polarity_scores(inp)["compound"])
        print("Awesome! :) ")
    else:
        print(sid.polarity_scores(inp)["compound"])
        print("Aye! Speak your mind but mind your speech!!! :P ")

    print()
    i+=1
