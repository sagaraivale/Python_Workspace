import os
import glob
import config

config.RULES_PATH
config.CONTENT_REPO

fileList = []


def absPath():

    files1 = glob.glob("**/**/**/**/plugins/*.py")  # WORKING FINE
    for var1 in files1:
        fileList.append(os.path.abspath(var1))

    files2 = glob.glob("**/**/**/**/**/plugins/*.py")
    for var2 in files2:
        fileList.append(os.path.abspath(var2))
   
    return fileList

