from sys import argv
from os import environ


def getArg(argIndex,format=str,default=""):
    try:
        return format(argv[argIndex])
    except:
        return None

def getJobid():
    return environ["SLURM_JOBID"]