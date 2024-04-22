import json
import re
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def get_utterances():
    with open("/home/kapmcgil/scratch/weblinx/modeling/wl_data/data-process/extracted_chats_valid_demos.json", "r") as chat_file:
        demos_chat = json.load(chat_file)

    per_demo_utterances = {}
    for demo in demos_chat.keys():
        chats = []
        for time_sequences in demos_chat[demo]:
            chats.append(time_sequences['utterance'])
        per_demo_utterances[demo] = chats
    # print(per_demo_utterances)
    
    print("Retrieved all utterances for all demos...")
    return per_demo_utterances

def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print('all-MiniLM-L6-v2' + "LOADED" + "...")
    return model

def process_utterances(dialogues):
    dialogues_processed = []
    for utterance in dialogues:
        
        sen = re.sub(r"[/]+", " ", utterance)
        sen = sen.lower()
        sen = re.sub(r"\s{2,}", "", sen)
        sen = re.sub("hi", "", sen)
        sen = re.sub("hello", "", sen)
        sen = re.sub("okay.", "", sen)
        sen = re.sub("done.", "", sen)
        sen = re.sub("alright.", "", sen)
        
        if len(sen) > 1:
            dialogues_processed.append(sen)
    print(f"processed dialogue list {dialogues_processed}")
    return dialogues_processed

def process_similarity(similarity_model, dialogues):
    embeddings = similarity_model.encode(dialogues)
    similarity_matrix = cosine_similarity(embeddings)
    average_similarity = np.nanmean(similarity_matrix, axis=1)
    top_indices = np.argsort(average_similarity)[-3:][::-1]
    
    # return top 3 dialogues with the best matched one first in the list.
    return [dialogues[index] for index in top_indices]

def demo_theme():
    main_utterance_per_demo = {}
    per_demo_utterances = get_utterances()
    model = load_model()
    for demo in per_demo_utterances.keys():
        dialogues = per_demo_utterances[demo]
        dialogues_processed = process_utterances(dialogues)
        
        main_utterances = process_similarity(model, dialogues_processed)
        main_utterance_per_demo.setdefault(demo, {})["TOP-3"] = main_utterances
        main_utterance_per_demo[demo]["processed_dialogues"] = dialogues_processed
        print(f"Processed demo {demo} - retrieved the main utterance...")
    return main_utterance_per_demo

all_demo_top = demo_theme()
print(all_demo_top)
    
with open("main_utterance_per_demo.json", "w") as main_utterances_file:
    json.dump(all_demo_top, main_utterances_file)
    print("######   Saved the data...   ######")