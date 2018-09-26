'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
'''
string1 = 'AAAABBBCCDAA'
string2 = 'AABBAABBAABB'
string3 = 'aabbccdddcbbbbaabbc'

def successive(string):
	#create dict
	used_dict = dict()
	flag = 'x'
	for i in range(len(string)):
		if string[i] not in used_dict:
			used_dict[string[i]] = 1
		else:
			tmp = string[i]
			tmp += flag
			if string[i] != string[i - 1]:
				if tmp in used_dict:
					flag += 'x'
					tmp += 'x'
				used_dict[tmp] = 1
				
			else:
				if tmp in used_dict:
					used_dict[tmp] += 1
					continue
				else:
					used_dict[string[i]] += 1
				

	
	#loop to count
	result = ""
	for item in used_dict.items():
		char, num = item
		result += str(num)
		result += char[0]

	return result
	
print(successive(string1)) #---> 4A3B2C1D2A
print(successive(string2)) #---> 2A2B2A2B2A2B
print(successive(string3)) #---> 2a2b2c3d1c4b2a2b1c