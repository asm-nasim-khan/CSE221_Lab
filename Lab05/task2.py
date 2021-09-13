fhand = open('task2_input.txt','r')
data = fhand.read()
fhand.close()
value = data.split('\n')
app = value[0].split()
size = int(app[0])
person = int(app[1])
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
item = 0
finish_time = [0]*person
while(item<len(arr2)):
    if count == 0:
        for index in range(person):
            finish_time[index] = arr2[item]
            item +=1
        count+=person
    else:
        for index in range(person):
            if sorted_list[arr2[item]]>= finish_time[index]:
                finish_time[index] = arr2[item]
                count+=1
        item +=1
pen = open('output2.txt','w')
pen.write(f'{count}')
pen.close()