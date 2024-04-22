import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity

# def load_model():
#     from sentence_transformers import SentenceTransformer
#     model = SentenceTransformer('all-MiniLM-L6-v2')
#     return model

def process_similarity(similarity_model, dialogues):
    embeddings = similarity_model.encode(dialogues)
    similarity_matrix = cosine_similarity(embeddings)
    average_similarity = np.nanmean(similarity_matrix, axis=1)
    return dialogues[np.argmax(average_similarity)]
    

def process_utterances(utterance):
    sen = re.sub(r"\s*\[[0-9:+-]+\]\s*", "```", utterance)
    parts = sen.split("```")
    parts = [part for part in parts if len(part)>0]
    return parts

def user_theme(similarity_model, utterance_history):
    print("Inside dialogues process, user_theme.############")
    processed_dialogues = process_utterances(utterance_history)
    main_theme_history = process_similarity(similarity_model, processed_dialogues)
    return main_theme_history
    