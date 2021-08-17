from nltk.corpus import wordnet
import gensim
from gensim.models import Word2Vec
import re

def filterOutNonEnglish(corpus):
    filteredCorpus = []
    for msg in corpus:
        words = msg.split(' ')
        foundBad = False
        for word in words:
            if not wordnet.synsets(word):
                foundBad = True
                break
        if not foundBad:
            filteredCorpus.append(msg)            
    return filteredCorpus

# Tokenize each message
# word2vec model needs a list of lists of words, not a list of strings (messages)
def tokenizeMsgs(listOfMsgs):
    newList = []
    for msg in listOfMsgs:
        listOfTokens = [tok for tok in msg.split(' ')]
        newList.append(listOfTokens)
    return newList

def trainWord2VecModel(corpus):
    tokenized = tokenizeMsgs(corpus)
    embeddings = Word2Vec(tokenized, vector_size=1000, window=20, min_count=1, workers=2, sg=1)
    return embeddings