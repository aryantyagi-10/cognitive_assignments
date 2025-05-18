import numpy as np;
from keras.preprocessing.text import Tokenizer;
from keras.preprocessing.sequence import pad_sequences;
from keras.models import Sequential;
from keras.layers import LSTM, Dense, Embedding;
from keras.utils import np_utils;

text = """Artificial Intelligence (AI) is revolutionizing the way we live and work. From self-driving cars to virtual assistants, AI technology is becoming increasingly prevalent in our daily lives. Machine learning, a subset of AI, allows systems to learn and adapt based on data without human intervention. As AI continues to advance, its potential applications across industries are vast, including healthcare, finance, and education. However, with great power comes great responsibility, and it is important to consider the ethical implications of AI technologies as they continue to evolve.""";

tokenizer = Tokenizer();
tokenizer.fit_on_texts([text]);
sequences = tokenizer.texts_to_sequences([text])[0];
sequence_length = 5;
input_sequences = [];
for i in range(sequence_length, len(sequences)):
    input_sequences.append(sequences[i-sequence_length:i+1]);
input_sequences = np.array(input_sequences);
X = input_sequences[:, :-1];
y = input_sequences[:, -1];
X = pad_sequences(X, maxlen=sequence_length-1, padding='pre');

model = Sequential();
model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=50, input_length=sequence_length-1));
model.add(LSTM(100, return_sequences=False));
model.add(Dense(len(tokenizer.word_index)+1, activation='softmax'));
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy']);

model.fit(X, y, epochs=100, verbose=1);
def generate_text(seed_text, model, tokenizer, sequence_length, num_words=10):
    for _ in range(num_words):
        tokenized_seed = tokenizer.texts_to_sequences([seed_text])[0];
        tokenized_seed = pad_sequences([tokenized_seed], maxlen=sequence_length-1, padding='pre');
        predicted = model.predict_classes(tokenized_seed, verbose=0);
        predicted_word = tokenizer.index_word[predicted[0]];
        seed_text += ' ' + predicted_word;
    return seed_text;
seed_word = "AI";
generated_text = generate_text(seed_word, model, tokenizer, sequence_length);
print("\nGenerated Text:");
print(generated_text);