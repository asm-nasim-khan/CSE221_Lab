fhand = open('task1_input.txt','r')
data = fhand.read()
fhand.close()
value = data.split('\n')
size = int(value[0])
sorted_list = {}
selected_items = {}
arr = []
for i in range(1,size+1):
    temp = value[i].split()
    start = int(temp[0])
    finish = int(temp[1])
    sorted_list[finish] = start
    arr.append(finish)
arr2=sorted(arr)
count=0
for item in arr2:
    if count == 0:
        finish = item
        count+=1
        selected_items[sorted_list[item]] = item
    else:
        if sorted_list[item]>= finish:
            count+=1
            finish = item
            selected_items[sorted_list[item]] = item
pen = open('output1.txt','w')
pen.write(f'{count}\n')
for i in selected_items:
    pen.write(f'{i} {selected_items[i]}\n')
pen.close()