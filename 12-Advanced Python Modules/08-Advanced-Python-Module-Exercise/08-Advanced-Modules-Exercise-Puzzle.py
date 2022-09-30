'''Attempt of solution of the puzzle by luan_brav0'''

from shutil import unpack_archive
import zipfile

unzip_path = "C:\\GitHub\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions.zip"

# unpack_archive('unzip_me_for_instructions.zip','','zip')
with zipfile.ZipFile(unzip_path, 'r') as unziping:
    unziping.extractall("C:\\GitHub\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions")