from subprocess import call


for i in range(1000,1,-1): # i = 1000, then i = 999 ....

	shell = call("tar -xvf "+str(i)+".tar", shell=True)f # extract tar file by calling this bash command
  
print("Finished")
