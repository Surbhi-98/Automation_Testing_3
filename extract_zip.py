# importing necessary modules
import zipfile
from io import BytesIO
import os
#import shutil

#---------------------------Extract File using Expand-Archive command------------------------
# print('File Extraction started')
# os.system('powershell.exe Expand-Archive -Path go1.17.3.windows-amd64.zip -DestinationPath C:/Users/CBNITS/unzip_file/')
# print('File Extraction completed')

#---------------------------Extract File using unzip command------------------------
#we have to run the command in git bash terminal because unzip command is not a builtin command in window. so we use bash shell to execute the command.
print('File Extraction started')
# os.system('unzip -l subprocess.zip | find . -name sub.py')
os.system('unzip -l go1.17.3.windows-amd64.zip | find -name semi5.go')
print('File Extraction completed')

#--------------------------Extract File using zipfile module-------------------------- 
#print('File Extraction started')
#cwd = 'extacted_file'
# with zipfile.ZipFile('go1.17.3.windows-amd64.zip', 'r') as zip_ref:
#   zip_ref.extractall(cwd)
#print('File Extraction completed')


#--------------------------Extract File using shutil module-------------------------- 
## Extract all files in the single_zip.zip file to your home folder.
#shutil.unpack_archive('go1.17.3.windows-amd64.zip', '~')