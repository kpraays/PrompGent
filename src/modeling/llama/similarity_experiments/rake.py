from rake_nltk import Rake
import operator
import nltk

nltk.download('stopwords')
nltk.download('punkt')

# Sample list of dialogues
dialogues = ["Can you please find me a room in Boston through Airbnb.com?"]
# ["Hello", "Open Encyclopedia website.", "Search for biotechnology"]
# Initialize RAKE using NLTK's stop words
rake_nltk_var = Rake()

# Combine dialogues into a single text for analysis
combined_text = " ".join(dialogues)

# Extract keywords
rake_nltk_var.extract_keywords_from_text(combined_text)
keyword_ranked = rake_nltk_var.get_ranked_phrases_with_scores()

# Display the top-ranked phrases
print("Top-ranked phrases:")
for score, phrase in keyword_ranked[:5]:  # Adjust number as needed
    print(f"{phrase} (Score: {score})")

# Assuming you want to find a dialogue that best matches the top keywords
# Here is a simple way to score each dialogue based on the top keywords
# This is a basic implementation, focusing on keyword presence

top_keywords = [phrase for score, phrase in keyword_ranked[:5]]  # Adjust slice as needed
dialogue_scores = {}

for dialogue in dialogues:
    score = 0
    for keyword in top_keywords:
        if keyword in dialogue:
            score += 1
    dialogue_scores[dialogue] = score

# Sort dialogues by their score
sorted_dialogues = sorted(dialogue_scores.items(), key=lambda x: x[1], reverse=True)

# Display the dialogue with the highest score
if sorted_dialogues:
    print("\nDialogue most representative of the main themes:")
    print(sorted_dialogues[0][0])
else:
    print("No dialogues matched the criteria.")
