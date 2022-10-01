'''Attempt of solution of the puzzle by luan_brav0'''

import shutil
import zipfile
import os

# unzip_path = "C:\\GitHub\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise"

# shutil.unpack_archive('unzip_me_for_instructions.zip',unzip_path,'zip')
# with zipfile.ZipFile(unzip_path, 'r') as unziped_file:
    # unziping.extractall("C:\\GitHub\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions")

unzip_path = "C:\\Users\\luanm\\Documents\\GitHub\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise"
os.chdir(unzip_path)
print(os.getcwd())
for folder, sub_folders, files in os.walk(unzip_path):
    
    print("Folder: "+ folder)
    print('\n')
    # print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
        print('\n')
    
    
    print("Files: ")
    for f in files:
        print("\t File: "+f)
        print("Direcs: ", os.listdir())
        with open(f,'r') as file:
            print("Content: ", file.readline)  

    print('\n')

    