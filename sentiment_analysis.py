from math import floor, ceil
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Given a training corpus (as a list of messages), return a fitted CountVectorizer and
# a trained MultinomialNB model
def trainBayesModel(corpus):
    countVectorizer = CountVectorizer()
    msgVectors = countVectorizer.fit_transform(corpus)
    
    # Creating our labels. Could have an odd number of training samples
    split = len(corpus) / 2
    msgLabels = []
    if len(corpus) % 2 == 0:
        msgLabels = split * [0] + split * [1]
    else:
        msgLabels = floor(split) * [0] + ceil(split) * [1]
    
    classifier = MultinomialNB()
    classifier.fit(msgVectors, msgLabels)
    return classifier, countVectorizer

# Given a message (as a string), a trained MultinomialNB, and a fitted CountVectorizer,
# predict the sentiment of the message
def testBayesModel(msg, model, countVectorizer):
    msgVector = countVectorizer.transform([msg])
    predictions = model.predict_proba(msgVector)
    return predictions
