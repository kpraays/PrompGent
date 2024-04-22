import dialogues_process
import pickle
from transformers.pipelines.pt_utils import KeyDataset
# from sentence_transformers import SentenceTransformer

# similarity_model = SentenceTransformer('all-MiniLM-L6-v2')

with open("user_themes", "rb") as fil:
    input_records = pickle.load(fil)
    
for record in input_records:
    start_index = record['text'].find("\nTheme:")
    print(start_index)
    end_index = record['text'].find("\nHere are the top candidates")
    print(end_index)
    extracted_history = record['text'][start_index:end_index]
    main_theme = dialogues_process.user_theme("similarity_model", extracted_history)
    print(main_theme)
    modified_prompt = record['text'][0:start_index] + r"\nTheme: " + main_theme + record['text'][end_index:]
    record = modified_prompt
    
dset = KeyDataset(input_records, key="text")
print(dset[-1])   
    
    