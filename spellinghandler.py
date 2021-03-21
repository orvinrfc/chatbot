from spellchecker import SpellChecker

# Create a dictionary of some mispelled words as key, and correct word as value
# This is because some words are not flagged as mispelled by pyspellchecker 
# for example "wnat" is not fixed to "want"
dictionary = {}

def createDictionary(file):
    f = open(file)
    for line in f:
        (key,val) = line.split()
        dictionary[key] = val

createDictionary("words.txt")

# Instantiate a SpellChecker object
spell = SpellChecker()

# Fix a word by first checking in the dictionary, if it doesn't exist use pyspellchecker
def fixWord(word):
    for key in dictionary:
        if word == key:
            return dictionary[key]
        else:
            return spell.correction(word)

# Fix a complete sentence
# sentence = sentence to be fixed
# entityArray = array of entities extracted from named-entity recognition
def fixSentence(sentence, entityArray):
    words = sentence.split() # Convert the sentence into array of words
    newsentence = ""

    for word in words:
        
        if word in entityArray:
            newsentence += word + " "
        else:
            wrongword = spell.unknown([word]) # assign the mispelled word to wrongword variable

            if wrongword != None: # if wrong word exists, fix the word
                word = fixWord(word)
            
            newsentence += word + " " 
            
    return newsentence

# Offer correction by IMDBot instead
def offerCorrection(sentence,entityArray):
    newsentence = fixSentence(sentence, entityArray)
    print("IMDBot: Do you mean " + newsentence + "?")


# --------------Testing------------ #

print(fixWord("egt"))
print(fixWord("wnat"))

entityArray = ["Zendaya","Spider-man"]
print(fixSentence("Whof plaked Zendaya inm Spider-man",entityArray))