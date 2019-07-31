import numpy as np
import tensorflow as tf
from sklearn.utils import shuffle
import re
import time
import collections
import os
import sqlite3
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
import spacy
from spacy.matcher import Matcher

saver = tf.train.Saver()

saver.restore(sess, "testmodel.ckpt")


#FOLLOW-UP PART


print("follow-up...")



#Steps to repeat

#Step 1: Connect fresh to database again. Necessary since closed. Also better to close and open (since cursor might give problems like pointers? :P)
conn=sqlite3.connect('chatbot.db')
cur = conn.cursor()
cur.execute("SELECT * from NER")
rows = cur.fetchall()



#Step 2: This time re-define question test which is a list of strings. This time with the ones stored. Unlike last time where we took from user.
question_test=[]
for row in rows:
    #print("Response: ", row[0])
    questionNew=list(row)
    question_test.append(' '.join(questionNew))
    #question_test.append(row[0]


#Step 3: Change only those variables which depend on X_test
X_test = str_idx(question_test, dictionary_from)
batch_x, seq_x = pad_sentence_batch(X_test[:batch_size], PAD)


#Step 4: Pass new batch_x (which depends on question_test) to the model (that has already been built the first time) using sess.run()
predicted = sess.run(model.predicting_ids, feed_dict={model.X:batch_x,model.X_seq_len:seq_x})


#Step 5: Print results
for i in range(len(batch_x)):
    print('QUESTION:',' '.join([rev_dictionary_from[n] for n in batch_x[i] if n not in [0,1,2,3]]))
    print('PREDICTED ANSWER:',' '.join([rev_dictionary_to[n] for n in predicted[i] if n not in[0,1,2,3]]),'\n')


conn.close()
