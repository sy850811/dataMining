def merge(lh,uh,arr,col):#merges the two sorted arrays into once sorted array
    n,m,i,j,k = len(lh),len(uh),0,0,0
    while i< len(lh) and j < len(uh):
        if lh[i][col] <= uh[j][col]:
            arr[k] = lh[i]
            i+=1
        else:
            arr[k] = uh[j]
            j+=1
        k+=1
    arr[k:] = lh[i:] + uh[j:]

def mergeSort(arr,col):
    #base Canse
    if len(arr) <= 1:
        return arr
    
    mid = (len(arr)) //2
    
    #induction hypothesis
    lh = arr[0:mid]
    mergeSort(lh,col)
    
    uh = arr[mid:]
    mergeSort(uh,col)
    
    #induction step
    merge(lh,uh,arr,col)
    return arr
