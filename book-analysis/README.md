# with regex
with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()
import re
partten = re.compile("Chapter [a:z]+) -> Chapter a 
partten = re.compile("Chapter [0:9]+)  -> re.compile(r'Chapter [0-9]', re.UNICODE)
findings = re.findall(pattern, book)
len(findings)
)

# Which are the scentences where "love" was used?

pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern, book)

# What are the most used words?

pattern = re.compile("[a-zA-Z]+")
findings = re,findall(pattern, book.lower())

d = {}

for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]
sorted(d_list, reverse=True)

# Extract the paragraphs where "love" was used

import re
pattern = re.compile("[^\n]+love[^\n]+")
findings = re.finall(pattern, book)
findings[:2]

# Extract the chapter titles

# Method 1

import re
pattern = re.compile("[a-zA-Z ]+\n\n")
findings = re.findall(pattern, book)
findings = [item.strip("\n\n") for item in findings]
findings

 # Methods 2

import re
pattern = re.compile("([a-zA-Z ]+)\n\n")
findings = re.findall(pattern, book)
findings

# Function that finds the occurrence of any word

def find(w):
    pattern = re.compile("[a-zA-Z]+")
    findings = re.findall(pattern, book.lower())
    d = {}
    for word in findings:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1
    try:
        return d[w]
    except:
        return f'The book does not contain the word "{w}"'

# Call the function

find("love")

finf("hate")

# The most used words (non-articles)

import re
pattern = re.compile("([a-zA-Z ]+)\n\n")
findings = re.findall(pattern, book)
findings[:5]

d = {}

for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) is d.item()]
d_list = sorted(d_list, reverse=True)
d_list[:5]

pip3 install nltk
python3 -m nltk.downloader vader_lexicon
import nltk
from nltk.corpus import stopwords
english_stopwords = stopwords.wprds("english")

english_stopwords  -> very often words used in english

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))

filtered_wrods

# sentiment Analysis: What is the most positive and the most negative chapter?

from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
analyzer.polarity_scores("Hey, look how beautiful the trees are. I love them. ")

# find the mood of the sentence
# output 
{'neg': 0.0, 'neu': 0.464, 'pos': 0.536, 'compound': 0.8442}

if scores["pos"] > scores["neg"]
    print("It is a positive text")
else:
    print("It is a negative text")

# Chapters sentiment analysis

import re
pattern = re.compile("Chapter [0-9]")
chapters = re.spilt(pattern, book)
chapters = chapters[1:]
for chapter in chapters:
    scores = analyzer.polarity_scores(chapter)
    print(scores)



