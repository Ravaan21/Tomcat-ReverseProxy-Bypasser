import os
host = input("Enter your host \n Ex:https://victim.com : ")
path = input("Enter path to TomcatTraversalMap.txt : ")
print("Selected host = " + host)
print("Selected path = " + path)
print("Cooking Logic.... Please Wait...")
cmd = "dirb " + host + " " + path + " " + '-N 400 -r >> TomReverse.txt ; cat TomReverse.txt | grep "..;"'
execution = os.system(cmd)
print(execution)
