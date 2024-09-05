import subprocess

s = subprocess.run('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
print(s.stdout, s.stderr)