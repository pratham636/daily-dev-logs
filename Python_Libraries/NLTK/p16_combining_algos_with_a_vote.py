import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers=classifiers
    def classify(self, features):
        votes=[]
        for c in self._classifiers:
            v=c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence(self,features):
        votes=[]
        for c in self._classifiers:
            v=c.classify(features)
            votes.append(v)
        choice_votes=votes.count(mode(votes))
        conf=choice_votes/len(votes)
        return conf

# documents=[(list(movie_reviews.words(fileid)),category) 
#            for category in movie_reviews.categories() 
#            for fileid in movie_reviews.fileids(category)]
# nltk.download('movie_reviews')
documents=[]
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)),category))

random.shuffle(documents)
# print(documents[1])
all_words=[0]
for w in movie_reviews.words():
    all_words.append(w.lower())
    
    
all_words=nltk.FreqDist(all_words)
words_features=[str(w) for w in list(all_words.keys())[:3000]]
def find_feature(document):
    words=set(document)
    features={}
    for w in words_features:
        features[w]=(w in words)
    return features
# print((find_feature(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets=[(find_feature(rev),category)for (rev,category) in documents]


training_set=featuresets[:1900]
testing_set=featuresets[1900:]

classifier=nltk.NaiveBayesClassifier.train(training_set)

classifier_f=open("naivebayes.pickle","rb")
classifier=pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes Algo accuracy:",(nltk.classify.accuracy(classifier,testing_set))*100)
classifier.show_most_informative_features(15)

MNB_classifier=SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB classifier accuracy:",(nltk.classify.accuracy(MNB_classifier,testing_set))*100)

# GaussianNB,BernoulliNB
# Gaussian_classifier=SklearnClassifier(GaussianNB())
# Gaussian_classifier.train(training_set)
# print("Gaussian classifier accuracy:",(nltk.classify.accuracy(Gaussian_classifier,testing_set))*100)

Bernoulli_classifier=SklearnClassifier(BernoulliNB())
Bernoulli_classifier.train(training_set)
print("Bernoulli classifier accuracy:",(nltk.classify.accuracy(Bernoulli_classifier,testing_set))*100)


# save_classifier=open("naivebayes.pickle","wb")
# pickle.dump(classifier,save_classifier)
# save_classifier.close()

# LogisticRegression, SGDClassifier
# SVC,LinearSVC,NuSVC

LogisticRegression_classifier=SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression classifier accuracy:",(nltk.classify.accuracy(LogisticRegression_classifier,testing_set))*100)

SGDClassifier_classifier=SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier classifier accuracy:",(nltk.classify.accuracy(SGDClassifier_classifier,testing_set))*100)

SVC_classifier=SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC classifier accuracy:",(nltk.classify.accuracy(SVC_classifier,testing_set))*100)

LinearSVC_classifier=SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC classifier accuracy:",(nltk.classify.accuracy(LinearSVC_classifier,testing_set))*100)

NuSVC_classifier=SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC classifier accuracy:",(nltk.classify.accuracy(NuSVC_classifier,testing_set))*100)

voted_classifier=VoteClassifier(classifier,MNB_classifier,Bernoulli_classifier,LogisticRegression_classifier,SGDClassifier_classifier,SVC_classifier,LinearSVC_classifier,NuSVC_classifier)
print("voted classifier accuracy:",(nltk.classify.accuracy(voted_classifier,testing_set))*100)

print("Classification",voted_classifier.classify(testing_set[0][0]),"Confidence %",voted_classifier.confidence(testing_set[0][0]))
