import os.path

encrypted = input("Please enter the file you wish to decrypt: ")
while (not os.path.exists(encrypted)):
	print("Whoops! That file doesn't seem to exist.")
	encrypted = input("Please enter the file you wish to decrypt: ")
key = input("Please enter the decryption key: ")
while (not os.path.exists(key)):
	print("Whoops! That file doesn't seem to exist.")
	key = input("Please enter the decryption key: ")

fA = open(encrypted,"r")
fB = open(key,"r")
encF = fA.readlines()
keyF = fB.readlines()
fA.close()
fB.close()

encArr = []
keyArr = []

for line in encF:
	encArr.extend(line.split("|"))
encArr = list(map(int,encArr))

for line in keyF:
	for i in range(len(line)):
		keyArr.append(int(ord(line[i])))

if (len(encArr) != len(keyArr)):
	print("A serious error occurred! The two files are different lengths!")
else:
	decrypted = []
	for k in range(len(encArr)):
		decrypted.append(chr(encArr[k]^keyArr[k]))
	decrypted = ''.join(decrypted)

	print(decrypted)
