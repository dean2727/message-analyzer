import re

def getNumQuestions(corpus, numMsgs):
    print("Calculating number of text messages with questions...")

    questions = 0
    pattern = re.compile(r"\?")
    for msg in corpus:
        if pattern.search(msg):
            questions += 1

    print(str(questions) + "/" + str(numMsgs) + " messages contain questions (" + str(round(questions/numMsgs*100)) + "%)")
    print()