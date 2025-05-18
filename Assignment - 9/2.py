import nltk;
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer;
from nltk.corpus import wordnet;
nltk.download('wordnet');
nltk.download('omw-1.4');

filtered_words = ['technology', 'transformed', 'way', 'live', 'work', 'communicate','smartphones', 'artificial', 'intelligence', 'innovation','continues', 'shape', 'future', 'internet', 'connects', 'people','across', 'globe', 'instant', 'automation', 'machine', 'learning','changing', 'industries', 'creating', 'new', 'opportunities','technology', 'sometimes', 'feel', 'overwhelming', 'offers','incredible', 'tools', 'solving', 'realworld', 'problems'];
porter = PorterStemmer();
lancaster = LancasterStemmer();
lemmatizer = WordNetLemmatizer();
print(f"{'Original':<15}{'Porter':<15}{'Lancaster':<15}{'Lemmatized':<15}");
print("-" * 60);
for word in filtered_words:
    porter_stem = porter.stem(word);
    lancaster_stem = lancaster.stem(word);
    lemmatized = lemmatizer.lemmatize(word);
    print(f"{word:<15}{porter_stem:<15}{lancaster_stem:<15}{lemmatized:<15}");
