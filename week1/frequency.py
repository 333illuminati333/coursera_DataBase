# -*- coding: utf-8 -*-
import sys
import json
import string

from collections import defaultdict


def norm_word(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word


def construct_dict(sentiment_score_file):
    sentiment_file = open(sentiment_score_file)
    scores = {}
    for line in sentiment_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


def update_dict(dct, tweet):
    for word in tweet.split():
        if word in dct:
            dct[word] += 1
        else:
            dct[word] = 1


def get_sentiment(sentiment_dict, line):
    sentiment_score = 0
    non_sentiment_words = []
    for word in line.split(' '):
        if word in sentiment_dict:
            sentiment_score += sentiment_dict[word]
        else:
            non_sentiment_words.append(word)
    return sentiment_score, non_sentiment_words


def main():
    dct = defaultdict()
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        d = json.loads(line.encode('utf8'))
        if 'text' in d.keys():
            update_dict(dct, norm_word(d['text'].encode('utf8')))

    all_occ = sum(dct.values())
    for word in dct.keys():
        print(word, dct[word] / float(all_occ))


if __name__ == '__main__':
    main()
