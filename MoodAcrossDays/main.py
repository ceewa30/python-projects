import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

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

print(positivity)
dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)

fig = px.pie(values=positivity, names=dates, title='Population of European continent')
fig.show()


df = pd.DataFrame({'values': [positivity, negativity, neutral, compound], 'groups' : ['G1', 'G2', 'G3', 'G4']})
fig1 = px.pie(df, values = 'values', names = 'groups')

fig1.show()
