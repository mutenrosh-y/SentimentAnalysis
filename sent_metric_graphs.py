from matplotlib import pyplot as plt
from nltk.tag import pos_tag_sents
from p1 import *
fig = plt.figure()
ax = fig.subplots()
ax1 = fig.add_subplot(131)
sns.histplot(data['Positive'], color="yellow", bins=10)
ax1.set_ylabel('Positive')
ax1.set_xlabel('Ages')
ax2 = fig.add_subplot(132)
sns.histplot(data['Negative'], color="red", bins=10)
ax2.set_ylabel('Negative')
ax2.set_xlabel('Ages')
ax2 = fig.add_subplot(133)
sns.histplot(data['Neutral'], color="lightblue", bins=10)
ax2.set_ylabel('Neutral')
ax2.set_xlabel('Ages')
ax.set_title('Product Sentiments')
plt.show()