#!/usr/bin/env python3
from subprocess import check_output
from utils import getArg,getJobid

def run(command):
    out = int(check_output(command,shell=True,text=True))
    return out

base = "sbatch --parsable"
dependency = " --dependency=afterok:{jobid} "
array=" --array={start}-{finish}%{maxjobs} "
name = "-J {name}"


