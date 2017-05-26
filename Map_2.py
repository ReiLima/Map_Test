# -*- coding: cp1252 -*-
import cv2
import numpy as np

##arq = open("table.txt", "w")

lista = 400*[[0]]

for contador in range(0,400):
    lista[contador] = 400*[[0,0,0]]

img = cv2.imread('Maptest.png')

for contador in range(0,400):
    
    for y in range(0,400):
        lista[y][contador] = img[contador,y]

table = 400*[[0]]

for contador in range(0,400):
    table[contador] = 400*[[0]]

for contador in range(0,400):
    ##arq.write("\n")
    for y in range(0,400):
        if(np.all(lista[contador][y]) == 0):
            table[contador][y] = ['0']
            
        if(np.all(lista[contador][y] == 255)):
            table[contador][y] = ['1']

        if(np.any(lista[contador][y] == 36)):
            table[contador][y] = ['2']

        ##arq.write(str(table[contador][y]))
        ##arq.write(" ")

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

    print ("Celula Valida!")
    print (table[startcell[0]][startcell[1]])    
        
    distx = ((startcell[0] - endcell[0])**2)
    disty = ((startcell[1] - endcell[1])**2)
    dist = (distx + disty) ** 0.5
    print dist

    ##Varredura 

    dist_table = 8*[0]

    last_x = 1600*[0]
    last_y = 1600*[0]
    indice = 0

    start_x = startcell[0]
    start_y = startcell[1]

    ifx = start_x + 1
    ifx_ = start_x - 1
    ify = start_y + 1
    ify_ = start_y - 1

    dist_t = 565.685424949
    count = 0

    while(dist_t > 0 and count < 1600):
        
        dist_t = 565.685424949
        
        if ifx > 399:
            dist_table[0] = 565.685424949
  
        else:        
       
            if table[start_x + 1][start_y] == ['0']:
       
                dist_table[0] = 565.685424949
            else:
        
                distx = (((start_x+1) - endcell[0])**2)
                disty = ((start_y - endcell[1])**2)
                dist_table[0] = (distx + disty) ** 0.5            
   
        if ifx_ < 0:
            dist_table[1] = 565.685424949
        
        else:        
                    
            if table[start_x - 1][start_y] == ['0']:
           
                dist_table[1] = 565.685424949
            else:
            
                distx = (((start_x-1) - endcell[0])**2)
                disty = ((start_y - endcell[1])**2)
                dist_table[1] = (distx + disty) ** 0.5
            
        if ify > 399:
            dist_table[2] = 565.685424949
      
        else:        
        
            if table[start_x][start_y+1] == ['0']:
              
                dist_table[2] = 565.685424949
            else:
              
                distx = (((start_x) - endcell[0])**2)
                disty = (((start_y +1)- endcell[1])**2)
                dist_table[2] = (distx + disty) ** 0.5

        if ify_ < 0:
            dist_table[3] = 565.685424949
            
        else:        
        
            if table[start_x][start_y - 1] == ['0']:                
                dist_table[3] = 565.685424949
            else:                
                distx = (((start_x) - endcell[0])**2)
                disty = (((start_y - 1) - endcell[1])**2)
                dist_table[3] = (distx + disty) ** 0.5
            
        if ifx_ < 0 or ify_ <0:
            dist_table[4] = 565.685424949
            
        else:       
        
            if table[start_x - 1][start_y - 1] == ['0']:                
                dist_table[4] = 565.685424949
            else:                
                distx = (((start_x-1) - endcell[0])**2)
                disty = (((start_y - 1) - endcell[1])**2)
                dist_table[4] = (distx + disty) ** 0.5

        if ifx > 399 or ify_ < 0:
            dist_table[5] = 565.685424949
          
        else:        
        
            if table[start_x + 1][start_y - 1] == ['0']:            
         
                dist_table[5] = 565.685424949
            else:              
                distx = (((start_x+1) - endcell[0])**2)
                disty = (((start_y - 1)- endcell[1])**2)
                dist_table[5] = (distx + disty) ** 0.5

        if ifx_ < 0 or ify > 399:
            dist_table[6] = 565.685424949
         
        else:        
        
            if table[start_x - 1][start_y + 1] == ['0']:             
                dist_table[6] = 565.685424949
            else:               
                distx = (((start_x-1) - endcell[0])**2)
                disty = (((start_y + 1) - endcell[1])**2)
                dist_table[6] = (distx + disty) ** 0.5

        if ifx > 399 or ify > 399:            
           
            dist_table[7] = 565.685424949
            
        else:       
        
            if table[start_x + 1][start_y + 1] == ['0']:              
                dist_table[7] = 565.685424949
            else:                
                distx = (((start_x+1) - endcell[0])**2)
                disty = (((start_y+1) - endcell[1])**2)
                dist_table[7] = (distx + disty) ** 0.5

        for contador in range(0,7):        
            if dist_table[contador] < dist_t:
                dist_t = dist_table[contador]
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
        
              
        if count > 2:
            if ((last_x[count-2] - start_x <= 2 and last_x[count-2] - start_x > -1)or (last_x[count-2] - start_x >= -2 and last_x[count-2] - start_x <= 1)) and ((last_y[count-2] - start_y <= 2 and last_y[count-2] - start_y > -1)or (last_y[count-2] - start_y >= -2 and last_y[count-2] - start_y <= 1)):
                
                cv2.line(img,(start_x,start_y),(last_x[count-2],last_y[count-2]),(255,0,0),2)
            if (start_x == last_x[count-2]) and (start_y == last_y[count-2]):                
                print ("LOOP")
                difx = last_x[count-1] - start_x 
                dify = last_y[count-1] - start_y                 

                ##x e y voltam pra posicao antes do loop
                start_x = last_x[count-1]
                start_y = last_y[count-1]
                              
                direct = ""

                if table[start_x + 1][start_y] == ['0']:
                    direct = "Direita"

                    ##contadores de preto pra ver o melhor caminho

                    ##Se atentar ao fato de que a linha e desenhada porem as coordenadas nao sao armazenadas
                    xc = 0
                    xb = 0
                    xa = 10
                    while table[start_x+1][start_y - xc] == ['0'] and start_y - 7 - xc > 0 and xc < 400:
                        xc = xc + 1                      
                        

                    while table[start_x+1][start_y + xb] == ['0'] and start_y + 7 + xb < 399 and xc < 400:
                        xb = xb + 1                   
                        
                    print ("nesse momento:", start_x, start_y)   
                    if xb > xc:
                        xa = 0
                        if table[start_x][start_y - 1] == ['0']:
                            xa = 1
                    if xb < xc:
                        xa = 1
                        if table[start_x][start_y + 1] == ['0']:
                            xa = 0
                        
                    if xb == xc:
                        xa = 2

                    if start_y - xc <= 7:
                        xa = 1

                    if start_y + xb >= 392:
                        xa = 0 
                                                       
                    if xa == 0:
                        print (start_x,start_y-xc-1)                                              
                        
                        cv2.line(img,(start_x,start_y),(start_x,start_y-xc-1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y-xc-1),(start_x + 8,start_y-xc-1),(255,0,0),2)
                        start_y = start_y-xc-1
                        start_x = start_x + 8                                        
                           
                        
                    if xa == 1:
                        print (start_x,start_y+xb+1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y+xb+1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y+xb+1),(start_x + 8,start_y+xb+1),(255,0,0),2)
                        start_y = start_y+xb+1
                        start_x = start_x + 8

                if table[start_x - 1][start_y] == ['0']:
                    direct = "Esquerda"
                    xc = 0
                    xb = 0
                    xa = 10
                    while table[start_x-1][start_y - xc] == ['0'] and start_y - 7 - xc > 0 and xc < 400:
                        xc = xc + 1

                    while table[start_x-1][start_y + xb] == ['0'] and start_y + 7 + xb < 399 and xc < 400:
                        xb = xb + 1

                    if xb > xc:
                        xa = 0
                        if table[start_x][start_y - 1] == ['0']:
                            xa = 1
                    if xb < xc:
                        xa = 1
                        if table[start_x][start_y + 1] == ['0']:
                            xa = 1
                    if xb == xc:
                        xa = 2

                    if start_y - xc <= 7:
                        xa = 1

                    if start_y + xb >= 392:
                        xa = 0

                                  
                    if xa == 0:
                        print (start_x,start_y-xc-1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y-xc-1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y-xc-1),(start_x - 8,start_y-xc-1),(255,0,0),2)
                        start_y = start_y-xc-1
                        start_x = start_x - 8

                    if xa == 1:
                        print (start_x,start_y+xb+1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y+xb+1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y+xb+1),(start_x - 8,start_y+xb+1),(255,0,0),2)
                        start_y = start_y+xb+1
                        start_x = start_x - 8

                if table[start_x][start_y + 1] == ['0']:
                    direct = "Baixo"

                    ##contadores de preto pra ver o melhor caminho

                    ##Se atentar ao fato de que a linha e desenhada porem as coordenadas nao sao armazenadas
                    xe = 100
                    xd = 100
                    xc = 0
                    xb = 0
                    xa = 100
                    while table[start_x - xc][start_y + 1] == ['0'] and start_x - 7 - xc > 0 and xc < 400:
                        xc = xc + 1                      
                        

                    while table[start_x + xb][start_y + 1] == ['0'] and start_x + 7 + xb < 399 and xb < 400:
                        xb = xb + 1

                    if table[start_x-1][start_y] == ['0']:
                        xd = 0
                        while table[start_x - 1][start_y - xd] == ['0'] and start_y - 7 - xd > 0 and xd < 400:
                            xd = xd + 1

                    if table[start_x+1][start_y] == ['0']:
                        xe = 0
                        while table[start_x + 1][start_y - xe] == ['0'] and start_y - 7 - xe > 0 and xe < 400:
                            xe = xe + 1
                                              
                    if xb > xc:
                        xa = 0
                        if table[start_x - 1][start_y] == ['0']:
                            xa = 1
                    if xb < xc:
                        xa = 1
                        if table[start_x + 1][start_y] == ['0']:
                            xa = 1
                    if xb == xc:
                        xa = 2

                    if start_y - xc <= 7:
                        xa = 1

                    if start_y + xb >= 392:
                        xa = 0

                    if xd < xb and xd <xc:
                        xa = 3

                    if xe < xb and xd <xc:
                        xa = 4
                                                       
                    if xa == 0:
                        print (start_x - xc - 1,start_y)
                                              
                        cv2.line(img,(start_x - xc - 1,start_y),(start_x - xc - 1,start_y + 8),(255,0,0),2)
                        cv2.line(img,(start_x,start_y),(start_x - xc - 1,start_y),(255,0,0),2)
                        start_y = start_y + 8
                        start_x = start_x - xc - 1                                     
                           
                        
                    if xa == 1:
                        print (start_x + xb + 1,start_y)
                                              
                        cv2.line(img,(start_x + xb + 1,start_y),(start_x + xb + 1,start_y + 8),(255,0,0),2)
                        cv2.line(img,(start_x,start_y),(start_x + xb + 1,start_y),(255,0,0),2)
                        start_y = start_y + 8
                        start_x = start_x + xb + 1

                    if xa == 3:
                        print (start_x,start_y-xc-1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y-xc-1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y-xc-1),(start_x - 8,start_y-xc-1),(255,0,0),2)
                        start_y = start_y-xc-1
                        start_x = start_x - 8

                    if xa == 4:
                        print (start_x,start_y-xc-1)
                        cv2.line(img,(start_x,start_y),(start_x,start_y-xc-1),(255,0,0),2)
                        cv2.line(img,(start_x,start_y-xc-1),(start_x + 8,start_y-xc-1),(255,0,0),2)
                        start_y = start_y-xc-1
                        start_x = start_x + 8
                    

                if table[start_x][start_y - 1] == ['0']:
                    direct = "Cima"

                    ##contadores de preto pra ver o melhor caminho

                    ##Se atentar ao fato de que a linha e desenhada porem as coordenadas nao sao armazenadas
                   xc = 0
                    xb = 0
                    xa = 10
                    while table[start_x - xc][start_y - 1] == ['0'] and start_x - 7 - xc > 0 and xc < 400:
                        xc = xc + 1                      
                        

                    while table[start_x + xb][start_y - 1] == ['0'] and start_y + 7 + xb < 399 and xc < 400:
                        xb = xb + 1                   
                        

                    print ("nesse momento:", start_x-1,start_y)
                    if xb > xc:
                        xa = 0
                        if table[start_x - 1][start_y] == ['0']:
                            xa = 1
                    if xb < xc:
                        xa = 1
                        if table[start_x + 1][start_y] == ['0']:
                            xa = 1
                    if xb == xc:
                        xa = 2

                    if start_y - xc <= 7:
                        xa = 1

                    if start_y + xb >= 392:
                        xa = 0 
                                                       
                    if xa == 0:
                        print (start_x - xc - 1,start_y)
                                              
                        cv2.line(img,(start_x - xc - 1,start_y),(start_x - xc - 1,start_y - 8),(255,0,0),2)
                        cv2.line(img,(start_x,start_y),(start_x - xc - 1,start_y),(255,0,0),2)
                        start_y = start_y - 8
                        start_x = start_x - xc - 1                                     
                           
                        
                    if xa == 1:
                        print (start_x + xb + 1,start_y)
                                              
                        cv2.line(img,(start_x + xb + 1,start_y),(start_x + xb + 1,start_y - 8),(255,0,0),2)
                        cv2.line(img,(start_x,start_y),(start_x + xb + 1,start_y),(255,0,0),2)
                        start_y = start_y - 8
                        start_x = start_x + xb + 1

                print direct                                            

        count = count + 1        
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
##arq.close() 
