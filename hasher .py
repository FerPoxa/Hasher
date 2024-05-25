import requests
import json

def print_hasher():
	letra_h = "\033[94mH   H\nH   H\nHHHHH\nH   H\nH   H\n"
	letra_a = "AAAAA\nA   A\nAAAAA\nA   A\nA   A\n"
	letra_s = " SSSS\nS    \n SSSS\n    S\nSSSS \n"
	letra_e = "EEEEE\nE    \nEEEEE\nE    \nEEEEE\n"
	letra_r = "RRRR \nR   R\nRRRR \nR R  \nR  R \n"

	word = [letra_h, letra_a, letra_s, letra_h, letra_e, letra_r]

	for i in range(5):
		for letter in word:
			line = letter.split('\n')
			print(line[i], end='  ')
		print()
try:
	def hash_lookup():
		to_curl="https://hashlookup.circl.lu/lookup/"
		print("|-------------------------------------|")
		print("|\t   1->MD5                     |")
		print("|\t   2->SHA-256                 |")
		print("|\t   3->SHA-1                   |")
		print("|\t   4->SSDEEP                  |")
		print("|\t   5->TLSH                    |")
		print("|-------------------------------------|")
		select=int(input("Select your type of hash:"))
		if (select == 1):
			to_curl+='md5/'
		elif (select == 2):
			to_curl = to_curl+'sha256/'
		elif (select == 3):
			to_curl+='sha1/'
		elif (select == 4):
			to_curl=to_curl+'ssdeep/'
		elif (select == 5):
			to_curl+='tlsh/'
		to_curl+=input("Enter hash to lookup:")
		mycurl=requests.get(to_curl, headers = {"accept": "application/json"})
		#131312A96CAD4ACAA7E2631A34A0D47C
		info=dict(json.loads(mycurl.text))
		print('Name of hashed file: '+info.get('FileName'))
		print('Size of hashed file: '+info.get('FileSize'))
		print('App type: '+info['ProductCode']['ApplicationType'])
	print_hasher()
	print ("\033[0m")
	hash_lookup()
except TypeError:
	print("The hash entered was not found") 
except ValueError:
	print("Enter a valid value")