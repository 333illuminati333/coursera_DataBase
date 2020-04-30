# -*- coding: utf-8 -*-
import sys
import json
import string


def normalizer_word(word):
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


def get_sentiment(sentiment_dict, line):
    sentiment_score = 0
    for word in line.split(' '):
        if word in sentiment_dict:
            sentiment_score += sentiment_dict[word]
    return sentiment_score


def main():
    sentiment_dict = construct_dict(sys.argv[1])
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        d = json.loads(line.encode('utf8'))
        if 'text' in d.keys():
            norm_tweet = normalizer_word(d['text'].encode('utf8'))
            print(get_sentiment(sentiment_dict, norm_tweet))


if __name__ == '__main__':
    main()
