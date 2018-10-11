
#Implementación de mergesort
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
        

def mergeSort(A,p,r):
    if p < r:
        mid = (p+r)//2
        mergeSort(A,p,mid)
        mergeSort(A,mid+1,r)
        merge(A,p,mid,r)
