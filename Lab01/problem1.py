import math
def isPalindrome(take):
	if len(take) == 0: return False
	else: 
		n = len(take)
		for i in range(math.floor(n/2)):
			if take[i] != take[n-1-i]:
				return False
		return True

fdata = open('input.txt')
fdata= fdata.read()
file=open('output.txt','w')
checker = {True:'a palindrome',False:'not a palindrome'}
evennumbers = []
oddnumbers = []
notpnumber = []
palindrome=[]
notPalindrom=[]
wordcheck = False
numCheck = False
data = fdata.split('\n')
l = len(data)
for item in data:
	myLine = None
	item = item.split(' ')
	lx ='.' in item[0]
	if lx:
		notpnumber.append(item[0])
		myLine = item[0]+" cannot have parity"
	else:
		data = int(item[0])% 2 == 0
		if data:
			evennumbers.append(int(item[0]))
			numCheck = True
		else:
			oddnumbers.append(int(item[0]))
			numCheck = False
	ispa = isPalindrome(item[1])
	if ispa:
		palindrome.append(item[1])
	else:
		notPalindrom.append(item[1])
	if myLine != None:
		file.write(f'{myLine} and {item[1]} is {checker[ispa]}\n')
	elif numCheck:
		file.write(f'{item[0]} has even parity and {item[1]} is {checker[ispa]}\n')
	else:
		file.write(f'{item[0]} has odd parity and {item[1]} is {checker[ispa]}\n')
rfile=open('records.txt','w')
rfile.write(f'Percentage of odd parity: {((len(oddnumbers)/l)*100)} %\n')
rfile.write(f'Percentage of even parity: {((len(evennumbers)/l)*100)} %\n')
rfile.write(f'Percentage of no parity: {((len(notpnumber)/l)*100)} %\n')
rfile.write(f'Percentage of palindrome: {((len(palindrome)/l)*100)} %\n')
rfile.write(f'Percentage of non-palindrome: {((len(notPalindrom)/l)*100)} %\n')