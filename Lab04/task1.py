import numpy as np
import math
from queue import PriorityQueue
def Dijkstra(Graph,source):
    distance = [math.inf]*(len(Graph))
    distance[source] = 0
    prev = [None]*(len(Graph))
    Queue = PriorityQueue()
    visited = [False]*(len(Graph))
    for v in range(len(Graph)):
        Queue.put((distance[v],v))
    while not Queue.empty():
      temp = Queue.get()
      u = temp[1]
      if visited[u]:
          continue
      visited[u] = True
      for v in range(1,len(Graph[u])):
          if Graph[u][v] == 0:
              continue
          alt = distance[u] + Graph[u][v]
          if alt < distance[v]:
              distance[v] = alt
              prev[v]=u
              Queue.put((distance[v],v))
    return distance,prev

    
fhand = open('input1.txt','r')
fhand = fhand.read()
data = fhand.split('\n')
size = int(data[0])
n = 1
pen = open('output1.txt','w')
for idx in range(0,size):
    values = data[n].split()
    places = int(values[0])
    graph=np.zeros((places+1,places+1), dtype = int)
    edge = int(values[1])
    n +=1
    for idy in range(edge):
        lst = data[n].split()
        n+=1
        graph[int(lst[0])][int(lst[1])] = int(lst[2])
        graph[int(lst[1])][int(lst[0])] = int(lst[2])
    lst1,lst2=Dijkstra(graph,1)
    pen.write(str(lst1[-1])+'\n')
pen.close()