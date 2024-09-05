import subprocess
# from subprocess import run
# from sys import stderr, stdout
#--------------------------------To use subprocess.run--------------------------------------------
# cmd = 'ping www.google.com'
# s = subprocess.run(cmd, shell=True, universal_newlines=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(s.stdout, s.stderr)
# print('exit status code:', s.check_returncode())
# --------------------------------To use subprocess.Popen--------------------------------------------
p = subprocess.Popen(['ping', 'www.google.com'], shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(p.stdout, p.stderr, p.communicate()[0])
print(p.returncode)
print('exit status/return code:', p.returncode)
