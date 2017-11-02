# -*- coding: cp1252 -*-
import cv2
import numpy as np

def distance (start_x, start_y, final_x, final_y):

    start_x = int(start_x)
    start_y = int(start_y)
    final_x = int(final_x)
    final_y = int(final_y)
    
    distance_x = (start_x - final_x) ** 2
    distance_y = (start_y - final_y) ** 2
    distance = (distance_x + distance_y) ** 0.5
    return distance

def black_line (start_x, start_y, alcance, direct):

    start_x = int(start_x)
    start_y = int(start_y)
    alcance = int(alcance)
    direct = int(direct)

    black = 0

    if(direct == 0):
        for i in range(0, alcance):
            if table[start_x + i][start_y] == ['0']:
                black = 1

    if(direct == 1):
        for i in range(0, alcance):
            if table[start_x - i][start_y] == ['0']:
                black = 1

    if(direct == 2):
        for i in range(0, alcance):
            if table[start_x][start_y + i] == ['0']:
                black = 1

    if(direct == 3):
        for i in range(0, alcance):
            if table[start_x][start_y - i] == ['0']:
                black = 1

    if(direct == 4):
        for i in range(0, alcance):
            if table[start_x - i][start_y - i] == ['0']:
                black = 1

    if(direct == 5):
        for i in range(0, alcance):
            if table[start_x + i][start_y - i] == ['0']:
                black = 1

    if(direct == 6):
        for i in range(0, alcance):
            if table[start_x - i][start_y + i] == ['0']:
                black = 1
                
    if(direct == 7):
        for i in range(0, alcance):
            if table[start_x + i][start_y + i] == ['0']:
                black = 1
    
    return black

#arquivo = open("Caminho.txt", "w")

lista = 400*[[0]]
table = 400*[[0]]
path = 4000*[[0,0]]
inversao = 0

for i in range(0,400):
    lista[i] = 400*[[0,0,0]]
    table[i] = 400*[[0]]

data_input = raw_input("Digite o numero do mapa desejado: ")
data_input = int(data_input)
if data_input == 1:    
    img = cv2.imread('Map1.png')
else:
    img = cv2.imread('img2.png')

#print img.shape[0]
#print img.shape[1]

for i in range(0,400):
    
    for j in range(0,400):
        lista[j][i] = img[i,j]

for i in range(0,400):
    
    for j in range(0,400):
        if(np.all(lista[i][j]) == 0):
            table[i][j] = ['0']
            
        if(np.all(lista[i][j] == 255)):
            table[i][j] = ['1']

        if(np.any(lista[i][j] == 36)):
            table[i][j] = ['2']

condicional = 0
while(condicional == 0):
    data_input = raw_input("Digite as coordenadas iniciais: ")
    startcell = data_input.split(",")
    startcell[0] = int(startcell[0])
    startcell[1] = int(startcell[1])

    if(table[startcell[0]][startcell[1]] == ['0']):
        print ("\nCoordenadas Invalidas! Digite Novamente.\n")
    else:
        condicional = 1

condicional = 0
while(condicional == 0):
    data_input = raw_input("Digite as coordenadas finais: ")
    endcell = data_input.split(",")
    endcell[0] = int(endcell[0])
    endcell[1] = int(endcell[1])

    if(table[endcell[0]][endcell[1]] == ['0']):
        print ("\nCoordenadas Invalidas! Digite Novamente.\n")
    else:
        condicional = 1

print 'Distancia Total:' , distance(startcell[0],startcell[1],endcell[0],endcell[1])

cell_distance = 8*[0]

last_x = 4000*[0]
last_y = 4000*[0]
indice = 0

start_x = startcell[0]
start_y = startcell[1]

alcance = int(30)

count = 0

total_distance = 565.685424949

