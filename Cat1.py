#Importing Natural Language Toolkit
#BRIAN MAIRURA
#CIT-227-044/2017
print("CIT-227-044/2017")
import string
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = """A Hare was making fun of the Tortoise one day for being so slow. "Do you ever get anywhere?" he asked with
 a mocking laugh. "Yes," replied the Tortoise, "and I get there sooner than you think. I'll run you a race
and prove it." The Hare was much amused at the idea of running a race with the Tortoise, but for the fun of the 
thing he agreed. So, the Fox, who had consented to act as judge, marked the distance and started the runners off. """

#Sentence tokenization
tokenized_text = sent_tokenize(text)
print(tokenized_text)

#Text tokenization
tokenized_word = word_tokenize(text)
print(tokenized_word)

#Removing stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = []
for i in tokenized_word:
    if i not in stop_words:
        filtered_tokens.append(i)
print("Tokenized Words:", tokenized_word)
print("Filtered Tokens:", filtered_tokens)

#Removing punctuations
punctuations = list(string.punctuation)
filtered_tokens2 = []
for j in filtered_tokens:
    if j not in punctuations:
        filtered_tokens.append(j)
print("Filtered Tokens After removing Punctuations:", filtered_tokens)

#Stemming
ps = PorterStemmer()
for w in tokenized_text:
    print("These are the stemmed words")
    print(w,":",ps.stem(w))

#Lemmatization
lemmatizer = WordNetLemmatizer()
sentence_words = nltk.word_tokenize(text)
for k in sentence_words:
    if k in punctuations:
        sentence_words.remove(k)

sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print ("{0:20}{1:20}".format(word,WordNetLemmatizer.lemmatize(word)))