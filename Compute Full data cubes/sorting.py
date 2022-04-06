
def merge(lh,uh,arr,col):
    # this function merges the two sorted array into a sungle sorted array
    n,m,i,j,k = len(lh),len(uh),0,0,0
    # append elements into merged array till one of the two given array is exhausted
    while i< len(lh) and j < len(uh):
        if lh[i][col] <= uh[j][col]:
            arr[k] = lh[i]
            i+=1
        else:
            arr[k] = uh[j]
            j+=1
        k+=1
    arr[k:] = lh[i:] + uh[j:] # append the remaining elements when one of the two given array is exhausted

def mergeSort(arr,col):
    #base Case
    if len(arr) <= 1:
        return []
    
    mid = (len(arr)) //2
    
    #induction hypothesis for recursion
    lh = arr[0:mid]
    mergeSort(lh,col)
    
    uh = arr[mid:]
    mergeSort(uh,col)
    
    #induction step for recursion
    merge(lh,uh,arr,col)
    return arr
