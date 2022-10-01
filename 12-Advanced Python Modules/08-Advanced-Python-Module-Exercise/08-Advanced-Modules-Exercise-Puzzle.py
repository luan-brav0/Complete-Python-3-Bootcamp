'''Attempt of solution of the puzzle by luan_brav0'''

import shutil
import zipfile
import os
import re
import codecs

# unzip_path = "C:\\GitHub\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise"

# shutil.unpack_archive('unzip_me_for_instructions.zip',unzip_path,'zip')
# with zipfile.ZipFile(unzip_path, 'r') as unziped_file:
    # unziping.extractall("C:\\GitHub\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions")

unzip_path = "C:\\Users\\luanm\\Documents\\GitHub\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\extracted_content"
os.chdir(unzip_path)
print(os.getcwd())
rgx = r'\d{3}-\d{3}-\d{4}'

# with codecs.open('test.txt', 'r', encoding='utf-8', errors='ignore') as file:
#     phone = re.search(rgx, file.readline())
#     print("In: ", bool(phone))
#     # print("Line: ", file.readline())
#     print("Lines: ", file.readlines())



def is_phone_in_txt(unzip_path, rgx):
    phone_numbers_found = []
    for folder, sub_folders, files in os.walk(unzip_path):
        
        print("Folder: "+ folder.split("\\")[-1])
        print('\n')
        # print("THE SUBFOLDERS ARE: ")
        for sub_fold in sub_folders:
            print("\t Subfolder: "+sub_fold )
            print('\n')
        
        
        print("Files: ")
        for f in files:
            print("\t File: "+f)
            # print(sub_fold)
            # print(f)
            # print(os.getcwd())
            os.chdir(folder)
            # file_path = f"{unzip_path}\\{sub_fold}"
            with codecs.open(f,'r', encoding='utf-8', errors='ignore') as file:
                phone = re.search(rgx, file.readline())
                if bool(phone):
                    print ("Phone {} found at {} in folder {}".format(phone.group(), f, folder.split('\\')[-1]))
                    phone_numbers_found.append(phone.group())
               

        print('\n')

    return phone_numbers_found

print(is_phone_in_txt(unzip_path, rgx))

    