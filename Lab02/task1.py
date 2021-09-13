def bubbleSort(arr):
    iterateCount = 0
    for i in range(len(arr)-1):
        swapCount = 0
        iterateCount +=1
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapCount +=1
        # loop controll condition to get O(n) for best case
        # if no swap happens it means the array is already sorted,
        # in that case break out of the loop
        if swapCount == 0: 
            break

file_opener=open("input1.txt")
file_opener=file_opener.read()
data = file_opener.split('\n')
size = int(data[0])
items = data[1].split(' ')
lst=[]
for item in items:
    lst.append(int(item))
bubbleSort(lst)
Output_filer = open('output1.txt','w')
for item in lst:
    Output_filer.write(str(item)+' ')


