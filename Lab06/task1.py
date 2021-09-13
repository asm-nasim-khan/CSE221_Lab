import  numpy as np
fhand = open('task1_input.txt','r')
data = fhand.read()
fhand.close()
value = data.split('\n')
size = int(value[0])
data_1=value[1]
data_2 = value[2]
zones_center = {'Y': 'Yasnaya',
                'P': 'Pochinki',
                'S': 'School',
                'R': 'Rozhok',
                'F': 'Farm', 
                'M': 'Mylta', 
                'H': 'Shelter',
                'I': 'Prison'}
def LCS(data_1,data_2):
    zone1 = {}
    zone2 = {}
    for i in range(len(data_1)):
        zone1[i+1] = data_1[i]
    for j in range(len(data_2)):
        zone2[j+1] = data_2[j]
    graph=np.zeros((len(data_2)+1,len(data_1)+1), dtype = int)
    for col in range(1,len(data_2)+1):
        for rows in range(1,len(data_1)+1):
            if zone1[rows] == zone2[col]:
                graph[col][rows] = (graph[col-1][rows-1]) + 1
            else:
                graph[col][rows] = max(graph[col-1][rows],graph[col][rows-1])
    row = len(data_1)
    cols = len(data_2)
    path=[]
    while(cols>0):
        while(row>0):
            if graph[cols-1][row]==graph[cols][row] and graph[cols][row-1]== graph[cols][row]:
                cols-=1
            elif graph[cols-1][row]==graph[cols][row]:
                cols-=1
            elif graph[cols][row-1] == graph[cols][row]:
                row-=1
            else:
                path.append(zone1[row])
                row-=1
                break
        cols-=1
    return path
path=LCS(data_1,data_2)
pen = open('output1.txt','w')
for items in range(len(path)-1,-1,-1):
        pen.write(f'{zones_center[path[items]]} ')
error=(len(path)/size)*100
pen.write(f'\nCorrectness of prediction: {int(error)}%')
pen.close()
