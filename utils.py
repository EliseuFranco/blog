

ALLOWED_FILES = ["png",'jpg','jpg']

def check_file(file):
    return "." in file and file[file.index(".")+1:].lower() in ALLOWED_FILES

import os

print(os.environ.get('ps_data_base_url'))