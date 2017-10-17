import glob
import re

directory_key = []
directory_key_main = []


def directory_call():
    lines1 = glob.glob("diag-insights-content/content/**/**/**")
    for each_line in lines1:
        find = re.search(r'\.*\/.*\/(.*)', each_line)
        directory_key.append(find.group())
    
    for var2 in directory_key:
        if var2.isupper():
            directory_key_main.append(var2)

    lines2 = glob.glob("diag-insights-content/content/**/satellite/**/**")
    for each_line in lines2:
        find = re.search(r'\.*\/.*\/.*\/(.*)', each_line)
        directory_key_main.append(find.group())
   return directory_key_main
