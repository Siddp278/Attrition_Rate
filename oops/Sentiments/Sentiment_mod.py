#File: sentiment_mod.py

import os
import random
import pickle
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize



class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, r'Pickle\Doc.pickle')

documents_f = open(filename, "rb")
documents = pickle.load(documents_f)
documents_f.close()



filename = os.path.join(dirname, r'Pickle\word_features5k.pickle')
word_features5k_f = open(filename, "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


filename = os.path.join(dirname, r"Pickle\features_set.pickle")
feature_f = open(filename, "rb")
featuresets = pickle.load(feature_f)
feature_f.close()

random.shuffle(featuresets)
print(len(featuresets))

testing_set = featuresets[10000:]
training_set = featuresets[:10000]


filename = os.path.join(dirname, r"Pickle\originalnaivebayes5k.pickle")
open_file = open(filename, "rb")
classifier = pickle.load(open_file)
open_file.close()

filename = os.path.join(dirname, r"Pickle\BernoulliNB_classifier5k.pickle")
open_file = open(filename, "rb")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()

filename = os.path.join(dirname, r"Pickle\LogisticRegression_classifier5k.pickle")
open_file = open(filename, "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()

filename = os.path.join(dirname, r"Pickle\LinearSVC_classifier5k.pickle")
open_file = open(filename, "rb")
LinearSVC_classifier = pickle.load(open_file)
open_file.close()

filename = os.path.join(dirname, r"Pickle\SGDC_classifier5k.pickle")
open_file = open(filename, "rb")
SGDC_classifier = pickle.load(open_file)
open_file.close()




voted_classifier = VoteClassifier(
                                  classifier,
                                  LinearSVC_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                   SGDC_classifier)




def sentiment_check(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)