#!/usr/bin/python3

import os

a = "/home"
os.chdir(a)
user = os.listdir() #collect user folder

folpath = [] #where to store user folder content path
filepath = [] 


def filecol(fdlist, fol1, file) :
	for path in fdlist :
		os.chdir(path) 
		content2 = os.listdir()
		for item in content2 :
			if os.path.isfile(item) :
				file.append(os.path.abspath(item))

			else :
				folderpath = os.path.abspath(item)
				fol1.append(folderpath)

# maybe i should assemble both of the filecol func, but idk how :P

def filecol2(folpath,filepath) :
	for folder in folpath :
		child = os.listdir(folder)
		if len(child) == 0 : #remove empty folder from list
			folpath.remove(folder)
			print(folder, "removed")

		for content in child :
			abpath = f'{os.path.abspath(folder)}/{content}'

			if "filecol.py" in abpath :
				print("DONT MESS WITH IT")
				continue

			if os.path.isfile(abpath) :
				filepath.append(abpath)

			else :
				folpath.append(abpath)

#i think the reason why i don't need a recursive function is because i append the folder path and it makes everysingle folder in this machine would be added 
#how lucky i am :DD

#unnecessary write check

filecol(user, folpath,filepath)

filecol2(folpath,filepath)

print(folpath)
print(filepath)
print("panjang folpath",len(folpath))
print("panjang filepath", len(filepath))
