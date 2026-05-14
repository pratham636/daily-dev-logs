from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
example_words=["python","pythoner","pythoning","pythonly"]
for w in example_words:
    print(ps.stem(w))
new_text="It is very important to be pythonly while you are pythoning with python. All pythoners has pythones."
words=word_tokenize(new_text)
for w2 in words:
    print(ps.stem(w2))