import re
import path
import content_directory

list_of_files = []
list_of_errorkeys = []
directory = []
directory_exists = []
directory_not_exists = []


def parameter_extraction():
    list_of_files = path.absPath()
    for var_files in list_of_files:
        f = open(var_files, 'rU')
        errorkey = re.findall(r'ERROR_KE.* = [\"\']([\w\s]+)[\'\"]', f.read())
        for Key in errorkey:
            list_of_errorkeys.append(Key)

    directory = content_directory.directory_call()
    for var1 in list_of_errorkeys:
        if var1 in directory:
            directory_exists.append(var1)
        else:
            directory_not_exists.append(var1)

    print "LIST OF DIRECTORY EXIST\n"
    for exist in directory_exists:
        print exist
    print "\nTotal Directory Exist  ", len(directory_exists)

    print "\nLIST OF DIRECTORY NOT_EXIST\n"
    for non_exist in directory_not_exists:
        print non_exist
    print "\nTotal Directory Non Exist  ", len(directory_not_exists)

parameter_extraction()
