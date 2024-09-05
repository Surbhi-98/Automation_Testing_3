import subprocess
import os
#----------------------------------------Search a Particular file------------------------------------
def find_files(file_name, search_path):
  output = []
# Walking top-down from the root
  for root, dir, files in os.walk(search_path):
    if file_name in files:
      output.append(os.path.join(root, file_name))
  if output == []:
    return file_name + " Not Found"
  else:
    return output

print(find_files("first.py",'C:/Users/CBNITS'))

#----------------------------------------Search a Particular file in current working directory------------------------
# s = subprocess.run('cd /')
# cmd = 'dir sub.py /s /p'
# p = subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(p.stdout, p.stderr)
