# -*- coding: cp1252 -*-
import cv2
import numpy as np

arq = open("Dist.txt","w")

def dist(startx, starty, finalx, finaly):
    
    distx = ((startx - finalx) ** 2)
    disty = ((starty - finaly) ** 2)
    dist = (distx + disty) ** 0.5
    
    return dist

Color_List = 400*[[0]]

for contador in range(0,400):
    Color_List[contador] = 400*[[0,0,0]]

img = cv2.imread('Maptest.png')
table = 400*[[0]]
distance = 400*[[0]]
path = 1600 * [[0,0]]

for contador in range(0,400):
    
    for y in range(0,400):
        
        Color_List[y][contador] = img[contador,y]
        
    table[contador] = 400*[[0]]
    distance[contador] = 400*[[0]]
    
for contador in range(0,400):
    
    for y in range(0,400):
        
        if(np.all(Color_List[contador][y]) == 0):
            table[contador][y] = ['0']
            
        if(np.all(Color_List[contador][y] == 255)):
            table[contador][y] = ['1']

        if(np.any(Color_List[contador][y] == 36)):
            table[contador][y] = ['2']


celula = raw_input("Digite as coordenadas iniciais: ")
startcell_ = celula.split(",")

startcell = 2*[0]

startcell[0] = int(startcell_[0])
startcell[1] = int(startcell_[1])

endcell = 2*[0]

celula = raw_input("Digite as coordenadas finais: ")
endcell_ = celula.split(",")
endcell[0] = int(endcell_[0])
endcell[1] = int(endcell_[1])

if table[endcell[0]][endcell[1]] == ['0'] or table[startcell[0]][startcell[1]] == ['0']:
     print("Celula Invalida!")

else:
    
    for contador in range(0,400):
    
        for y in range(0,400):
            

            if table[contador][y] == ['0']:
                distance[contador][y] = 1000

            else:

                distance[contador][y] = dist(contador, y, endcell[0], endcell[1])

for contador in range(0, 389):
    
        for y in range(0,389):

            for c in range(0,10):
                if table[contador + c][y] == ['0'] or table[contador][y + c] == ['0']:
                    distance[contador][y] = 1000


for contador in range(0,400):
    
    for y in range(0,400):

        arq.write(str (distance[contador][y]))
        arq.write("\n")

start_x = startcell[0]
start_y = startcell[1]

cond = 4 * [[0]]
cond[0] = start_x + 1
cond[1] = start_x - 1
cond[2] = start_y + 1
cond[3] = start_y - 1

dist_table = 4 * [[0]]

for i in range(0, 1600):
    aux = 1000
    count = 0
    
    dist_table[0] = distance[cond[0]][start_y]
    dist_table[1] = distance[cond[1]][start_y]
    dist_table[2] = distance[start_x][cond[2]]
    dist_table[3] = distance[start_x][cond[3]]

    for j in range(0, 4):
        if dist_table[j] < aux:
            aux = dist_table[j]
            count = j

    if aux == 0:
        break;

    if count == 0:
        start_x = cond[0]
    if count == 1:
        start_x = cond[1]
    if count == 2:
        start_y = cond[2]
    if count == 3:
        start_y = cond[3]

    path[i] = [start_x, start_y]

    print path[i]
        

