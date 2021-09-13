def merge(arr,l,mid,r):
    n1 = mid -l + 1
    n2 = r - mid
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[mid + 1 + j]
    i,j,k=0,0,l
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    if i<n1 or j<n2:
        if i<n1:
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
        else:
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1
            
    return arr
        
def merge_sort(arr,l,r):
    if l<r:
        mid = (l+(r-1))//2
        A1=merge_sort(arr,l,mid)
        A2=merge_sort(arr,mid+1,r)
        D = merge(arr,l,mid,r)
        return D


file_opener=open("input4.txt")
file_opener=file_opener.read()
data = file_opener.split('\n')
size = int(data[0])
items = data[1].split(' ')
lst=[]
for item in items:
    lst.append(int(item))
P = merge_sort(lst,0,(len(lst)-1))
Output_filer = open('output4.txt','w')
for item in lst:
    Output_filer.write(str(item)+' ')