### Steps to run the code
- Clone the webLinx repo and add our code (modelling directory under src)/ Clone our repo.
- Download complete webLinx dataset.
- Run the evaluation scripts per experiment.


The default configs (`llama/conf/config.yml`) assume that the `train.jsonl` is located at `./wl_data/candidates/train.jsonl`. If you want to change the path, you need to modify the `config.yml` accordingly.

### Set `WEBLINX_PROJECT_DIR`

You need to set the `WEBLINX_PROJECT_DIR` environment variable to the root directory of the WebLINX project. For example, if you have the following directory structure:

```bash
export WEBLINX_PROJECT_DIR=/path/to/the/modeling/directory/

# For example, if you are in the modeling directory, you can run:
export WEBLINX_PROJECT_DIR=$(pwd)
```


### Install the requirements
```bash
module load StdEnv/2020 gcc/9.3.0 arrow/13.0.0 rust/1.70.0 python/3.10.2 cudacore/.11.7.0
# then  pip install the following:

pip install transformers==4.35.0 lxml numpy datasets==2.14.0

pip install torch sentence-transformers peft backoff tensorboardX hydra-core peft

pip install accelerate optimum openai tiktoken trl 

# we want the gpu version of bitsandbytes

pip install bitsandbytes

pip install coloredlogs sacrebleu bert-score packaging ninja
```

Since `flash-attention` requires `torch` to be installed, we have to install it after everything else is properly installed.
```bash
# Regular install
pip install "flash-attn>=2.3.0"
# IF you have limited RAM, you can try this:
MAX_JOBS=4 pip install "flash-attn>=2.3.0" --no-build-isolation
# If you have issues with nvcc, try this:
FLASH_ATTENTION_SKIP_CUDA_BUILD=TRUE pip install "flash-attn>=2.3.0" --no-build-isolation
```


### Downloading data
- You can download the complete dataset as shown in the weblinx modelling [instructions](https://github.com/McGill-NLP/weblinx/tree/main/modeling) or refer to our instructions in the main [README](../README.md).
- We faced Internal Server Errors midway while downloading the webLinx dataset from huggingfacehub (even after multiple retries). To work around that, we downloaded the demos in parts.
- Also, since the dataset is huge and we only worked with text-only model so we excluded images and video demonstrations from our demo downloads.
- In our case, we had limitations on the home directory storage which is where the cache for huggingfacehub is stored. So, we downloaded demos with a different cache location and symlinks disabled (we had some intricate file sharing situation across user space on the cluster).
- Scripts which we used can be found here: [candidates, chats and data files](../scripts/data_process/get-data-scripts/get-cand-chat-data.py) and [demos](../scripts/data_process/get-data-scripts/get-test-demo-1.py).



### Compute Canada specific setup issues

A guide to setting up your compute Canada environment (credits to the author): https://prashp.gitlab.io/post/compute-canada-tut/


#### load pyarrow module
pyarrow is a package which contains dependencies for many other packages including datasets. These packages are needed for operations during training/ evaluation. pyarrow serves as the backend for data manipulation as it provides packages built on top of it with low level interface for handling data. 

compute Canada uses Gentoo Linux distro which needs none-any wheels (essentially purely python based files for executing stuff). pyarrow has optimisations from c++ bindings which need to be there in its wheel file which is needed to install the package on the distro. These were not available for latest versions online so we could build the wheel from source on Gentoo but we do not have sudo access and there were errors during build process which may or may not have been resolved using that access.

since pyarrow is so fundamental for other packages in ML that almost everyone will need it which is why they made it available as a module which we could load in our session and it would show up directly as package imported resolving dependencies for other packages.

#### submitting GPU jobs
An example:
```bash
#! /bin/bash
# ====================================
#SBATCH --job-name=Llama_1.3_eval
#SBATCH --cpus-per-task=6
#SBATCH --mem=48GB
#SBATCH --gres=gpu:1
#SBATCH --time=0-00:30
#SBATCH --output=./Eval_llama_1.3_eval_%j.out
#SBATCH --mail-user=aayush.kapur@mail.mcgill.ca
#SBATCH --mail-type=ALL
# ====================================

module load gcc/9.3.0 arrow/13.0.0 rust/1.70.0 python/3.10.2 cudacore/.11.7.0 

export WEBLINX_PROJECT_DIR=/home/kapmcgil/scratch/weblinx/modeling

cd /home/kapmcgil/scratch/weblinx/modeling

export CUDA_VISIBLE_DEVICES=0

# Finetune 1.3b variant
python -m llama.eval +variant="ft_1.3b" eval.split=valid

```