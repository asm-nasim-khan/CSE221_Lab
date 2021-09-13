import numpy as np
import math
from queue import PriorityQueue
def Network(Graph, source):
    distance = [-math.inf]*(len(Graph))
    distance[source] = math.inf
    prev = [None]*(len(Graph))
    Queue = PriorityQueue()
    visited = [False]*(len(Graph))
    for v in range(len(Graph)):
        Queue.put((-distance[v], v))
    while not Queue.empty():
        # print(list(Queue.queue))
        temp = Queue.get()
        # print(temp)
        u = temp[1]
        if visited[u]:
            continue
        visited[u] = True
        for v in range(1, len(Graph[u])):
            if Graph[u][v] == 0:
                continue
            alt = min(distance[u], Graph[u][v])
            if alt > distance[v]:
                distance[v] = alt
                prev[v] = u
                Queue.put((-distance[v], v))
    for i in range(len(distance)):
        if distance[i] == -math.inf:
            distance[i] = -1
        if distance[i] == math.inf:
            distance[i] = 0
    return distance, prev


fhand = open('input4.txt','r')
fhand = fhand.read()
data = fhand.split('\n')
size = int(data[0])
n = 1
pen = open('output4.txt','w')
for i in range(size):
    value = data[n].split()
    place = int(value[0])
    edge = int(value[1])
    graph = np.zeros((place+1, place+1), dtype=int)
    nextSource = n + edge + 1
    source = int(data[nextSource])
    for j in range(n+1, nextSource):
        lst = data[j].split()
        graph[int(lst[0])][int(lst[1])] = int(lst[2])
    n = nextSource+1
    # print(graph)
    lst1, lst2 = Network(graph, source)
    for ite in range(1,len(lst1)):
        items = lst1[ite]
        pen.write(str(items)+' ')
    pen.write('\n')
pen.close()