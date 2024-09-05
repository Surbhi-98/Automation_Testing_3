import os
# Get current Working Directory 
cwd = os.getcwd()
print("Current working directory:", cwd)

# Get List of all files and directory under given path
path = "/"
#dir_list = os.listdir(cwd)
dir_list = os.listdir(cwd) 
#print("Files and directories in '", path, "' :")
print("Files and directories in '", cwd, "' :") 
# print the list
print(dir_list)
# gives the name of the operating system dependent module imported
print(os.name)

#subprocess.run('dir', shell=True)