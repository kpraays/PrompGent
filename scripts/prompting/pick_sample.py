import json
import random

with open("./llama/formatted_samples.json", "r") as samples_file:
    samples = json.load(samples_file)
    
def get_sample():
    sample_number = random.randint(0,99)
    print(f"Setting sample with ID: {sample_number}")
    return samples[str(sample_number)]

# print(get_sample())