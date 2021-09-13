def BFS (visited, graph, node, endPoint):
   visited.append(node)
   queue.append(node)
   while queue:
       m = queue.pop(0)
       Output_filer.write(m+' ')
       if m == endPoint:
           break
       for neighbour in graph[m]:
           if neighbour not in visited:
               visited.append(neighbour)
               queue.append(neighbour)

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
visited =[]
queue =[]
Output_filer = open('D:\\Books\\CSE221\\Lab\\8_19101623_3\\output2.txt','w')
BFS (visited,MyDict,'1','12')
Output_filer.close()