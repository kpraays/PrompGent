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
