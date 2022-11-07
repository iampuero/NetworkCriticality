#!/bin/bash
#SBATCH --job-name=Crit
#SBATCH --output=slurm_out/output_%A.out
#SBATCH --time=8:00:00
#SBATCH -c 1


eval "$(conda shell.bash hook)"
conda activate iampuero

python $1 $2 $3 $4

