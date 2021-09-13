fname = open('input4.txt')
data = fname.read()
lex = data.split('\n')
l = int(lex[0])
rows,cols = (l,l)
A = [[0 for i in range(cols)] for j in range(rows)]
B = [[0 for i in range(cols)] for j in range(rows)]
C = [[0 for i in range(cols)] for j in range(rows)]
for i in range(1,l+1):
	data = lex[i].split(' ')
	for j in range(rows):
		A[i-1][j] = int(data[j])
for i in range(l+2,len(lex)):
	data = lex[i].split(' ')
	for j in range(rows):
		B[i-(l+2)][j] = int(data[j])
file=open('output4.txt','w')
for i in range(rows):
	for j in range(rows):
		for k in range(rows):
			C[i][j] += A[i][k]*B[k][j]
		file.write(str(C[i][j])+' ')
	file.write('\n')