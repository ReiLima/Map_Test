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
path = 1600 * [[0]]

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

for contador in range(0,400):
    
    for y in range(0,400):

        arq.write(str (distance[contador][y]))
        arq.write("\n")



    
