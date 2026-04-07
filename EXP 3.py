from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

text = "Cats are running"
words = word_tokenize(text)

lemmatizer = WordNetLemmatizer()

for w in words:
    print(w, "->", lemmatizer.lemmatize(w))
