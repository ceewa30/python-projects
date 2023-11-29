import glob
from nltk.sentiment import SentimentIntensityAnalyzer
from matplotlib import pyplot as plt

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


plt.plot(dates, positivity, 'g', linestyle='-', label='Positive')
plt.title('Diary Tone')
plt.xlabel('Date')
plt.ylabel('Mode')

plt.plot(dates, negativity, 'r', linestyle='--', label='Negative')

plt.plot(dates, neutral, 'y', linestyle='-.', label='Neutral')

plt.plot(dates, compound, 'b', linestyle=':', label='Compound')

# plt.legend(['Positive', 'Negative'])
plt.legend()

plt.grid()

plt.tight_layout()

# plt.savefig('plot.png')

plt.show()

