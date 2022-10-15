import sys
import math

# https://www.geeksforgeeks.org/hamming-code-implementation-in-python/
# https://github.com/danielmuthama/Hamming-Code/blob/master/hammingcode.py
# https://stackoverflow.com/questions/11243272/error-correcting-codes
# https://levelup.gitconnected.com/explaining-error-detection-and-correction-codes-with-python-be517596d42f

def adding_parity(binary_list,count):
	for i in range(count):
		binary_list.insert(pow(2,i) - 1,'0')
	return binary_list

def adding_parity2(binary_list,argv1,count):
	for i in range(count):
		binary_list.insert(pow(2,i) - 1, argv1[i])
	return binary_list

def xOR(located_position,new_size,temp,count,over,result,binary_list):
	while located_position < new_size:
		temp = int(temp)
		temp = int(binary_list[located_position]) ^ temp
		located_position = located_position + 1
		count -= 1
		if count == 0:
			located_position += over
			count = over
	result.append(str(temp))
	#print(result)
	return result


def check_second_parm(input1,temp,argv1):
	write_in_ascii_2 = bytes(input1, "ascii")
	#print (write_in_ascii_2)
	binary_string_2 = (' '.join('{0:08b}'.format(x) for x in write_in_ascii))
	binary_string_2 = ''.join(str(binary_string).replace(' ',''))
	binary_list_2  = list(binary_string_2)
	binary_list_2 = adding_parity2(binary_list_2,argv1,len(argv1))
	sizes = len(argv1)
	print(binary_list_2)
	byte_number = 8

	if binary_list_2[temp - 1] == '1':
		binary_list_2[temp - 1] ='0'
	else:
		binary_list_2[temp - 1] = '1'
	for i in range (sizes-1,-1,-1):
		binary_list_2.pop(pow(2,i)-1)

	count_bits = int(len(binary_list_2)/byte_number)
	for i in range (count_bits-1,-1,-1):
		binary_list_2.pop(byte_number*i)
	print("binary part:",binary_list_2)

	return binary_list_2

def check_first_parm (input1,final_result,argv1,length,temp):
	new_position = str(math.log2(temp))
	if new_position[-1] == '0' and new_position[-2] == '.':
		pos = math.log2(temp)

		res = list(argv1)
		if (argv1[int(pos)]) == '0':
			res[int(pos)] = '1'
		else:
			res[int(pos)] = '0' 
		return res
	else:
		b_list = check_second_parm(input1,temp,argv1)
		b_list = ''.join(str(b_list).split(','))
		b_list = ''.join(str(b_list).split('['))
		b_list = ''.join(str(b_list).split(']'))
		b_list = ''.join(str(b_list).split("'"))
		b_list = ''.join(str(b_list).replace(' ',''))
		
		print("letter part:",b_list)
		size_list = len(b_list)
		answer = ''
		for i in range (0,size_list,7):
			answer += chr(int(b_list[i:i+7],2))
		print(argv1)
		print(answer)
		return -1



input1 = (sys.argv[2])
write_in_ascii = bytes(input1, "ascii")
#print (write_in_ascii)


# https://stackoverflow.com/questions/29151181/writing-an-ascii-string-as-binary-in-python
# https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
binary_string = (' '.join('{0:08b}'.format(x) for x in write_in_ascii))
binary_string = ''.join(str(binary_string).replace(' ',''))
size = len(binary_string)
#print("The binary is",binary_string)
#print("The size is",size)
#2^(i-1) -1 = x
#2^ (i-1) = x + 1
#log2(x+1) = i-1
#[log2(x+1)]+1 = i
number_of_parity = (math.log2(size + 1))+1
number_of_parity = math.floor(number_of_parity)
#print("Need # parity:",number_of_parity)

#print(type(binary_string))
binary_list = list(binary_string)
#print(binary_list)
binary_list = adding_parity(binary_list,number_of_parity)
#print(binary_list)
new_size  = size + number_of_parity
#print("New size is",new_size)



result = []


for i in range (number_of_parity):
	located_position = pow(2,i)-1
	count = pow(2,i)
	over = count
	temp = 0
	xOR(located_position,new_size,temp,count,over,result,binary_list)
	#print(result)
#print(result)

result = ''.join(str(result).split(','))
result = ''.join(str(result).split('['))
result = ''.join(str(result).split(']'))
result = ''.join(str(result).split("'"))
final_result = ''.join(str(result).replace(' ',''))
print("The final output is",final_result)


argv1 = (sys.argv[1])
length = len(final_result)

if (argv1 ==  final_result):
	print(argv1)
	print(input1)
else:
	#check the length if they are different
	if len(final_result) != len(argv1):
		print("Incorrect inputs")

	# Scenario when argv[1] is incorrect and argv[2] is correct,
	# only change one bit in binary series
	else:
		temp = 0
		for i in range(length):
			if (final_result[i] != argv1[i]):
				temp += pow(2,i)
		res = check_first_parm(input1,final_result,argv1,length,temp)
		if (res == -1):
			sys.exit()
		else:
			res = ''.join(str(res).split(','))
			res = ''.join(str(res).split('['))
			res = ''.join(str(res).split(']'))
			res = ''.join(str(res).split("'"))
			res = ''.join(str(res).replace(' ',''))
			print(res)
			print(input1)

























