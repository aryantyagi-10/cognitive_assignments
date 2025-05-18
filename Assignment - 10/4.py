import nltk;
import re;
from sklearn.feature_extraction.text import TfidfVectorizer;
from sklearn.metrics.pairwise import cosine_similarity;
nltk.download('punkt');

text_ai = """Artificial Intelligence (AI) is revolutionizing industries by automating tasks and improving decision-making. 
It uses machine learning algorithms to process large datasets and make predictions. AI applications range from self-driving cars to voice assistants, 
and it continues to evolve rapidly.""";
text_blockchain = """Blockchain is a decentralized ledger technology that ensures secure transactions without intermediaries. 
It is most commonly known for being the backbone of cryptocurrencies like Bitcoin. Blockchain’s transparency and security make it a powerful tool for various industries, 
from finance to supply chains.""";

def preprocess_text(text):
    text = text.lower(); 
    text = re.sub(r'[^\w\s]', '', text);
    tokens = nltk.word_tokenize(text);
    return tokens;
tokens_ai = preprocess_text(text_ai);
print("Tokens for AI:", tokens_ai, "\n");
tokens_blockchain = preprocess_text(text_blockchain);
print("Tokens for Blockchain:", tokens_blockchain);

def jaccard_similarity(tokens1, tokens2):
    set1, set2 = set(tokens1), set(tokens2);
    intersection = set1.intersection(set2);
    union = set1.union(set2);
    return len(intersection) / len(union);

jaccard_sim = jaccard_similarity(tokens_ai, tokens_blockchain)
print("\nJaccard Similarity:", jaccard_sim);

vectorizer = TfidfVectorizer();
texts = [text_ai, text_blockchain];
tfidf_matrix = vectorizer.fit_transform(texts);
cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1]);
print("\nCosine Similarity:", cosine_sim[0][0]);

if jaccard_sim > cosine_sim:
    print("\nJaccard Similarity gives better insights in this case.");
else:
    print("\nCosine Similarity gives better insights in this case.");
