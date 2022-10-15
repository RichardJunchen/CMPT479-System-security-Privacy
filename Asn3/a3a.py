import sys
import math

def adding_parity(binary_list,count):
	for i in range(count):
		binary_list.insert(pow(2,i) - 1,'0')
	return binary_list

def xOR(located_position,new_size,temp,count,over,result,binary_list):
	while located_position < new_size:
		temp = int(temp)
		temp2 = int(binary_list[located_position])
		count -=1
		temp = temp ^ temp2
		located_position = located_position + 1
		if count == 0:
			located_position += over
			count = over
	ans = str(temp)
	result.append(ans)
	print(result)
	return result

input1 = (sys.argv[1])
write_in_ascii = bytes(input1, "ascii")
print (write_in_ascii)


# https://stackoverflow.com/questions/29151181/writing-an-ascii-string-as-binary-in-python
# https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
binary_string = (' '.join('{0:08b}'.format(x) for x in write_in_ascii))
binary_string = ''.join(str(binary_string).replace(' ',''))
size = len(binary_string)
print("The binary is",binary_string)
print("The size is",size)
#2^(i-1) -1 = x
#2^ (i-1) = x + 1
#log2(x+1) = i-1
#[log2(x+1)]+1 = i 5.012
number_of_parity = (math.log2(size + 1))+1
number_of_parity = math.floor(number_of_parity)
print("Need # parity:",number_of_parity)

#print(type(binary_string))
binary_list = list(binary_string)
#print(binary_list)
binary_list = adding_parity(binary_list,number_of_parity)
print(binary_list)
result = []
new_size  = size + number_of_parity
print("New size is",new_size)

for i in range (number_of_parity):
	located_position = pow(2,i)-1
	count = pow(2,i)
	over = count
	temp = 0
	xOR(located_position,new_size,temp,count,over,result,binary_list)
	#print(result)
print(result)

result = ''.join(str(result).split(','))
result = ''.join(str(result).split('['))
result = ''.join(str(result).split(']'))
result = ''.join(str(result).split("'"))
final_result = ''.join(str(result).replace(' ',''))
print(final_result)




