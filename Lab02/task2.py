def selection_sort(arr):
    for i in range(len(arr)):
        min_loc = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_loc]:
                min_loc = j
        temp = arr[i]
        arr[i] = arr[min_loc]
        arr[min_loc] = temp

file_opener=open("input2.txt")
file_opener=file_opener.read()
data = file_opener.split('\n')
counts = data[0].split(' ')
size = int(counts[0])
show = int(counts[1])
items = data[1].split(' ')
lst=[]
for item in items:
    lst.append(int(item))
selection_sort(lst)
Output_filer = open('output2.txt','w')
for item in range(show):
    Output_filer.write(str(lst[item])+' ')