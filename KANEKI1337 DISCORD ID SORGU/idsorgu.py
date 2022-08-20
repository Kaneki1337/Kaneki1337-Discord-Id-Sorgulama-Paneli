# KANEKI1337
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """ 

 -  KANEKI BABA ID SORGULAMA PANELI  -


""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [KANEKI1337] SORGULANCAK ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [KANEKI1337] TOKENININ İLK PARTI : {encodedStr}')
os.system('pause >nul') 
