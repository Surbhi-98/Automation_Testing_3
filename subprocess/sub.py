import subprocess

def subprocess():
  output = subprocess.run('dir', shell=True)
  return output