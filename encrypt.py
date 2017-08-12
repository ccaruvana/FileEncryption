from random import randint
import os.path

toEncrypt = input("Please enter the file you wish to encrypt: ")
while (not os.path.exists(toEncrypt)):
	print("Whoops! That file doesn't seem to exist.")
	toEncrypt = input("Please enter the file you wish to encrypt: ")

override = 0
while (override != '1'):
	key = input("Please enter the desired name of the decryption key: ")
	if (os.path.exists(key)):
		print("It seems that this file already exists. Do you wish to overwrite it?")
		override = input("'1' for overwrite | '0' to input new file name: ")
	else:
		override = str(1)

override = 0
while (override != '1'):
	outFile = input("Please enter the desired name of the encrypted file: ")
	if (os.path.exists(outFile)):
		print("It seems that this file already exists. Do you wish to overwrite it?")
		override = input("'1' for overwrite | '0' to input new file name: ")
	else:
		override = str(1)

inF = open(toEncrypt, "r")
inputFile = inF.readlines()
inF.close()

length = 0
for line in inputFile:
	length += len(line)

inArr = []

for line in inputFile:
	for i in range(len(line)):
		inArr.append(int(ord(line[i])))

keyArr = []

for c in inArr:
	keyArr.append(randint(32,126))

keyF = open(key, "w")
for c in keyArr:
	keyF.write(chr(c))
keyF.close()

encrypted = []

for k in range(len(inArr)):
	encrypted.append(str(inArr[k]^keyArr[k]))

encrypted = '|'.join(encrypted)

output = open(outFile, "w")
output.write(encrypted)
output.close()
