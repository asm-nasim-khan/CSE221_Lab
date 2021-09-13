def DFS_VISIT(graph,node):
    visited.append(node)
    printed.append(node)
    for point in graph[node]:
        if point not in visited:
            DFS_VISIT(graph,point)

def DFS(graph,endPoint):
    for point in graph:
        if point not in visited:
            DFS_VISIT(graph,point)
    for items in printed:
        Output_filer.write(items+' ')
        if items == endPoint:
            break

# Tester Class    
fhand = open('D:\\Books\\CSE221\\Lab\\8_19101623_3\\input1.txt')
fhand = fhand.read()
super_lst = fhand.split('\n')
MyDict = {}
for index in range(1,len(super_lst)):
    temp = super_lst[index].split()
    MyDict[temp[0]] = []
    for j in range(1,len(temp)):
        MyDict[temp[0]].append(temp[j])

visited = []
printed = []
Output_filer = open('D:\\Books\\CSE221\\Lab\\8_19101623_3\\output3.txt','w')
DFS(MyDict,'12')
Output_filer.close()