while(total_distance > 0 and count < 4000):

    total_distance = 565.685424949

    direita = start_x + alcance
    esquerda = start_x - alcance
    baixo = start_y + alcance
    cima = start_y - alcance

    direita_caminho = start_x + 1
    esquerda_caminho = start_x - 1
    baixo_caminho = start_y + 1
    cima_caminho = start_y - 1
    

    if direita > 399:
        cell_distance[0] = 565.685424949
    else:        
        if black_line (start_x, start_y, alcance, 0) == 1:
            #print('1')
            cell_distance[0] = 565.685424949        
        else:
            cell_distance[0] = distance(direita_caminho,start_y,endcell[0],endcell[1])

    if esquerda < 0:
        cell_distance[1] = 565.685424949
    else:        
        if black_line (start_x, start_y, alcance, 1) == 1:
            #print('2')
            cell_distance[1] = 565.685424949        
        else:
            cell_distance[1] = distance(esquerda_caminho,start_y,endcell[0],endcell[1])


    if baixo > 399:
        cell_distance[2] = 565.685424949
    else:        
        if black_line (start_x, start_y, alcance, 2) == 1:
            #print('3')
            cell_distance[2] = 565.685424949        
        else:
            cell_distance[2] = distance(start_x,baixo_caminho,endcell[0],endcell[1])

    
    if cima < 0:
        cell_distance[3] = 565.685424949
    else:        
        if black_line (start_x, start_y, alcance, 3) == 1:
            #print('4')
            cell_distance[3] = 565.685424949        
        else:
            cell_distance[3] = distance(start_x,cima_caminho,endcell[0],endcell[1])


    if esquerda < 0 or cima <0:
        cell_distance[4] = 565.685424949            
    else:
        if black_line (start_x, start_y, alcance, 4) == 1:
            #print('5')
            cell_distance[4] = 565.685424949
        else:
            cell_distance[4] = distance(esquerda_caminho,cima_caminho,endcell[0],endcell[1])                


    if direita > 399 or cima < 0:
        cell_distance[5] = 565.685424949          
    else:     
        if black_line (start_x, start_y, alcance, 5):
            #print('6')
            cell_distance[5] = 565.685424949
        else:
            cell_distance[5] = distance(direita_caminho,cima_caminho,endcell[0],endcell[1])                


    if esquerda < 0 or baixo > 399:
        cell_distance[6] = 565.685424949         
    else:       
        if black_line (start_x, start_y, alcance, 6) == 1:
            #print('7')
            cell_distance[6] = 565.685424949
        else:
            cell_distance[6] = distance(esquerda_caminho,baixo_caminho,endcell[0],endcell[1])                


    if direita > 399 or baixo > 399:         
        cell_distance[7] = 565.685424949
    else:       
        if black_line (start_x, start_y, alcance, 7):
            #print('8')
            cell_distance[7] = 565.685424949
        else:
            cell_distance[7] = distance(direita_caminho,baixo_caminho,endcell[0],endcell[1])                


    for contador in range(0,7):        
        if cell_distance[contador] < total_distance:
            total_distance = cell_distance[contador]
            indice = contador

    
    if indice == 0:
        start_x = direita_caminho

    if indice == 1:
        start_x = esquerda_caminho

    if indice == 2:
        start_y = baixo_caminho

    if indice == 3:
        start_y = cima_caminho

    if indice == 4:
        start_x = esquerda_caminho
        start_y = cima_caminho

    if indice == 5:
        start_x = direita_caminho
        start_y = cima_caminho

    if indice == 6:
        start_x = esquerda_caminho
        start_y = baixo_caminho

    if indice == 7:
        start_x = direita_caminho
        start_y = baixo_caminho


    #print (start_x,start_y)

    path[count] = [int(start_x), int(start_y)]    

    is_loop = 0

    if(count > 1):
        if path[count] == path[count - 2]:
            #print('LOOP')
            is_loop = 1
            #total_distance = -10

    direct = " "

    if(is_loop == 1):        

        if black_line (start_x, start_y, alcance, 0) == 1:
            direct = "direita"
        if black_line (start_x, start_y, alcance, 1) == 1:
            direct = "esquerda"
        if black_line (start_x, start_y, alcance, 2) == 1:
            direct = "baixo"
        if black_line (start_x, start_y, alcance, 3) == 1:
            direct = "cima"

        #print direct

        upper_black = 0
        lower_black = 0
        righter_black = 0
        lefter_black = 0

        opcao = 0

        if direct == "direita":
            while black_line (start_x, start_y - upper_black, alcance, 0) == 1 and start_y - upper_black - 10 > 0:
                upper_black = upper_black + 1
                if start_y - upper_black - 30 < 0:
                    break

            while black_line (start_x, start_y + lower_black, alcance, 0) == 1 and start_y + lower_black + 10 < 400:
                lower_black = lower_black + 1
                if start_y + lower_black + 30 > 400:
                    break
                

            if upper_black < lower_black:
                opcao = 1
            if lower_black < upper_black:
                opcao = 2
            if upper_black == lower_black:
                opcao = 3

            if start_y - upper_black - 30 < 0:
                opcao = 2
            if start_y + lower_black + 30 > 400:
                opcao = 1


            if opcao == 1:

                contador_quina = 1

                corner = black_line (start_x,start_y, upper_black, 3)
                #print corner

                if corner == 1:
                    while black_line (start_x - contador_quina,start_y, upper_black, 3) == 1:
                        contador_quina = contador_quina + 1
                        if start_x - contador_quina - 30 < 0:
                            break
                    for i in range(1, contador_quina + 10):
                        path[count] = [int(start_x - i), int(start_y)]
                        if(count + 1 == 4000):
                            break  
                        count = count + 1
                    start_x = start_x - i
                
                for i in range(1,upper_black + 10):
                    path[count] = [int(start_x), int(start_y - i)]
                    if(count + 1 == 4000):
                        break  
                    count = count + 1
                    #print path[count - 1]

                start_y = start_y - i

                for i in range(1,40):
                    path[count] = [int(start_x + i), int(start_y)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_x = start_x + i
            
            if opcao == 2:

                contador_quina = 1
                
                corner = black_line (start_x,start_y, upper_black, 2)
                #print corner

                if corner == 1:
                    while black_line (start_x - contador_quina,start_y, lower_black, 2) == 1:
                        contador_quina = contador_quina + 1
                        if start_x - contador_quina - 30 < 0:
                            break
                    for i in range(1, contador_quina + 10):
                        path[count] = [int(start_x - i), int(start_y)]
                        if(count + 1 == 4000):
                            break                        
                        count = count + 1
                    start_x = start_x - i
                    
                for i in range(1,lower_black + 10):
                    path[count] = [int(start_x), int(start_y + i)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_y = start_y + i                

                for i in range(1,40):
                    path[count] = [int(start_x + i), int(start_y)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_x = start_x + i
                    
            count = count - 1

        if direct == "esquerda":
            while black_line (start_x, start_y - upper_black, alcance, 1) == 1 and start_y - upper_black - 10 > 0:
                upper_black = upper_black + 1
                if start_y - upper_black - 30 < 0:
                    break

            while black_line (start_x, start_y + lower_black, alcance, 1) == 1 and start_y + lower_black + 10 < 400:
                lower_black = lower_black + 1
                if start_y + lower_black + 30 > 400:
                    break

            if upper_black < lower_black:
                opcao = 1
            if lower_black < upper_black:
                opcao = 2
            if upper_black == lower_black:
                opcao = 3

            if start_y - upper_black - 30 < 0:
                opcao = 2
            if start_y + lower_black + 30 > 400:
                opcao = 1


            if opcao == 1:

                contador_quina = 1

                corner = black_line (start_x,start_y, upper_black, 3)
                #print corner

                if corner == 1:
                    while black_line (start_x + contador_quina,start_y, upper_black, 3) == 1:
                        contador_quina = contador_quina + 1
                        if start_x + contador_quina + 30 > 400:
                            break
                    for i in range(1, contador_quina + 10):
                        path[count] = [int(start_x + i), int(start_y)]
                        if(count + 1 == 4000):
                            break                        
                        count = count + 1
                    start_x = start_x + i
                    
                for i in range(1,upper_black + 10):
                    path[count] = [int(start_x), int(start_y - i)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    ##print path[count - 1]

                start_y = start_y - i

                for i in range(1,40):
                    path[count] = [int(start_x - i), int(start_y)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_x = start_x - i
            
            if opcao == 2:

                contador_quina = 1

                corner = black_line (start_x,start_y, lower_black, 2)
                #print corner

                if corner == 1:
                    while black_line (start_x + contador_quina,start_y, lower_black, 2) == 1:
                        contador_quina = contador_quina + 1
                        if start_x + contador_quina + 30 > 400:
                            break
                    for i in range(1, contador_quina + 10):
                        path[count] = [int(start_x + i), int(start_y)]
                        if(count + 1 == 4000):
                            break                        
                        count = count + 1
                    start_x = start_x + i
                    
                for i in range(1,lower_black + 10):
                    path[count] = [int(start_x), int(start_y + i)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_y = start_y + i

                for i in range(1,40):
                    path[count] = [int(start_x - i), int(start_y)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_x = start_x - i
                    
            count = count - 1

        if direct == "cima":
            while black_line (start_x - lefter_black,start_y, alcance, 3) == 1 and start_x - lefter_black - 10 > 0:
                lefter_black = lefter_black + 1
                if start_x - lefter_black - 30 < 0:
                    break

            while black_line (start_x + righter_black,start_y, alcance, 3) == 1 and start_x + righter_black + 10 < 400:
                righter_black = righter_black + 1
                if start_y + righter_black + 30 > 400:
                    break

            if lefter_black < righter_black:
                opcao = 1
            if righter_black < lefter_black:
                opcao = 2
            if lefter_black == righter_black:
                opcao = 3

            if start_y + righter_black + 30 > 400:
                opcao = 1
            if start_x - lefter_black - 30 < 0:
                opcao = 2


            if opcao == 1:

                contador_quina = 1

                corner = black_line (start_x,start_y, lefter_black, 1)
                #print corner

                if corner == 1:
                    
                    while black_line (start_x,start_y + contador_quina, lefter_black, 1) == 1:
                        contador_quina = contador_quina + 1
                        if start_y + contador_quina + 30 > 400:
                            break
                    for i in range(1, contador_quina + 10):
                        path[count] = [int(start_x), int(start_y + i)]
                        if(count + 1 == 4000):
                            break                        
                        count = count + 1
                    start_y = start_y + i
                    
                for i in range(1,lefter_black + 10):
                    path[count] = [int(start_x - i), int(start_y)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_x = start_x - i

                for i in range(1,40):
                    path[count] = [int(start_x), int(start_y - i)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_y = start_y - i
            
            if opcao == 2:

                contador_quina = 1

                corner = black_line (start_x,start_y, righter_black, 0)
                #print corner
                
                if corner == 1:
                    
                    while black_line (start_x,start_y + contador_quina, righter_black, 0) == 1:
                        contador_quina = contador_quina + 1
                        if start_y + contador_quina + 30 > 400:
                            break
                    for i in range(1, contador_quina + 10):
                        path[count] = [int(start_x), int(start_y + i)]
                        if(count + 1 == 4000):
                            break                        
                        count = count + 1
                    start_y = start_y + i
                    
                for i in range(1,righter_black + 10):
                    path[count] = [int(start_x + i), int(start_y)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_x = start_x + i

                for i in range(1,40):
                    path[count] = [int(start_x), int(start_y - i)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_y = start_y - i
                    
            count = count - 1
            
        if direct == "baixo":
            while black_line (start_x - lefter_black,start_y, alcance, 2) == 1 and start_x - lefter_black - 10 > 0:
                lefter_black = lefter_black + 1
                if start_x - lefter_black - 30 < 0:
                    break

            while black_line (start_x + righter_black,start_y, alcance, 2) == 1 and start_x + righter_black + 10 < 400:
                righter_black = righter_black + 1
                if start_y + righter_black + 30 > 400:
                    break

            if lefter_black < righter_black:
                opcao = 1
            if righter_black < lefter_black:
                opcao = 2
            if lefter_black == righter_black:
                opcao = 3

            if start_y + righter_black + 30 > 400:
                opcao = 1
            if start_x - lefter_black - 30 < 0:
                opcao = 2


            if opcao == 1:

                contador_quina = 1

                corner = black_line (start_x,start_y, lefter_black, 1)
                #print corner

                if corner == 1:
                    
                    while black_line (start_x,start_y - contador_quina, lefter_black, 1) == 1:
                        contador_quina = contador_quina + 1
                        if start_y - contador_quina - 30 < 0:
                            break
                    for i in range(1, contador_quina + 10):
                        path[count] = [int(start_x), int(start_y + i)]
                        if(count + 1 == 4000):
                            break                        
                        count = count + 1
                    start_y = start_y - i
     
                
                for i in range(1,lefter_black + 10):
                    path[count] = [int(start_x - i), int(start_y)]
                    if(count + 1 == 4000):
                        break                    
                    count = count + 1
                    #print path[count - 1]

                start_x = start_x + i

                for i in range(1,40):
                    path[count] = [int(start_x), int(start_y + i)]
                    if(count + 1 == 4000):
                        break
                    count = count + 1
                    #print path[count - 1]

                start_y = start_y + i
            
            if opcao == 2:

                contador_quina = 1

                corner = black_line (start_x,start_y, righter_black, 0)
                #print corner

                if corner == 1:
                    
                    while black_line (start_x,start_y - contador_quina, righter_black, 0) == 1:
                        contador_quina = contador_quina + 1
                        if start_y - contador_quina - 30 < 0:
                            break
                    for i in range(1, contador_quina + 10):
                        path[count] = [int(start_x), int(start_y + i)]
                        if(count + 1 == 4000):
                            break
                        count = count + 1
                    start_y = start_y - i     
                
                for i in range(1,righter_black + 10):
                    path[count] = [int(start_x + i), int(start_y)]
                    if(count + 1 == 4000):
                        break
                    count = count + 1
                    #print path[count - 1]

                start_x = start_x + i

                for i in range(1,40):
                    path[count] = [int(start_x), int(start_y + i)]
                    if(count + 1 == 4000):
                        break
                    count = count + 1
                    #print path[count - 1]

                start_y = start_y + i
                    
            count = count - 1
    if(count + 1 == 4000):
        break
    count = count + 1

inicio_troca = 0
final_troca = 0
caminho_erro = 0

if count + 1 == 4000:
    print ("Erro na geracao do caminho. Overload.")
    caminho_erro = 1
else:
    for i in range(0, count):
        if table[path[i][0]][path[i][1]] == ['0']:
            print ("Erro na geracao do caminho. Black Path.")
            caminho_erro = 1

if caminho_erro == 1:

    inversao = 1
    
    path = 4000*[[0,0]]

    last_x = 4000*[0]
    last_y = 4000*[0]
    indice = 0

    start_x = endcell[0]
    start_y = endcell[1]

    endcell[0] = startcell[0]
    endcell[1] = startcell[1]

    alcance = int(30)

    count = 0

    total_distance = 565.685424949

    while(total_distance > 0 and count < 4000):

        total_distance = 565.685424949

        direita = start_x + alcance
        esquerda = start_x - alcance
        baixo = start_y + alcance
        cima = start_y - alcance

        direita_caminho = start_x + 1
        esquerda_caminho = start_x - 1
        baixo_caminho = start_y + 1
        cima_caminho = start_y - 1
        

        if direita > 399:
            cell_distance[0] = 565.685424949
        else:        
            if black_line (start_x, start_y, alcance, 0) == 1:
                #print('1')
                cell_distance[0] = 565.685424949        
            else:
                cell_distance[0] = distance(direita_caminho,start_y,endcell[0],endcell[1])

        if esquerda < 0:
            cell_distance[1] = 565.685424949
        else:        
            if black_line (start_x, start_y, alcance, 1) == 1:
                #print('2')
                cell_distance[1] = 565.685424949        
            else:
                cell_distance[1] = distance(esquerda_caminho,start_y,endcell[0],endcell[1])


        if baixo > 399:
            cell_distance[2] = 565.685424949
        else:        
            if black_line (start_x, start_y, alcance, 2) == 1:
                #print('3')
                cell_distance[2] = 565.685424949        
            else:
                cell_distance[2] = distance(start_x,baixo_caminho,endcell[0],endcell[1])

        
        if cima < 0:
            cell_distance[3] = 565.685424949
        else:        
            if black_line (start_x, start_y, alcance, 3) == 1:
                #print('4')
                cell_distance[3] = 565.685424949        
            else:
                cell_distance[3] = distance(start_x,cima_caminho,endcell[0],endcell[1])


        if esquerda < 0 or cima <0:
            cell_distance[4] = 565.685424949            
        else:
            if black_line (start_x, start_y, alcance, 4) == 1:
                #print('5')
                cell_distance[4] = 565.685424949
            else:
                cell_distance[4] = distance(esquerda_caminho,cima_caminho,endcell[0],endcell[1])                


        if direita > 399 or cima < 0:
            cell_distance[5] = 565.685424949          
        else:     
            if black_line (start_x, start_y, alcance, 5):
                #print('6')
                cell_distance[5] = 565.685424949
            else:
                cell_distance[5] = distance(direita_caminho,cima_caminho,endcell[0],endcell[1])                


        if esquerda < 0 or baixo > 399:
            cell_distance[6] = 565.685424949         
        else:       
            if black_line (start_x, start_y, alcance, 6) == 1:
                #print('7')
                cell_distance[6] = 565.685424949
            else:
                cell_distance[6] = distance(esquerda_caminho,baixo_caminho,endcell[0],endcell[1])                


        if direita > 399 or baixo > 399:         
            cell_distance[7] = 565.685424949
        else:       
            if black_line (start_x, start_y, alcance, 7):
                #print('8')
                cell_distance[7] = 565.685424949
            else:
                cell_distance[7] = distance(direita_caminho,baixo_caminho,endcell[0],endcell[1])                


        for contador in range(0,7):        
            if cell_distance[contador] < total_distance:
                total_distance = cell_distance[contador]
                indice = contador

        
        if indice == 0:
            start_x = direita_caminho

        if indice == 1:
            start_x = esquerda_caminho

        if indice == 2:
            start_y = baixo_caminho

        if indice == 3:
            start_y = cima_caminho

        if indice == 4:
            start_x = esquerda_caminho
            start_y = cima_caminho

        if indice == 5:
            start_x = direita_caminho
            start_y = cima_caminho

        if indice == 6:
            start_x = esquerda_caminho
            start_y = baixo_caminho

        if indice == 7:
            start_x = direita_caminho
            start_y = baixo_caminho


        #print (start_x,start_y)

        path[count] = [int(start_x), int(start_y)]    

        is_loop = 0

        if(count > 1):
            if path[count] == path[count - 2]:
                #print('LOOP')
                is_loop = 1
                #total_distance = -10

        direct = " "

        if(is_loop == 1):        

            if black_line (start_x, start_y, alcance, 0) == 1:
                direct = "direita"
            if black_line (start_x, start_y, alcance, 1) == 1:
                direct = "esquerda"
            if black_line (start_x, start_y, alcance, 2) == 1:
                direct = "baixo"
            if black_line (start_x, start_y, alcance, 3) == 1:
                direct = "cima"

            #print direct

            upper_black = 0
            lower_black = 0
            righter_black = 0
            lefter_black = 0

            opcao = 0

            if direct == "direita":
                while black_line (start_x, start_y - upper_black, alcance, 0) == 1 and start_y - upper_black - 10 > 0:
                    upper_black = upper_black + 1
                    if start_y - upper_black - 30 < 0:
                        break

                while black_line (start_x, start_y + lower_black, alcance, 0) == 1 and start_y + lower_black + 10 < 400:
                    lower_black = lower_black + 1
                    if start_y + lower_black + 30 > 400:
                        break
                    

                if upper_black < lower_black:
                    opcao = 1
                if lower_black < upper_black:
                    opcao = 2
                if upper_black == lower_black:
                    opcao = 3

                if start_y - upper_black - 30 < 0:
                    opcao = 2
                if start_y + lower_black + 30 > 400:
                    opcao = 1


                if opcao == 1:

                    contador_quina = 1

                    corner = black_line (start_x,start_y, upper_black, 3)
                    #print corner

                    if corner == 1:
                        while black_line (start_x - contador_quina,start_y, upper_black, 3) == 1:
                            contador_quina = contador_quina + 1
                            if start_x - contador_quina - 30 < 0:
                                break
                        for i in range(1, contador_quina + 10):
                            path[count] = [int(start_x - i), int(start_y)]
                            if(count + 1 == 4000):
                                break  
                            count = count + 1
                        start_x = start_x - i
                    
                    for i in range(1,upper_black + 10):
                        path[count] = [int(start_x), int(start_y - i)]
                        if(count + 1 == 4000):
                            break  
                        count = count + 1
                        #print path[count - 1]

                    start_y = start_y - i

                    for i in range(1,40):
                        path[count] = [int(start_x + i), int(start_y)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_x = start_x + i
                
                if opcao == 2:

                    contador_quina = 1
                    
                    corner = black_line (start_x,start_y, upper_black, 2)
                    #print corner

                    if corner == 1:
                        while black_line (start_x - contador_quina,start_y, lower_black, 2) == 1:
                            contador_quina = contador_quina + 1
                            if start_x - contador_quina - 30 < 0:
                                break
                        for i in range(1, contador_quina + 10):
                            path[count] = [int(start_x - i), int(start_y)]
                            if(count + 1 == 4000):
                                break                        
                            count = count + 1
                        start_x = start_x - i
                        
                    for i in range(1,lower_black + 10):
                        path[count] = [int(start_x), int(start_y + i)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_y = start_y + i                

                    for i in range(1,40):
                        path[count] = [int(start_x + i), int(start_y)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_x = start_x + i
                        
                count = count - 1

            if direct == "esquerda":
                while black_line (start_x, start_y - upper_black, alcance, 1) == 1 and start_y - upper_black - 10 > 0:
                    upper_black = upper_black + 1
                    if start_y - upper_black - 30 < 0:
                        break

                while black_line (start_x, start_y + lower_black, alcance, 1) == 1 and start_y + lower_black + 10 < 400:
                    lower_black = lower_black + 1
                    if start_y + lower_black + 30 > 400:
                        break

                if upper_black < lower_black:
                    opcao = 1
                if lower_black < upper_black:
                    opcao = 2
                if upper_black == lower_black:
                    opcao = 3

                if start_y - upper_black - 30 < 0:
                    opcao = 2
                if start_y + lower_black + 30 > 400:
                    opcao = 1


                if opcao == 1:

                    contador_quina = 1

                    corner = black_line (start_x,start_y, upper_black, 3)
                    #print corner

                    if corner == 1:
                        while black_line (start_x + contador_quina,start_y, upper_black, 3) == 1:
                            contador_quina = contador_quina + 1
                            if start_x + contador_quina + 30 > 400:
                                break
                        for i in range(1, contador_quina + 10):
                            path[count] = [int(start_x + i), int(start_y)]
                            if(count + 1 == 4000):
                                break                        
                            count = count + 1
                        start_x = start_x + i
                        
                    for i in range(1,upper_black + 10):
                        path[count] = [int(start_x), int(start_y - i)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        ##print path[count - 1]

                    start_y = start_y - i

                    for i in range(1,40):
                        path[count] = [int(start_x - i), int(start_y)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_x = start_x - i
                
                if opcao == 2:

                    contador_quina = 1

                    corner = black_line (start_x,start_y, lower_black, 2)
                    #print corner

                    if corner == 1:
                        while black_line (start_x + contador_quina,start_y, lower_black, 2) == 1:
                            contador_quina = contador_quina + 1
                            if start_x + contador_quina + 30 > 400:
                                break
                        for i in range(1, contador_quina + 10):
                            path[count] = [int(start_x + i), int(start_y)]
                            if(count + 1 == 4000):
                                break                        
                            count = count + 1
                        start_x = start_x + i
                        
                    for i in range(1,lower_black + 10):
                        path[count] = [int(start_x), int(start_y + i)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_y = start_y + i

                    for i in range(1,40):
                        path[count] = [int(start_x - i), int(start_y)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_x = start_x - i
                        
                count = count - 1

            if direct == "cima":
                while black_line (start_x - lefter_black,start_y, alcance, 3) == 1 and start_x - lefter_black - 10 > 0:
                    lefter_black = lefter_black + 1
                    if start_x - lefter_black - 30 < 0:
                        break

                while black_line (start_x + righter_black,start_y, alcance, 3) == 1 and start_x + righter_black + 10 < 400:
                    righter_black = righter_black + 1
                    if start_y + righter_black + 30 > 400:
                        break

                if lefter_black < righter_black:
                    opcao = 1
                if righter_black < lefter_black:
                    opcao = 2
                if lefter_black == righter_black:
                    opcao = 3

                if start_y + righter_black + 30 > 400:
                    opcao = 1
                if start_x - lefter_black - 30 < 0:
                    opcao = 2


                if opcao == 1:

                    contador_quina = 1

                    corner = black_line (start_x,start_y, lefter_black, 1)
                    #print corner

                    if corner == 1:
                        
                        while black_line (start_x,start_y + contador_quina, lefter_black, 1) == 1:
                            contador_quina = contador_quina + 1
                            if start_y + contador_quina + 30 > 400:
                                break
                        for i in range(1, contador_quina + 10):
                            path[count] = [int(start_x), int(start_y + i)]
                            if(count + 1 == 4000):
                                break                        
                            count = count + 1
                        start_y = start_y + i
                        
                    for i in range(1,lefter_black + 10):
                        path[count] = [int(start_x - i), int(start_y)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_x = start_x - i

                    for i in range(1,40):
                        path[count] = [int(start_x), int(start_y - i)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_y = start_y - i
                
                if opcao == 2:

                    contador_quina = 1

                    corner = black_line (start_x,start_y, righter_black, 0)
                    #print corner
                    
                    if corner == 1:
                        
                        while black_line (start_x,start_y + contador_quina, righter_black, 0) == 1:
                            contador_quina = contador_quina + 1
                            if start_y + contador_quina + 30 > 400:
                                break
                        for i in range(1, contador_quina + 10):
                            path[count] = [int(start_x), int(start_y + i)]
                            if(count + 1 == 4000):
                                break                        
                            count = count + 1
                        start_y = start_y + i
                        
                    for i in range(1,righter_black + 10):
                        path[count] = [int(start_x + i), int(start_y)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_x = start_x + i

                    for i in range(1,40):
                        path[count] = [int(start_x), int(start_y - i)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_y = start_y - i
                        
                count = count - 1
                
            if direct == "baixo":
                while black_line (start_x - lefter_black,start_y, alcance, 2) == 1 and start_x - lefter_black - 10 > 0:
                    lefter_black = lefter_black + 1
                    if start_x - lefter_black - 30 < 0:
                        break

                while black_line (start_x + righter_black,start_y, alcance, 2) == 1 and start_x + righter_black + 10 < 400:
                    righter_black = righter_black + 1
                    if start_y + righter_black + 30 > 400:
                        break

                if lefter_black < righter_black:
                    opcao = 1
                if righter_black < lefter_black:
                    opcao = 2
                if lefter_black == righter_black:
                    opcao = 3

                if start_y + righter_black + 30 > 400:
                    opcao = 1
                if start_x - lefter_black - 30 < 0:
                    opcao = 2


                if opcao == 1:

                    contador_quina = 1

                    corner = black_line (start_x,start_y, lefter_black, 1)
                    #print corner

                    if corner == 1:
                        
                        while black_line (start_x,start_y - contador_quina, lefter_black, 1) == 1:
                            contador_quina = contador_quina + 1
                            if start_y - contador_quina - 30 < 0:
                                break
                        for i in range(1, contador_quina + 10):
                            path[count] = [int(start_x), int(start_y + i)]
                            if(count + 1 == 4000):
                                break                        
                            count = count + 1
                        start_y = start_y - i
         
                    
                    for i in range(1,lefter_black + 10):
                        path[count] = [int(start_x - i), int(start_y)]
                        if(count + 1 == 4000):
                            break                    
                        count = count + 1
                        #print path[count - 1]

                    start_x = start_x + i

                    for i in range(1,40):
                        path[count] = [int(start_x), int(start_y + i)]
                        if(count + 1 == 4000):
                            break
                        count = count + 1
                        #print path[count - 1]

                    start_y = start_y + i
                
                if opcao == 2:

                    contador_quina = 1

                    corner = black_line (start_x,start_y, righter_black, 0)
                    #print corner

                    if corner == 1:
                        
                        while black_line (start_x,start_y - contador_quina, righter_black, 0) == 1:
                            contador_quina = contador_quina + 1
                            if start_y - contador_quina - 30 < 0:
                                break
                        for i in range(1, contador_quina + 10):
                            path[count] = [int(start_x), int(start_y + i)]
                            if(count + 1 == 4000):
                                break
                            count = count + 1
                        start_y = start_y - i     
                    
                    for i in range(1,righter_black + 10):
                        path[count] = [int(start_x + i), int(start_y)]
                        if(count + 1 == 4000):
                            break
                        count = count + 1
                        #print path[count - 1]

                    start_x = start_x + i

                    for i in range(1,40):
                        path[count] = [int(start_x), int(start_y + i)]
                        if(count + 1 == 4000):
                            break
                        count = count + 1
                        #print path[count - 1]

                    start_y = start_y + i
                        
                count = count - 1
        if(count + 1 == 4000):
            break
        count = count + 1
    


for i in range(0, count):
    for j in range(0, count):
        if(path[i] == path[j]):
            inicio_troca = i
            final_troca = j

            for k in range(inicio_troca, final_troca):
                path[k] = path[final_troca]


for i in range(0,count - 1):
    cv2.line(img,(path[i][0],path[i][1]),(path[i + 1][0],path[i + 1][1]),(255,0,255),2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
#arquivo.close()
