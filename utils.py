from sys import argv
from os import environ,listdir

def getArg(argIndex,format=str,default=""):
    try:
        return format(argv[argIndex])
    except:
        return None

def getJobId(arrayjob=False):
    if not arrayjob:
        return int(environ["SLURM_JOB_ID"])
    return int(environ["SLURM_ARRAY_JOB_ID "])

def getTaskId():
    try:
        return int(environ["SLURM_ARRAY_TASK_ID"])
    except:
        return None

def checkFile(filename,folder=""):
    return filename in listdir(folder)

