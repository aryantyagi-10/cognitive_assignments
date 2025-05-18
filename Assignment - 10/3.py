from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer;
import numpy as np;

texts = [
    "New tech innovations change the world every day.",
    "The best smartphone of 2025 is here, offering amazing features.",
    "Breaking news: Natural disaster causes widespread damage across the region."
];

vectorizer = CountVectorizer();
X_count = vectorizer.fit_transform(texts);
count_feature_names = vectorizer.get_feature_names_out();
print("Bag of Words Representation:");
print(X_count.toarray());
print("Feature Names (Words in BoW):", count_feature_names);

tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(texts);
print("TF-IDF Scores: ");
print(X_tfidf.toarray());
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out();
print("Feature Names (Words in TF-IDF): ",tfidf_feature_names);

print("\nTop 3 Keywords (TF-IDF Scores) for each Text:");
for i, text in enumerate(texts):
    print(f"\nText {i + 1}: {text}");
    tfidf_scores = X_tfidf[i].toarray().flatten();
    top_indices = tfidf_scores.argsort()[-3:][::-1];
    top_keywords = [(tfidf_feature_names[idx], tfidf_scores[idx]) for idx in top_indices];
    print("Top 3 Keywords (Word, TF-IDF Score):");
    for keyword, score in top_keywords:
        print(f"'{keyword}': {score:.4f}");
