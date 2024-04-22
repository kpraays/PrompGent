from rake_nltk import Rake
import operator
import nltk
import re

def process_similarity(similarity_model, dialogues):
    # Initialize RAKE using NLTK's stop words
    rake_nltk_var = Rake()

    # Combine dialogues into a single text for analysis
    combined_text = " ".join(dialogues)

    # Extract keywords
    rake_nltk_var.extract_keywords_from_text(combined_text)
    keyword_ranked = rake_nltk_var.get_ranked_phrases_with_scores()

    # Keep the top 20 keywords for ranking the dialogues.
    top_keywords = [phrase for score, phrase in keyword_ranked[:20]]
    dialogue_scores = {}

    for dialogue in dialogues:
        score = 0
        for keyword in top_keywords:
            if keyword in dialogue:
                score += 1
        dialogue_scores[dialogue] = score

    # Sort dialogues by their score
    sorted_dialogues = sorted(dialogue_scores.items(), key=lambda x: x[1], reverse=True)

    
    if sorted_dialogues:
        output_theme = sorted_dialogues[0][0]
    else:
        output_theme = "None"
    return output_theme

def process_utterances(utterance):
    sen = re.sub(r"\s*\[[0-9:+-]+\]\s*", "```", utterance)
    parts = sen.split("```")
    parts = [part for part in parts if len(part)>0]
    return parts

def user_theme(similarity_model, utterance_history):
    #print("Inside dialogues process, user_theme.############")
    processed_dialogues = process_utterances(utterance_history)
    main_theme_history = process_similarity(similarity_model, processed_dialogues)
    return main_theme_history