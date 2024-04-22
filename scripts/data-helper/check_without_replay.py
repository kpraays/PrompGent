import os

# The root directory containing the subfolders
root_directory = "/home/kapmcgil/scratch/weblinx/modeling/wl_data/demonstrations"

# List to hold the names of subfolders that do not contain 'replace.json'
subfolders_without_file = []
num_total_demos = 0

# Walk through the root directory
for dirpath, dirnames, filenames in os.walk(root_directory):
    if dirpath.split("/")[-2]=="demonstrations":
    # Skip the root directory itself, only consider subdirectories
    
        # Check if 'replace.json' is not in the filenames within the current subdirectory
        if 'replay.json' in filenames:
            # Extract the subfolder name and add it to the list
            subfolder_name = os.path.basename(dirpath)
            num_total_demos+=1
            try:
                # Attempt to open the file
                with open(f"{root_directory}/{subfolder_name}/replay.json", 'r') as file:
                    # If successful, you could process the file here
                    pass
            except Exception as e:
                # If an exception occurs, add the file name to the list
                subfolders_without_file.append(subfolder_name)
            
print(set(subfolders_without_file))
print(len(set(subfolders_without_file)))
print(f"Total directories are:{num_total_demos}")



