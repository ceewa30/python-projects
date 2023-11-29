import glob
from nltk.sentiment import SentimentIntensityAnalyzer
from matplotlib import pyplot as plt
import numpy as np

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

positivity = []
negativity = []
neutral = []
compound = []
for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])
    neutral.append(scores["neu"])
    compound.append(scores["compound"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

x_indexes = np.arange(len(dates))
width = 0.25

plt.bar(x_indexes - width, positivity, width=width, color="#444444", label="Positive")

plt.bar(x_indexes, negativity, width=width, color="#a4a4a4", label="Negative")

plt.bar(x_indexes + width, neutral, width=width, color="#008fd5", label="Neutral")

# plt.bar(x_indexes + 2*width, compound, width=width, color="#e5ae38", label="Compound")

plt.legend()

# change the date index to date
plt.xticks(ticks=x_indexes, labels=dates)

plt.grid()

plt.tight_layout()

plt.show()