#! /bin/bash
# ====================================
#SBATCH --job-name=get_data_remaining_1_2
#SBATCH --cpus-per-task=4
#SBATCH --mem=16GB
#SBATCH --time=0-03:59
#SBATCH --output=./get_data_remaining_1_2_%j.out
#SBATCH --mail-user=aayush.kapur@mail.mcgill.ca
#SBATCH --mail-type=ALL
# ====================================
module load StdEnv/2020 gcc/9.3.0 arrow/13.0.0 rust/1.70.0 python/3.10.2 cudacore/.11.7.0
cd /home/kapmcgil/scratch/weblinx/modeling
python /home/kapmcgil/scratch/weblinx/modeling/wl_data/get-test-demo-1.py > get_data_remaining_1.out
python /home/kapmcgil/scratch/weblinx/modeling/wl_data/get-test-demo-2.py > get_data_remaining_2.out
