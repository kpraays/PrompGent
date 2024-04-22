from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_model():
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model


def process_similarity
# dialogues = ["Hello, how are you?", "I'm fine, thank you!", "What's the main topic of our conversation?"]
dialogues = ["Hi", "Can you please find me a room in Boston through Airbnb.com?", "13th June to 15th June for 2 People.", "Is 'Modern Suite, Jacuzzi, Yoga Loft near Boston' available for the above-mentioned date?", "What is the cost for 2-night stay?", "Ok. Thanks for the information."]
embeddings = model.encode(dialogues)

similarity_matrix = cosine_similarity(embeddings)

print(similarity_matrix)

average_similarity = np.nanmean(similarity_matrix, axis=1)
print(average_similarity)
print(dialogues[np.argmax(average_similarity)])
["[-00:14] Hi", "[00:35] Can you please find me a room in Boston through Airbnb.com?", "[02:30] 13th June to 15th June for 2 People.", "[04:54] Is 'Modern Suite, Jacuzzi, Yoga Loft near Boston' available for the above-mentioned date?"]


def process_utterances(utterance):
    import re
    sen = re.sub(r"\s*\[[0-9:+-]+\]\s*", "```", utterance)
    parts = sen.split("```")
    parts = [part for part in parts if len(part)>0]
    return parts



# import numpy as np
# import re
# from sklearn.metrics.pairwise import cosine_similarity

# def process_similarity(similarity_model, dialogues):
#     embeddings = model.encode(dialogues)
#     similarity_matrix = cosine_similarity(embeddings)
#     average_similarity = np.nanmean(similarity_matrix, axis=1)
#     return dialogues[np.argmax(average_similarity)]
    

# def process_utterances(utterance):
#     sen = re.sub(r"\s*\[[0-9:+-]+\]\s*", "```", utterance)
#     parts = sen.split("```")
#     parts = [part for part in parts if len(part)>0]
#     return parts

# def user_theme(similarity_model, utterance_history):
#     processed_dialogues = process_utterances(utterance_history)
#     main_theme_history = process_similarity(similarity_model, processed_dialogues)
#     return main_theme_history
    

    