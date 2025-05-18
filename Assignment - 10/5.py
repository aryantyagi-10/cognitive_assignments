from textblob import TextBlob;
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer;
from wordcloud import WordCloud;
import matplotlib.pyplot as plt;

review = "I recently bought the XYZ smartphone, and I am really impressed with its performance! The battery lasts all day, and the camera quality is outstanding. The display is vibrant and smooth, making it perfect for gaming and media consumption. Although the price is a bit high, I think it's totally worth it for all the features it offers. Highly recommend it!";

blob = TextBlob(review);
textblob_polarity = blob.sentiment.polarity;
print("TextBlob Polarity:", textblob_polarity);
textblob_subjectivity = blob.sentiment.subjectivity;
print("TextBlob Subjectivity:", textblob_subjectivity);

analyzer = SentimentIntensityAnalyzer();
vader_sentiment = analyzer.polarity_scores(review);
print("\nVADER Sentiment Scores:", vader_sentiment);
def classify_review(polarity_score):
    if polarity_score > 0.1:
        return "Positive";
    elif polarity_score < -0.1:
        return "Negative";
    else:
        return "Neutral";
classification = classify_review(textblob_polarity);
print("\nReview Classification (TextBlob):", classification);

positive_reviews = [review];
positive_reviews_text = " ".join(positive_reviews);
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_reviews_text);
plt.figure(figsize=(10, 5));
plt.imshow(wordcloud, interpolation='bilinear');
plt.axis('off');
plt.show();