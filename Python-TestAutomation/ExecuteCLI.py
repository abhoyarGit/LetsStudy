import os
import subprocess

#print(os.popen('dir').read())
print(os.popen('path').read())

print(os.system('path'))
return_value = subprocess.run("path", shell=True,stdout=subprocess.PIPE )
print(return_value.stdout)