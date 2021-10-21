from numpy import negative
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiments = SentimentIntensityAnalyzer()

data = pd.read_csv("Reviews2.csv")

ratings = data["Score"].value_counts()
numbers = ratings.index
quantity = ratings.values

data = data.dropna()

data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["Text"]]
data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["Text"]]
data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["Text"]]
#print(data.head())

x = sum(data["Positive"])
y = sum(data["Negative"])
z = sum(data["Neutral"])

def get_sentiment(pos, neg, neu):
    scores_dict = {pos: "Positive", neg: "Negative", neu: "Neutral"}
    sentiment = pos #model seems to overvalue neutrality
    if pos + neg < neu:
        sentiment = neu
    if sentiment < neg:
        sentiment = neg
    return scores_dict[sentiment]

#def sentiment_score(a, b, c):
#    if (a>b) and (a>c):
#        print("Positive 😊 ")
#    elif (b>a) and (b>c):
#        print("Negative 😠 ")
#    else:
#        print("Neutral 🙂 ")

#sentiment_score(x, y, z)

#print("Positive: ", x)
#print("Negative: ", y)
#print("Neutral: ", z)
