from p1 import *
from collections import Counter
import numpy as np

def get_token():
    return input("Word: ")


def display_review(review, pos_score, neg_score, neu_score):
    next_line = chr(10)
    return f'{next_line * 2}Review: {review} {next_line * 2}Scores(0 - 1): Positive =  {pos_score}, Negative = {neg_score}, Neutral = {neu_score}'


def search_function(word):
    count_reviews = Counter()
    for review, pos_score, neg_score, neu_score\
            in zip(data['Text'], data['Positive'], data['Negative'], data['Neutral']):
        if word in review:
            #print(display_review(review, pos_score, neg_score, neu_score))
            print(review)
            sent = get_sentiment(pos_score, neg_score, neu_score)
            print("Sentiment:", sent)
            count_reviews[sent] += 1
    return count_reviews

def total_reviews(count_reviews):
    return sum(count_reviews.values())

def display_pie_chart(count_reviews):
    sentiments = ["Positive", "Negative", "Neutral"]
    arr = np.array([count_reviews[sent] for sent in sentiments])
    plt.pie(arr, labels = sentiments, startangle=45, colors=['gold','r','royalblue'])
    sort_legend = True
    plt.legend(title = "Sentiments of reviews")
    plt.tight_layout()
    plt.show()


display_pie_chart(search_function(get_token()))
