import os
#By Providing the host name as a parameter
# def myping(host):
#   response = os.system("ping " + host)
#   #The method returns 0 if the command executes without any error. 
#   if response == 0:
#     return True
#   else:
#     return False

# print(myping("www.google.com"))

#By Giving the host name inside the method
def myping():
  host = "www.google.com"
  response = os.system("ping " + host)
  #The method returns 0 if the command executes without any error. 
  if response == 0:
    return True
  else:
    return False

def mynetstat():
  response = os.system("netstat "+"-n")
  if response == 0:
    return True
  else:
    return False

print(myping())  
print(mynetstat())  