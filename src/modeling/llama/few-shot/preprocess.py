import json
import re
with open("raw_text.txt", "r") as data_file:
    data = data_file.read()
    
lines = data.split("\n")
samples = []
for line in lines:
    if len(line) > 0 and "Here is an example:" in line:
        line = re.sub(r"[\"]*", "", line)
        samples.append(line)
        
samples_dict = {}
for i in range(len(samples)):
    samples_dict[i] = samples[i]
    
with open("formatted_samples.json", "w") as output_file:
    json.dump(samples_dict, output_file)

print("Preprocessing complete...")