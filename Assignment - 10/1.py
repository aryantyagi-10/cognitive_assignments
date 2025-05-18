import nltk;
import string;
from nltk.corpus import stopwords;
from nltk.tokenize import word_tokenize, sent_tokenize;
from nltk.probability import FreqDist;
nltk.download('punkt');
nltk.download('stopwords');

paragraph = """Technology has transformed the way we live, work, and communicate. 
From smartphones to artificial intelligence, innovation continues to shape our future. 
The internet connects people across the globe in an instant. 
Automation and machine learning are changing industries and creating new opportunities. 
While technology can sometimes feel overwhelming, it offers incredible tools for solving real-world problems.""";

text_lower = paragraph.lower();
text_clean = text_lower.translate(str.maketrans('', '', string.punctuation));
print("Text in lowercase with removed punctuation is\n",text_clean);

words = word_tokenize(text_clean);
print("\nWord tokenization\n",words);
sentences = sent_tokenize(paragraph);
print("\nSentence tokenization\n",sentences);

word = word_tokenize(text_lower);
print("\nWord tokenization\n",word);
split = text_lower.split();
print("\n Split using python function\n",split);

stop_words = set(stopwords.words('english'));
filtered_words = [word for word in words if word not in stop_words];
print("\nText after removing stop words is\n",filtered_words);

freq_dist = FreqDist(filtered_words)
print("\nWord Frequency Counts\n");
for word, freq in freq_dist.items():
    print(f"{word}: {freq}");