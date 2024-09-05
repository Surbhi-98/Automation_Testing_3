import os
import shutil

#-------------------------------------------Delete a particular file along with its parent folder----------------------------------
#Use os.path.basename() to extract the file name from the path string
#To extract the file name without the extension, use os.path.splitext()
#Use os.path.dirname() to extract the directory name (folder name) from the path string.As shown below
#Use os.path.split() to get both the file and directory (folder) name. os.path.split() returns a tuple of file name returned by os.path.basename() and directory name returned by os.path.dirname().
#Use os.path.splitext() to get the extension. os.path.splitext() splits the extension and others (root) and returns it as a tuple. The extension contains the dot 
#To create a path string with only the extension changed from the original, concatenate the first element of the tuple returned by os.path.splitext() with any extension.

def search_files(file_name, search_path):
  output = []
# Walking top-down from the root
  for root, dir, files in os.walk(search_path):
    if file_name in files:
      output.append(os.path.join(root, file_name))
  return output

def delete_file_folder(file_name, search_path):
  str=""
  result = search_files(file_name, search_path)
  for element in result: 
    str += element 
  print("Location of file " + file_name + "is" + str)
  dirname = os.path.dirname(str)
  print ("Directory path " + dirname)
  if os.path.exists(str):
    shutil.rmtree(dirname)
    # os.remove(str)
    return str + " Deleted Successfully along wit parent folder " + os.path.basename(dirname)
  else:
    return file_name + " The file does not exist"

#print(search_files())
print(delete_file_folder("test3.txt",'C:/Users/CBNITS'))
