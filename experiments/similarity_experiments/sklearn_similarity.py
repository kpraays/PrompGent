from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample list of dialogues
dialogues = ["Hi", "Can you please find me a room in Boston through Airbnb.com?", "13th June to 15th June for 2 People.", "Is 'Modern Suite, Jacuzzi, Yoga Loft near Boston' available for the above-mentioned date?", "What is the cost for 2-night stay?", "Ok. Thanks for the information."]

# Convert the dialogues to TF-IDF vectors
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(dialogues)

# Calculate cosine similarity between each pair of dialogues
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

average_similarity = np.nanmean(similarity_matrix, axis=1)
print(dialogues[np.argmax(average_similarity)])
