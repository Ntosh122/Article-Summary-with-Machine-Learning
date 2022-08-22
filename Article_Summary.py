import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article


def summarize():
    url = url_text.get('1.0', 'end').strip()
    article = Article(url)
    article.download()
    article.parse()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentimental_analysis.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # performing sentimental analysis
    analysis = TextBlob(article)
    sentimental_analysis.delete('1.0', 'end')
    sentimental_analysis.insert('1.0',
                                f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentimental_analysis.config(state='disabled')

    article.nlp()

    analysis = TextBlob(article.text)


root = tk.Tk()
root.title("Article Summarizer - With Machine Learning")
root.geometry('1200x600')

#
url_label = tk.Label(root, text='Paste Article Url Here')
url_label.pack()

url_text = tk.Text(root, height=1, width=140)
url_text.pack()

t_label = tk.Label(root, text='Title')
t_label.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

a_label = tk.Label(root, text='Author')
a_label.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

p_label = tk.Label(root, text='Publication Date')
p_label.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

s_label = tk.Label(root, text='Summary')
s_label.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

se_label = tk.Label(root, text='Sentimental Analysis')
se_label.pack()

sentimental_analysis = tk.Text(root, height=1, width=140)
sentimental_analysis.config(state='disabled', bg='#dddddd')
sentimental_analysis.pack()

button = tk.Button(root, text='Summarize', command=summarize)
button.pack()

root.mainloop()
