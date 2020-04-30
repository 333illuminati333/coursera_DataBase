# -*- coding: utf-8 -*-
import sys
import json
import string
from collections import defaultdict


def word_normalizer(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word


def dict_construct(sentiment_score_file):
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


def place_info(tweet):
    try:
        if tweet['place']['country_code'] == 'US':
            state = tweet['place']['full_name'][-2:]
            return True, state
        else:
            return False, ''
    except:
        pass
    return False, ''


def main():
    sentiment_dict = dict_construct(sys.argv[1])
    tweet_file = open(sys.argv[2])

    state_happy_index = defaultdict()
    total_tweet_count = 0

    for line in tweet_file:
        d = json.loads(line.encode('utf8'))
        try:
            if d['lang'] == 'en':  # accept only english tweets
                if 'text' in d.keys():  # if there is a text field
                    norm_tweet = word_normalizer(d['text'].encode('utf8'))
                    isUS, state = place_info(d)
                    if isUS:  # only if tweet is from the US
                        total_tweet_count += 1
                        sentiment_score = get_sentiment(sentiment_dict, norm_tweet)
                        if state in state_happy_index:
                            state_happy_index[state] += sentiment_score
                        else:
                            state_happy_index[state] = sentiment_score
        except:
            pass

    happiest_state = 'XX'
    happy_score = -1
    saddest_state = 'YY'
    sad_score = 99999

    for state, score in state_happy_index.items():
        if score > happy_score:
            happy_score = score
            happiest_state = state
        if score < saddest_state:
            saddest_state = state
            sad_score = score
    print(happiest_state)


if __name__ == '__main__':
    main()
