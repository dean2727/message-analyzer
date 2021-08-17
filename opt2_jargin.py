from nltk.corpus import wordnet

# Get a dictionary of the jargin words (key = word, value = # of occurances)
def getJarginMap(corpus):
    jmap = {}
    for msg in corpus:
        words = msg.split(' ')
        for word in words:
            if word in jmap:
                jmap[word] += 1
            else:
                if word.isalpha() and not wordnet.synsets(word):
                    jmap[word] = 1
    # Sort by decreasing value
    jamp = {k: v for k, v in sorted(jmap.items(), key = lambda item: item[1])}
    return jmap

# Get a dictionary of a given word (key = word, value = # of occurances)
def getWordMap(corpus, word):
    wordMap = {}
    for msg in corpus:
        words = msg.split(' ')
        for word in words:
            if word in jmap:
                jmap[word] += 1
            else:
                if word.isalpha() and not wordnet.synsets(word):
                    jmap[word] = 1
    # Sort by decreasing value
    jamp = {k: v for k, v in sorted(jmap.items(), key = lambda item: item[1])}
    return jmap

# Jargin words. How many are there? And what are the most common ones?
def msgJarginAnalysis(cleanedText):
    print("Analyzing non-english words in the texts...")
    jwords = getJarginMap(cleanedText)
    jkeys = list(jwords.keys())
    print("Number of non-English/jargin words:", str(len(jkeys)))
    print("Most common non-English/jargin words:")
    print("1. \'" + jkeys[0] + "\'")
    print("2. \'" + jkeys[1] + "\'")
    print("3. \'" + jkeys[2] + "\'")
    print("4. \'" + jkeys[3] + "\'")
    print("5. \'" + jkeys[4] + "\'")
    print()