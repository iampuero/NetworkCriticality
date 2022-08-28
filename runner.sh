#!/bin/bash
#BATCH --job-name=kuramoto
#SBATCH --output=slurm_out/output_%A.out
#SBATCH --mail-user=ignacio.ampuero@uv.cl
#SBATCH --mail-type=ALL
#SBATCH --time=1:00

eval "$(conda shell.bash hook)"
conda activate iampuero

time python $1

