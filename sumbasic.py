import sys
import nltk
import operator
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import randint

class Summary:
    def __init__(self):
        self.content = []
        self.count = 0

    def make_summary(self):
        return ' '.join(self.content)

class SBU:
    def __init__(self, sentence):
        self.weight = 0.0
        self.sentence = sentence
        self.word_tokens = None
        self.clean_tokens = []

    def preprocess(self):
        wordnet_lemmatizer = WordNetLemmatizer()
        self.word_tokens = word_tokenize(self.sentence)

        stop_words = set(stopwords.words('english'))
        filtered = []
        for w in self.word_tokens:
            if w not in stop_words:
                lemm = wordnet_lemmatizer.lemmatize(w)
                self.clean_tokens.append(lemm.lower())

class Article:
    def __init__(self, article):
        self.data = article
        self.all_sbu = []
        self.clean_words = []

class Cluster:
    def __init__(self, version, corpus, raw_articles):
        if version not in ['orig', 'best-avg', 'simplified', 'leading']:
            raise ValueError('please enter valid input')
            exit()
        # data
        self.version = version
        self.corpus = corpus
        self.raw_articles = raw_articles
        self.all_articles = []
        self.summary = Summary()

        # summary utility variables
        self.word_counts = {}
        self.total = 0.0
        self.distribution = {}
        self.curr_sbu = None


    def process_articles(self):
        for article in self.raw_articles:
            self.all_articles.append(Article(article))

    def process_all_sbu(self):
        for article in self.all_articles:
            all_sentences = sent_tokenize(article.data)
            for sentence in all_sentences:
                sbu = SBU(sentence)
                sbu.preprocess()
                article.all_sbu.append(sbu)

    def get_all_tokens(self):
        for article in self.all_articles:
            for sbu in article.all_sbu:
                article.clean_words += sbu.clean_tokens

    def preprocess(self):
        self.process_articles()
        self.process_all_sbu()
        self.get_all_tokens()
        self.count_all_words()

    def count_all_words(self):
        for article in self.all_articles:
            for w in article.clean_words:
                if w in self.word_counts:
                    self.word_counts[w] += 1
                else:
                    self.word_counts[w] = 1
                self.total += 1

    # create probability distribution
    def step1(self):
        for k,v in self.word_counts.items():
            self.distribution[k] = v/self.total

    # for each sentence calculate weight(Sj)
    def step2(self):
        for article in self.all_articles:
            for sbu in article.all_sbu:
                for w in sbu.clean_tokens:
                    p_wi = self.distribution[w]
                    count_wi = sbu.clean_tokens.count(w)
                    sbu.weight += p_wi/count_wi

    def get_best_word(self):
        return max(self.distribution.items(), key=operator.itemgetter(1))[0]

    # pick best scoring sentence which contains the highest prob word
    def step3(self):
        best_word = self.get_best_word()
        best_weight = 0.0
        best_sbu = None
        for article in self.all_articles:
            for sbu in article.all_sbu:
                if best_word in sbu.clean_tokens and sbu.weight > best_weight:
                    best_weight = sbu.weight
                    best_sbu = sbu
        self.curr_sbu = best_sbu
        self.summary.content.append(best_sbu.sentence)
        self.summary.count += len(best_sbu.word_tokens)

    # update word probabilities p(wi)
    def step4(self):
        for w in self.curr_sbu.clean_tokens:
            self.distribution[w] = self.distribution[w]*self.distribution[w]

    def step3_simplified(self):
        best_word = self.get_best_word()
        best_weight = 0.0
        best_sbu = None
        for article in self.all_articles:
            for sbu in article.all_sbu:
                if best_word in sbu.clean_tokens and sbu.weight > best_weight and sbu.sentence not in self.summary.content:
                    best_weight = sbu.weight
                    best_sbu = sbu
        self.curr_sbu = best_sbu
        self.summary.content.append(best_sbu.sentence)
        self.summary.count += len(best_sbu.word_tokens)

    def pick_highest_probability_sentence(self):
        best_weight = 0.0
        best_sbu = None
        for article in self.all_articles:
            for sbu in article.all_sbu:
                if sbu.weight > best_weight:
                    best_weight = sbu.weight
                    best_sbu = sbu
        self.curr_sbu = best_sbu
        self.summary.content.append(best_sbu.sentence)
        self.summary.count += len(best_sbu.word_tokens)

    def sample_best_from_article(self, sample_article):
        best_weight = 0.0
        best_sbu = None
        for sbu in sample_article.all_sbu:
            if sbu.weight > best_weight:
                best_weight = sbu.weight
                best_sbu = sbu
        self.curr_sbu = best_sbu
        self.summary.content.append(best_sbu.sentence)
        self.summary.count += len(best_sbu.word_tokens)

    def summarize(self, length):
        if self.version == 'orig':
            self.step1()
            while self.summary.count <= length:
                self.step2()
                self.step3()
                self.step4()
            print('\n%s\n' % self.summary.make_summary())
        elif self.version == 'best-avg':
            self.step1()
            while self.summary.count <= length:
                self.step2()
                self.pick_highest_probability_sentence()
                self.step4()
            print('\n%s\n' % self.summary.make_summary())
        elif self.version == 'simplified':
            self.step1()
            while self.summary.count <= length:
                self.step2()
                self.step3_simplified()
            print('\n%s\n' % self.summary.make_summary())
        elif self.version == 'leading':
            sample_id = randint(0, len(self.all_articles)-1)
            sample_article = self.all_articles[sample_id]
            self.step1()
            while self.summary.count <= length:
                self.step2()
                self.sample_best_from_article(sample_article)
                self.step4()
            print('\n%s\n' % self.summary.make_summary())

def main():
    version = sys.argv[1]
    inputs = sys.argv[2:]
    all_articles = []
    for val in inputs:
        file = open(val, 'r')
        data = file.read()
        all_articles.append(data)

    corpus = '\n'.join(all_articles)
    cluster = Cluster(version, corpus, all_articles)
    cluster.preprocess()
    cluster.summarize(100)

if __name__== "__main__":
  main()
