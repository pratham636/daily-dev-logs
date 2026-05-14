from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentance="This is a example of showing off stop word filtration."
stopwords=set(stopwords.words("english"))
# print(stopwords)
words=word_tokenize(example_sentance)
filtered_sentance=[]
# for w in words:
#     if w not in stopwords:
#         filtered_sentance.append(w)
filtered_sentance=[w for w in words if not w in stopwords]        
print(filtered_sentance)