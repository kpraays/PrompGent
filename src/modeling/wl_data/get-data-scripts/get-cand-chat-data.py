from huggingface_hub import snapshot_download



# candidates files
snapshot_download(
    repo_id="McGill-NLP/WebLINX-full", 
    repo_type="dataset", 
    allow_patterns="candidates/*.jsonl", 
    local_dir="/home/kapmcgil/scratch/weblinx/modeling/wl_data",
    cache_dir="/home/kapmcgil/scratch/weblinx/modeling/llama/dummy-cache",
    local_dir_use_symlinks=False
    )
print("got candidates...")

# data files
snapshot_download(
    repo_id="McGill-NLP/WebLINX-full", 
    repo_type="dataset", 
    allow_patterns="data/*.csv", 
    local_dir="/home/kapmcgil/scratch/weblinx/modeling/wl_data",
    cache_dir="/home/kapmcgil/scratch/weblinx/modeling/llama/dummy-cache",
    local_dir_use_symlinks=False
    )
print("got data csv files...")

# chat files
snapshot_download(
    repo_id="McGill-NLP/WebLINX-full", 
    repo_type="dataset", 
    allow_patterns="chat/*.csv", 
    local_dir="/home/kapmcgil/scratch/weblinx/modeling/wl_data",
    cache_dir="/home/kapmcgil/scratch/weblinx/modeling/llama/dummy-cache",
    local_dir_use_symlinks=False
    )
print("got chat csv files...")