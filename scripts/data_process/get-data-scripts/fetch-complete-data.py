from huggingface_hub import snapshot_download
# # splits.json
# snapshot_download(
#     repo_id="McGill-NLP/WebLINX-full", repo_type="dataset", allow_patterns="splits.json", local_dir="./wl_data/"
# )
# # candidates files
# snapshot_download(
#     repo_id="McGill-NLP/WebLINX-full",
#     repo_type="dataset",
#     allow_patterns="candidates/*.jsonl",
#     local_dir="./wl_data/"
# )
# snapshot_download(repo_id="McGill-NLP/WebLINX-full", repo_type="dataset", ignore_patterns=["*.png", "*.mp4"], local_dir="./wl_data/")

snapshot_download(repo_id="McGill-NLP/WebLINX-full", repo_type="dataset", local_dir="./wl_data", allow_patterns="candidates/*.jsonl")
snapshot_download(repo_id="McGill-NLP/WebLINX-full", repo_type="dataset", local_dir="./wl_data", allow_patterns="chat/*.csv")
snapshot_download(repo_id="McGill-NLP/WebLINX-full", repo_type="dataset", local_dir="./wl_data", allow_patterns="data/*.csv")