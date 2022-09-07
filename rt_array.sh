#!/bin/bash
#SBATCH --job-name=kuramoto
#SBATCH --output=slurm_out/output_%A.out
#SBATCH --mail-user=@iampueror
#SBATCH --mail-type=all
#SBATCH --time=1:00
#SBATCH -c 1


eval "$(conda shell.bash hook)"
conda activate iampuero

python $1 $SLURM_ARRAY_TASK_ID

