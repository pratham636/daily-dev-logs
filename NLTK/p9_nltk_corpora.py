import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import NLTKWordTokenizer
# print(nltk.__file__)
# print(nltk.__file__)
sample_text=gutenberg.raw("bibie-kjv.txt")
tok=sent_tokenize(sample_text)
print(tok[5:15])
