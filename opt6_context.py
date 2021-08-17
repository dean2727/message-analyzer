# Words used in most similar contexts to a word
def showSimilarContextWords(cleanedText, w2vModel, n):
    while True:
        word = input("Enter word, or hit \'enter\' to quit >>> ")
        if word == '':
            break
        if not w2vModel.wv.key_to_index[word]:
            print("Unable to get information for this word! Sorry about that.")
        else:
            mostCommon = w2vModel.wv.most_similar(word.lower(), topn=n)
            print("Here are the top", n, "words associated with \'", word + "\':")
            for i in range(n):
                print(str(i + 1) + ". \'" + mostCommon[i][0] + "\' " + 
                "(cosine similarity of about " + str(round(mostCommon[i][1], 2)) + ")")
    print()