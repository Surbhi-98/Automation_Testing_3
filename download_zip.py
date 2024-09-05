# importing the requests module
import requests

print('Downloading started')
url = 'https://golang.org/dl/go1.17.3.windows-amd64.zip'

# Split URL to get the file name
filename = url.split('/')[-1]

# Downloading the file by sending the request to the URL
req = requests.get(url)
 
# Writing the file to the local file system
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')

# unzipped_file = zipfile.ZipFile("go1.17.3.windows-amd64.zip", "r")
