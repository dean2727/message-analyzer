import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import re
import pandas as pd

stopWords = stopwords.words('english')
normalizer = WordNetLemmatizer()

# Read messages dataset (csv file) and return a Pandas dataframe for it
def readMessagesCsv(path):
    messageData = pd.read_csv(path)
    messageDataframe = pd.DataFrame(messageData)
    return messageDataframe

# Get the part-of-speech for a word
def getPartOfSpeech(word):
    probablePartOfSpeech = wordnet.synsets(word)
    posCounts = Counter()
    posCounts["n"] = len([item for item in probablePartOfSpeech if item.pos()=="n"])
    posCounts["v"] = len([item for item in probablePartOfSpeech if item.pos()=="v"])
    posCounts["a"] = len([item for item in probablePartOfSpeech if item.pos()=="a"])
    posCounts["r"] = len([item for item in probablePartOfSpeech if item.pos()=="r"])
    mostLikelyPartOfSpeech = posCounts.most_common(1)[0][0]
    return mostLikelyPartOfSpeech

# Remove noise from a message
def cleanMessage(message):
    temp = message.replace("?", "__question__")
    tempCleaned1 = re.sub(r'\'', '', temp)
    tempCleaned2 = re.sub(r'\W+', ' ', tempCleaned1)
    cleaned = tempCleaned2.replace("__question__", "?")
    return cleaned.lower()

# Reduce words of a message to their parts-of-speech
def lemmatizeMessage(message):
    tokenized = word_tokenize(message)
    lemmatized = [normalizer.lemmatize(token, getPartOfSpeech(token)) for token in tokenized]
    normalized = " ".join(lemmatized)
    return normalized

# Clean the corpus of text
def cleanCorpus(messageList):
    cleanList = list()
    for message in messageList:
        # Possible for some messages to be nan, in which case, ignore it
        if type(message) is str:
            cleanList.append(cleanMessage(message))
    return cleanList