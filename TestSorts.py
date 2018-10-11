import sys #Para recibir los argumentos
import random #Para generar los arreglos
import busquedas #El archivo donde se guardan las funciones
import time #Para medir el tiempo

#Variables:
funcion = sys.argv[1]
n = int(sys.argv[2])
arreglo = []
tiempo = 0
#Programa:
for i in range(n):
    #Crea un arreglo aleatorio de números:
    arreglo.append(random.randint(1,n))

if funcion=="MergeSort":

    inicio = time.time()

    busquedas.MergeSort(arreglo,0,n-1)
    #p es 0 porque es el primer índice del arreglo, r es n-1 porque es el último.
    
    fin = time.time()
    tiempo = (fin - inicio)*1000
    
    print(funcion,n,tiempo)
elif funcion=="InsertionSort":

    inicio = time.time()

    busquedas.InsertionSort(arreglo,0,n-1)
    #p es 0 porque es el primer índice del arreglo, r es n-1 porque es el último.
    
    fin = time.time()
    tiempo = (fin - inicio)*1000
    
    print(funcion,n,tiempo)
else:
    print("Error: función no válida. funcion: ",funcion)

