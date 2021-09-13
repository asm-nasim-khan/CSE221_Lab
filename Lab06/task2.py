import  numpy as np
fhand = open('task2_input.txt','r')
data = fhand.read()
fhand.close()
value = data.split('\n')
data_1=value[0]
data_2 = value[1]
data_3 = value[2]
def LCS(data_1,data_2,data_3):
    zone1 = {}
    zone2 = {}
    zone3 = {}
    for i in range(len(data_1)):
        zone1[i+1] = data_1[i]
    for j in range(len(data_2)):
        zone2[j+1] = data_2[j]
    for k in range(len(data_3)):
        zone3[k+1] = data_3[k]
    graph=np.zeros((len(data_2)+1,len(data_1)+1,len(data_3)+1), dtype = int)
    for col in range(1,len(data_2)+1):
        for rows in range(1,len(data_1)+1):
            for z in range(1,len(data_3)+1):
                if zone1[rows] == zone2[col] and zone1[rows] == zone3[z]:
                    graph[col][rows][z] = (graph[col-1][rows-1][z-1]) + 1
                else:
                    if graph[col-1][rows][z] >= (graph[col][rows-1][z]):
                        maximum = graph[col-1][rows][z]
                        if maximum>= graph[col][rows][z-1]:
                            graph[col][rows][z] = maximum
                        else:
                            maximum = graph[col][rows][z-1]
                            graph[col][rows][z] = maximum
                    else:
                        maximum = graph[col][rows-1][z]
                        if maximum>= graph[col][rows][z-1]:
                            graph[col][rows][z] = maximum
                        else:
                            maximum = graph[col][rows][z-1]
                            graph[col][rows][z] = maximum
    return graph[len(data_2)][len(data_1)][len(data_3)]
n =LCS(data_1,data_2,data_3)
pen = open('output2.txt','w')
pen.write(str(n))
pen.close()