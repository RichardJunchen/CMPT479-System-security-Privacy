import random
import sys
import os
import time
import subprocess

def write_file(msg):
	f = open("check_r_or_yN","wb")
	f.write(msg)
	f.close

def check_valid(myRandomBlock):
	write_file(bytes(myRandomBlock))

	res = subprocess.check_output('python3 oracle.py check_r_or_yN',shell=True)
	#print(res[0])
	if res[0] == 0:
		return False
	elif res[0] == 1:
		return True




#START
f = open(sys.argv[1],"rb")	
ciphertext = f.read()
f.close()

seprated_block_ciphertext = []
size_ciphertext = len(ciphertext)/16

for i in range(int(size_ciphertext)):
	temp = []
	for j in range(16):
		temp.append(ciphertext[i*16+j])
		#print(temp)

	seprated_block_ciphertext.append(bytearray(temp))
	
#print(seprated_block_ciphertext)

#~~~~~~~~Decrypt byte~~~~~~~~~~~~~~~~~
size_random_block = 15
random_block = bytearray(os.urandom(size_random_block))
random_block.append(0)

print(random_block)
#print(seprated_block_ciphertext[-1])
#print(seprated_block_ciphertext[0])

# add at the end of random block
for i in range(len(seprated_block_ciphertext[-1])):
	random_block.append(seprated_block_ciphertext[-1][i])
print(random_block)


#4	
for j in range (256):
	if not check_valid(random_block):
		if j < 255:
			random_block[15] +=1
		else:
			break

#3
total = 0
for i in range(15):
	new_r = bytearray(os.urandom(1))[0]
	while new_r ==random_block[i]:
		new_r = bytearray(os.urandom(1))[0]
	random_block[i] = new_r
	if (check_valid(random_block)):
		total +=1
	else:
		break



d_yN = []
xN = []
i = random_block[15]
d_yN.append(i ^ total)
print(i)
#print(seprated_block_ciphertext)
#last_byte_of_yN = bytes(d_yN_[0])^ bytes(seprated_block_ciphertext[-2][-1])

#7
last_byte_of_yN = d_yN[0]^ seprated_block_ciphertext[-2][-1] 
#print(the_last_byte_of_yN)
xN.append(last_byte_of_yN)
#print(xN)



#~~~~~~~~~Decrypt block~~~~~~~~~~~ not finish, just some idea and some pseudocode below:
for i in range(15):
	
	temp = bytearray()
	for j in range (15-i):
		temp.append(random_block[j])
	temp.append(0)
	
		
# check padding oracle	
	for k in range (256):
		if not check_valid(temp):
			if k < 255:
				temp[15] +=1
			else:
				break

	d_yN_K = temp[-1] ^ (k-1)
	
	current_xN = currend_D_yN_k ^ seprated_block_ciphertext[0][k-1]
	
	
	
	xN.insert(0,current_xN)
	
	
	
final_answer = ""


#print(final_answer)



