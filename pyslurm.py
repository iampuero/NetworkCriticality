#!/usr/bin/env python3
from subprocess import check_output
from utils import getArg,getJobid

def run(command):
    out = int(check_output(command,shell=True,text=True))
    return out




dependency = "sbatch --dependency=afterok:{} {}".format

#start =
#end = 


