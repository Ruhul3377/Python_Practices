from turtle import width, window_height
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

# Read text 
text = open('sample.txt', mode ='r', encoding='utf-8').read()
stopwords = STOPWORDS
print(stopwords)


wc = WordCloud(
        background_color="white",
        stopwords=stopwords,
        height= 400,
        width= 600

)



wc.generate(text)

# store to file
wc.to_file('wordcloud_output.png')