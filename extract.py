import json

f=open("conv.json")
#stringg=f.readlines(f)
datastore = json.load(f)

'''
print(datastore[0]['dialog'])
[{'id': 0, 'sender': 'participant2', 'text': 'I love iphone! i just bought new iphone!', 'evaluation_score': None, 'sender_class': 'Bot'}, {'id': 1, 'sender': 'participant
1', 'text': "Thats good for you, i'm not very into new tech", 'evaluation_score': None, 'sender_class': 'Human'}, {'id': 2, 'sender': 'participant2', 'text': 'I am a colle
ge student and i am a college student', 'evaluation_score': None, 'sender_class': 'Bot'}, {'id': 3, 'sender': 'participant1', 'text': 'I am go to gym and live on donations
', 'evaluation_score': None, 'sender_class': 'Human'}, {'id': 4, 'sender': 'participant2', 'text': 'I am a vegan and i am in the midwest', 'evaluation_score': None, 'sende
r_class': 'Bot'}, {'id': 5, 'sender': 'participant1', 'text': 'So vegan... i have dogs maybe i should told then that they may eat cheap salads insted of meat', 'evaluation
_score': None, 'sender_class': 'Human'}, {'id': 6, 'sender': 'participant2', 'text': 'I would not mind having them in the office that would be hard for me', 'evaluation_sc
ore': None, 'sender_class': 'Bot'}, {'id': 7, 'sender': 'participant1', 'text': 'Dogs or vegan in office?', 'evaluation_score': None, 'sender_class': 'Human'}, {'id': 8, '
sender': 'participant2', 'text': 'I am a vegetarian so i am vegan', 'evaluation_score': None, 'sender_class': 'Bot'}, {'id': 9, 'sender': 'participant1', 'text': 'Strange
answer', 'evaluation_score': None, 'sender_class': 'Human'}, {'id': 10, 'sender': 'participant2', 'text': 'I guess i just do not know what to ps4 experience with.', 'evalu
ation_score': None, 'sender_class': 'Bot'}]

'''

fhuman= open("humanconv.txt","a",encoding="utf-8", errors="ignore")
fbot=open("botconv.txt","a", encoding="utf-8", errors="ignore")
#outer=datastore[0]['dialog']
for j in datastore:
    outer=j['dialog']
    for i in outer:
        if(i['sender_class']=="Bot"):
            fbot.write(i["text"])
            fbot.write("\n")
        elif(i['sender_class']=="Human"):
            fhuman.write(i["text"])
            fhuman.write("\n")


#print(d)
