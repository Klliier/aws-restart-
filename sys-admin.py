import os
import subprocess

#list(ls) the files in directory using single string arguments
#both will perform same function
#The subprocess.run() function is powerful because you can use it to run any Bash command.
os.system("ls") 
subprocess.run(["ls"])

#list(ls) the files in directory using double string arguments in subprocess.run()
#-l shows the user permission, saved directory, file size, date, time and file name
subprocess.run(["ls", "-l"])

#using triple arguments in subprocess.run()
#third argument will be file name
#it shows only the properties of given file
subprocess.run(["ls","-l","datatype.py"])



#uname command to get system information.
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#df command to get disk information
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])