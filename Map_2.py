# -*- coding: cp1252 -*-
import cv2
import numpy as np

arq = open("Dist.txt", "w")

lista = 400*[[0]]
table = 400*[[0]]
path = 1600*[[0,0]]

for i in range(0,400):
    lista[i] = 400*[[0,0,0]]
    table[i] = 400*[[0]]

img = cv2.imread('Map1.png')

for i in range(0,400):
    
    for j in range(0,400):
        lista[j][i] = img[i,j]

for i in range(0,400):
    ##arq.write("\n")
    for j in range(0,400):
        if(np.all(lista[i][j]) == 0):
            table[i][j] = ['0']
            
        if(np.all(lista[i][j] == 255)):
            table[i][j] = ['1']

        if(np.any(lista[i][j] == 36)):
            table[i][j] = ['2']

        ##arq.write(str(table[contador][y]))
        ##arq.write(" ")

data_input = raw_input("Digite as coordenadas iniciais: ")
startcell = data_input.split(",")
startcell[0] = int(startcell[0])
startcell[1] = int(startcell[1])

data_input = raw_input("Digite as coordenadas finais: ")
endcell = data_input.split(",")
endcell[0] = int(endcell[0])
endcell[1] = int(endcell[1])

if table[endcell[0]][endcell[1]] == ['0'] or table[startcell[0]][startcell[1]] == ['0']:
     print("Celula Invalida!")
