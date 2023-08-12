import streamlit as st
import os
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

paths = os.walk("diary/")
for each in paths:
    paths = [f"diary/{entry}" for entry in each[2]]
print(paths)

analyzer = SentimentIntensityAnalyzer()
diary_polarity = {}
date = []
positivity = []
negativity = []

st.title("Diary Tone")


for path in paths:
    stem = path.split("/")[1][:-4]
    print(stem)
    with open(path, "r", encoding="utf8") as file:
        entry = file.read()
        score = analyzer.polarity_scores(entry)
        diary_polarity[stem] = score
        date.append(stem)
        positivity.append(score['pos'])
        negativity.append(score['neg'])

st.header("Positivity")
figure = px.line(x=date, y=positivity, labels=("Date", "Positivity"))
st.plotly_chart(figure)

st.header("Negativity")
figure2 = px.line(x=date, y=negativity, labels=("Date", "Negativity"))
st.plotly_chart(figure2)
