import os 


def clearDirectory(dir):
    filelist = [f for f in os.listdir(dir) if f.endswith(".csv") ]
    for f in filelist:
        os.remove(os.path.join(dir, f))