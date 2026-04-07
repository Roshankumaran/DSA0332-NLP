from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "studies", "playing"]

for w in words:
    print(w, "->", stemmer.stem(w))
