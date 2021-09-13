def insertion_sort(arr,id):
    for i in range(len(arr)-1):
        temp = arr[i+1]
        tmp2 = id[i+1]
        j=i
        while j>=0:
            if arr[j]<temp: 
                arr[j+1]= arr[j]
                id[j+1] = id[j]
            else: break
            j -=1
        arr[j+1] = temp
        id[j+1] = tmp2
        
file_opener=open("input3.txt")
file_opener=file_opener.read()
data = file_opener.split('\n')
size = int(data[0])
item1 = data[1].split(' ')
item2= data[2].split(' ')
ID=[]
Marks=[]
for item in item1:
    ID.append(int(item))
for item in item2:
    Marks.append(int(item))
insertion_sort(Marks,ID)
Output_filer = open('output3.txt','w')
for item in ID:
    Output_filer.write(str(item)+' ')