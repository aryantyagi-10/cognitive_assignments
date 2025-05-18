import nltk;
import re;
from nltk.corpus import stopwords;
from nltk.tokenize import word_tokenize;
from nltk.stem import PorterStemmer;
from nltk.stem import WordNetLemmatizer;
nltk.download('punkt');
nltk.download('stopwords');
nltk.download('wordnet');

paragraph = """Technology is evolving faster than ever before. 
Smart devices are becoming essential parts of our daily lives. 
Artificial Intelligence helps businesses automate tasks and make smarter decisions. 
Virtual Reality is changing the way we experience games, movies, and education. 
Even healthcare is being transformed through wearable tech and data-driven diagnostics.""";

words_alpha = re.findall(r'\b[a-zA-Z]+\b', paragraph.lower());
print("Words with only alphabets (lowercase):\n", words_alpha)

stop_words = set(stopwords.words('english'));
filtered_words = [word for word in words_alpha if word not in stop_words];
print("\nFiltered Words (after removing stopwords):\n", filtered_words);

porter_stemmer = PorterStemmer();
stemmed_words = [porter_stemmer.stem(word) for word in filtered_words];
print("\nStemmed Words (using PorterStemmer):\n", stemmed_words);

lemmatizer = WordNetLemmatizer();
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words];
print("\nLemmatized Words (using WordNetLemmatizer):\n", lemmatized_words);