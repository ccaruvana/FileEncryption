import os.path

encrypted = input("Please enter the file you wish to decrypt: ")
while (not os.path.exists(encrypted)):
	print("Whoops! That file doesn't seem to exist.")
	encrypted = input("Please enter the file you wish to decrypt: ")
key = input("Please enter the decryption key: ")
while (not os.path.exists(key)):
	print("Whoops! That file doesn't seem to exist.")
	key = input("Please enter the decryption key: ")

newFile = input("Would you like to output the decrypted text to a file? [y/n]: ")
while (newFile != "y" and newFile != "n"):
	newFile = input("Plese input a valid choice: y-yes, n-no: ")
if (newFile == "y"):
	override = 0
	while (override != '1'):
		outFile = input("Please input the name of the file you wish to write to: ")
		if (os.path.exists(outFile)):
			print("It seems that this file already exists. Do you wish to overwrite it?")
			override = input("'1' for overwrite | '0' to input new file name: ")
		else:
			override = str(1)

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

	if (newFile == "y"):
		output = open(outFile, "w")
		output.write(decrypted)
		output.close()
	else:
		print(decrypted)