else:

    print ("Celula Valida!")
    print (table[startcell[0]][startcell[1]])    
        
    distance_x = ((startcell[0] - endcell[0])**2)
    distance_y = ((startcell[1] - endcell[1])**2)
    distance = (distance_x + distance_y) ** 0.5
    print distance

    ##Varredura 

    cell_distance = 8*[0]

    last_x = 1600*[0]
    last_y = 1600*[0]
    indice = 0

    start_x = startcell[0]
    start_y = startcell[1]

    direita = start_x + 1
    esquerda = start_x - 1
    baixo = start_y + 1
    cima = start_y - 1

    total_distance = 565.685424949
    count = 0

    while(total_distance > 0 and count < 1600):
        
        total_distance = 565.685424949
        
        if direita > 399:
            cell_distance[0] = 565.685424949
  
        else:        
       
            if table[start_x + 1][start_y] == ['0']:
       
                cell_distance[0] = 565.685424949
            else:
        
                distance_x = (((start_x+1) - endcell[0])**2)
                distance_y = ((start_y - endcell[1])**2)
                cell_distance[0] = (distance_x + distance_y) ** 0.5            
   
        if esquerda < 0:
            cell_distance[1] = 565.685424949
        
        else:        
                    
            if table[start_x - 1][start_y] == ['0']:
           
                cell_distance[1] = 565.685424949
            else:
            
                distance_x = (((start_x-1) - endcell[0])**2)
                distance_y = ((start_y - endcell[1])**2)
                cell_distance[1] = (distance_x + distance_y) ** 0.5
            
        if baixo > 399:
            cell_distance[2] = 565.685424949
      
        else:        
        
            if table[start_x][start_y+1] == ['0']:
              
                cell_distance[2] = 565.685424949
            else:
              
                distance_x = (((start_x) - endcell[0])**2)
                distance_y = (((start_y +1)- endcell[1])**2)
                cell_distance[2] = (distance_x + distance_y) ** 0.5

        if cima < 0:
            cell_distance[3] = 565.685424949
            
        else:        
        
            if table[start_x][start_y - 1] == ['0']:                
                cell_distance[3] = 565.685424949
            else:                
                distance_x = (((start_x) - endcell[0])**2)
                distance_y = (((start_y - 1) - endcell[1])**2)
                cell_distance[3] = (distance_x + distance_y) ** 0.5
            
        if esquerda < 0 or cima <0:
            cell_distance[4] = 565.685424949
            
        else:       
        
            if table[start_x - 1][start_y - 1] == ['0']:                
                cell_distance[4] = 565.685424949
            else:                
                distance_x = (((start_x-1) - endcell[0])**2)
                distance_y = (((start_y - 1) - endcell[1])**2)
                cell_distance[4] = (distance_x + distance_y) ** 0.5

        if direita > 399 or cima < 0:
            cell_distance[5] = 565.685424949
          
        else:        
        
            if table[start_x + 1][start_y - 1] == ['0']:            
         
                cell_distance[5] = 565.685424949
            else:              
                distance_x = (((start_x+1) - endcell[0])**2)
                distance_y = (((start_y - 1)- endcell[1])**2)
                cell_distance[5] = (distance_x + distance_y) ** 0.5

        if esquerda < 0 or baixo > 399:
            cell_distance[6] = 565.685424949
         
        else:        
        
            if table[start_x - 1][start_y + 1] == ['0']:             
                cell_distance[6] = 565.685424949
            else:               
                distance_x = (((start_x-1) - endcell[0])**2)
                distance_y = (((start_y + 1) - endcell[1])**2)
                cell_distance[6] = (distance_x + distance_y) ** 0.5

        if direita > 399 or baixo > 399:            
           
            cell_distance[7] = 565.685424949
            
        else:       
        
            if table[start_x + 1][start_y + 1] == ['0']:              
                cell_distance[7] = 565.685424949
            else:                
                distance_x = (((start_x+1) - endcell[0])**2)
                distance_y = (((start_y+1) - endcell[1])**2)
                cell_distance[7] = (distance_x + distance_y) ** 0.5

        for contador in range(0,7):        
            if cell_distance[contador] < total_distance:
                total_distance = cell_distance[contador]
                indice = contador
 
        if indice == 0:
            start_x = start_x + 1

        if indice == 1:
            start_x = start_x - 1

        if indice == 2:
            start_y = start_y + 1

        if indice == 3:
            start_y = start_y - 1

        if indice == 4:
            start_x = start_x - 1
            start_y = start_y - 1

        if indice == 5:
            start_x = start_x + 1
            start_y = start_y - 1

        if indice == 6:
            start_x = start_x - 1
            start_y = start_y + 1

        if indice == 7:
            start_x = start_x + 1
            start_y = start_y + 1

        last_x[count] = start_x
        last_y[count] = start_y    

        print (start_x,start_y)

        path[count] = [start_x, start_y]
        arq.write(str(path[count]))
        arq.write("\n")
        
              
        if count > 2:
            if ((last_x[count-2] - start_x <= 2 and last_x[count-2] - start_x > -1) or (last_x[count-2] - start_x >= -2 and last_x[count-2] - start_x <= 1)) and ((last_y[count-2] - start_y <= 2 and last_y[count-2] - start_y > -1)or (last_y[count-2] - start_y >= -2 and last_y[count-2] - start_y <= 1)):
                
                cv2.line(img,(start_x,start_y),(last_x[count-2],last_y[count-2]),(255,0,0),2)

            if (start_x == last_x[count-2]) and (start_y == last_y[count-2]): 

                print ("LOOP")
                dif_x = last_x[count-1] - start_x 
                dif_y = last_y[count-1] - start_y                 

                ##x e y voltam pra posicao antes do loop
                start_x = last_x[count-1]
                start_y = last_y[count-1]
                              
                direct = ""

                if table[start_x + 1][start_y] == ['0']:
                    direct = "Direita"

                    ##contadores de preto pra ver o melhor caminho

                    ##Se atentar ao fato de que a linha e desenhada porem as coordenadas nao sao armazenadas                    
                    opcao = 10
                    count_black = 0
                    count_black2 = 0

                    while table[start_x+1][start_y - count_black2] == ['0'] and start_y - 7 - count_black2 > 0 and count_black2 < 400:
                        count_black2 = count_black2 + 1                      
                        

                    while table[start_x+1][start_y + count_black] == ['0'] and start_y + 7 + count_black < 399 and count_black2 < 400:
                        count_black = count_black + 1                   
                        
                    print ("Nesse momento:", start_x, start_y)   
                    if count_black > count_black2:
                        opcao = 0
                        if table[start_x][start_y - 1] == ['0']:
                            opcao = 1
                    if count_black < count_black2:
                        opcao = 1
                        if table[start_x][start_y + 1] == ['0']:
                            opcao = 0
                        
                    if count_black == count_black2:
                        opcao = 2

                    if start_y - count_black2 <= 7:
                        opcao = 1

                    if start_y + count_black >= 392:
                        opcao = 0 
                                                       
                    if opcao == 0:
                        print (start_x,start_y-count_black2-1)                                              
                        
                        cv2.line(img,(start_x,start_y),(start_x,start_y-count_black2-1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y-count_black2-1),(start_x + 8,start_y-count_black2-1),(255,0,0),2)
                        start_y = start_y-count_black2-1
                        start_x = start_x + 8                                        
                           
                        
                    if opcao == 1:
                        print (start_x,start_y+count_black+1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y+count_black+1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y+count_black+1),(start_x + 8,start_y+count_black+1),(255,0,0),2)
                        start_y = start_y+count_black+1
                        start_x = start_x + 8

                if table[start_x - 1][start_y] == ['0']:
                    direct = "Esquerda"
                    count_black2 = 0
                    count_black = 0
                    opcao = 10
                    while table[start_x-1][start_y - count_black2] == ['0'] and start_y - 7 - count_black2 > 0 and count_black2 < 400:
                        count_black2 = count_black2 + 1

                    while table[start_x-1][start_y + count_black] == ['0'] and start_y + 7 + count_black < 399 and count_black2 < 400:
                        count_black = count_black + 1

                    if count_black > count_black2:
                        opcao = 0
                        if table[start_x][start_y - 1] == ['0']:
                            opcao = 1
                    if count_black < count_black2:
                        opcao = 1
                        if table[start_x][start_y + 1] == ['0']:
                            opcao = 1
                    if count_black == count_black2:
                        opcao = 2

                    if start_y - count_black2 <= 7:
                        opcao = 1

                    if start_y + count_black >= 392:
                        opcao = 0

                                  
                    if opcao == 0:
                        print (start_x,start_y-count_black2-1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y-count_black2-1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y-count_black2-1),(start_x - 8,start_y-count_black2-1),(255,0,0),2)
                        start_y = start_y-count_black2-1
                        start_x = start_x - 8

                    if opcao == 1:
                        print (start_x,start_y+count_black+1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y+count_black+1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y+count_black+1),(start_x - 8,start_y+count_black+1),(255,0,0),2)
                        start_y = start_y+count_black+1
                        start_x = start_x - 8

                if table[start_x][start_y + 1] == ['0']:
                    direct = "Baixo"

                    ##contadores de preto pra ver o melhor caminho

                    ##Se atentar ao fato de que a linha e desenhada porem as coordenadas nao sao armazenadas
                    count_black_esquerda = 100
                    count_black_direita = 100
                    count_black2 = 0
                    count_black = 0
                    opcao = 100
                    while table[start_x - count_black2][start_y + 1] == ['0'] and start_x - 7 - count_black2 > 0 and count_black2 < 400:
                        count_black2 = count_black2 + 1                      
                        

                    while table[start_x + count_black][start_y + 1] == ['0'] and start_x + 7 + count_black < 399 and count_black < 400:
                        count_black = count_black + 1

                    if table[start_x-1][start_y] == ['0']:
                        count_black_direita = 0
                        while table[start_x - 1][start_y - count_black_direita] == ['0'] and start_y - 7 - count_black_direita > 0 and count_black_direita < 400:
                            count_black_direita = count_black_direita + 1

                    if table[start_x+1][start_y] == ['0']:
                        count_black_esquerda = 0
                        while table[start_x + 1][start_y - count_black_esquerda] == ['0'] and start_y - 7 - count_black_esquerda > 0 and count_black_esquerda < 400:
                            count_black_esquerda = count_black_esquerda + 1
                                              
                    if count_black > count_black2:
                        opcao = 0
                        if table[start_x - 1][start_y] == ['0']:
                            opcao = 1
                    if count_black < count_black2:
                        opcao = 1
                        if table[start_x + 1][start_y] == ['0']:
                            opcao = 1
                    if count_black == count_black2:
                        opcao = 2

                    if start_y - count_black2 <= 7:
                        opcao = 1

                    if start_y + count_black >= 392:
                        opcao = 0

                    if count_black_direita < count_black and count_black_direita <count_black2:
                        opcao = 3

                    if count_black_esquerda < count_black and count_black_direita <count_black2:
                        opcao = 4
                                                       
                    if opcao == 0:
                        print (start_x - count_black2 - 1,start_y)
                                              
                        cv2.line(img,(start_x - count_black2 - 1,start_y),(start_x - count_black2 - 1,start_y + 8),(255,0,0),2)
                        cv2.line(img,(start_x,start_y),(start_x - count_black2 - 1,start_y),(255,0,0),2)
                        start_y = start_y + 8
                        start_x = start_x - count_black2 - 1                                     
                           
                        
                    if opcao == 1:
                        print (start_x + count_black + 1,start_y)
                                              
                        cv2.line(img,(start_x + count_black + 1,start_y),(start_x + count_black + 1,start_y + 8),(255,0,0),2)
                        cv2.line(img,(start_x,start_y),(start_x + count_black + 1,start_y),(255,0,0),2)
                        start_y = start_y + 8
                        start_x = start_x + count_black + 1

                    if opcao == 3:
                        print (start_x,start_y-count_black2-1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y-count_black2-1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y-count_black2-1),(start_x - 8,start_y-count_black2-1),(255,0,0),2)
                        start_y = start_y-count_black2-1
                        start_x = start_x - 8

                    if opcao == 4:
                        print (start_x,start_y-count_black2-1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y-count_black2-1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y-count_black2-1),(start_x + 8,start_y-count_black2-1),(255,0,0),2)
                        start_y = start_y-count_black2-1
                        start_x = start_x + 8
                    

                if table[start_x][start_y - 1] == ['0']:
                    direct = "Cima"

                    ##contadores de preto pra ver o melhor caminho

                    ##Se atentar ao fato de que a linha e desenhada porem as coordenadas nao sao armazenadas
                    count_black2 = 0
                    count_black = 0
                    opcao = 10
                    while table[start_x - count_black2][start_y - 1] == ['0'] and start_x - 7 - count_black2 > 0 and count_black2 < 400:
                        count_black2 = count_black2 + 1                      
                        

                    while table[start_x + count_black][start_y - 1] == ['0'] and start_y + 7 + count_black < 399 and count_black2 < 400:
                        count_black = count_black + 1                   
                        

                    print ("nesse momento:", start_x-1,start_y)
                    if count_black > count_black2:
                        opcao = 0
                        if table[start_x - 1][start_y] == ['0']:
                            opcao = 1
                    if count_black < count_black2:
                        opcao = 1
                        if table[start_x + 1][start_y] == ['0']:
                            opcao = 1
                    if count_black == count_black2:
                        opcao = 2

                    if start_y - count_black2 <= 7:
                        opcao = 1

                    if start_y + count_black >= 392:
                        opcao = 0 
                                                       
                    if opcao == 0:
                        print (start_x - count_black2 - 1,start_y)
                                              
                        cv2.line(img,(start_x - count_black2 - 1,start_y),(start_x - count_black2 - 1,start_y - 8),(255,0,0),2)
                        cv2.line(img,(start_x,start_y),(start_x - count_black2 - 1,start_y),(255,0,0),2)
                        start_y = start_y - 8
                        start_x = start_x - count_black2 - 1                                     
                           
                        
                    if opcao == 1:
                        print (start_x + count_black + 1,start_y)
                                              
                        cv2.line(img,(start_x + count_black + 1,start_y),(start_x + count_black + 1,start_y - 8),(255,0,0),2)
                        cv2.line(img,(start_x,start_y),(start_x + count_black + 1,start_y),(255,0,0),2)
                        start_y = start_y - 8
                        start_x = start_x + count_black + 1

                print direct                                            

        count = count + 1        
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
arq.close() 
