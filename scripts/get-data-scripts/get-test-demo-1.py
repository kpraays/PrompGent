import re
demos_download = "/home/kapmcgil/scratch/weblinx/modeling/wl_data/download_demo.txt"

with open(demos_download, "r") as get_demos:
    names = re.sub("['\s]*", "", get_demos.read()[1:-2])
    demos = names.split(",")

print("get test demo 0:20")
print(len(demos))

from huggingface_hub import snapshot_download
demo_names = demos[0:20]

patterns = [f"demonstrations/{name}/*" for name in demo_names]
snapshot_download(repo_id="McGill-NLP/WebLINX-full", repo_type="dataset", local_dir="/home/kapmcgil/scratch/weblinx/modeling/wl_data", allow_patterns=patterns, ignore_patterns=["*.png", "*.mp4"], cache_dir="/home/kapmcgil/scratch/weblinx/modeling/llama/dummy-cache", local_dir_use_symlinks=False)
