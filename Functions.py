import nltk
from nltk.probability import ConditionalFreqDist
from nltk.book import *

#Generates sentences of length n with the starting word w and a corpus c 
#uses the most likely bigrams and is completely deterministic
def generateSentences(n, w, c):
	cfd = nltk.ConditionalFreqDist([(w1, w2) for (w1, w2) in nltk.bigrams(c.words())])
	while n > 0:
		n = n - 1
		

print(generateSentences(10, 'hello', text1))