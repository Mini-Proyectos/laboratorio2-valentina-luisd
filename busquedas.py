"""
busquedas.py
Luis Diaz; 15-10420
Valentina Aguana; 15-10111
"""

#insertion sort:
def InsertionSort(A,p,r):
    for j in range(p+1,r+1):
        key = A[j]
        i = j - 1
        while i >= p and A[i]>key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

#Merge sort, está conformado por dos funciones:
def merge(A,p,mid,r):
    
    lenLeft = len(A[p:mid+1:1])
    lenRigth = len(A[mid+1:r+1:1])

    L = [0 for i in range(lenLeft+1)]
    L[0:lenLeft:1] = A[p:mid+1:1]
    L[lenLeft] = 10**19

    R = [0 for i in range(lenRigth+1)]
    R[0:lenRigth:1] = A[mid+1:r+1:1]
    R[lenRigth] = 10**19

    i,j = 0,0
    for k in range(p,r+1):
        
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        elif L[i] > R[j]:
            A[k] = R[j]
            j += 1
        

def MergeSort(A,p,r):
    if p < r:
        mid = (p+r)//2
        MergeSort(A,p,mid)
        MergeSort(A,mid+1,r)
        merge(A,p,mid,r)
"""
### <--Zona de testeo--> ###
A = [2,1,5,6,8,3,2,4]
MergeSort(A,0,7)
print(A)
"""