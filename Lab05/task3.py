fhand = open('task3_input.txt','r')
data = fhand.read()
fhand.close()
value = data.split('\n')
size = int(value[0])
s_list = value[1]
seq = value[2]
lst = s_list.split()
lst = [int(x) for x in lst]
paths = []
arr = sorted(lst)
stack = []
hours_list = [0,0] # Jack = 0 index ; Jill = 1 index
index = 0
for items in seq:
    if items == 'J':
        stack.append(arr[index])
        hours_list[0]+=arr[index]
        paths.append(arr[index])
        index += 1
    elif items == 'j':
        temp = stack.pop()
        hours_list[1]+=temp
        paths.append(temp)
pen = open('output3.txt','w')
for items in paths:
    temp = str(items)
    pen.write(temp)
pen.write('\n')
pen.write(f'Jack will work for {hours_list[0]} hours\n')
pen.write(f'Jill will work for {hours_list[1]} hours')
pen.close()
