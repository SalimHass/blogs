
def merge_sort(arr):
    if arr==[] or arr == None:
        raise Exception("empty or None array")
    
    n= len(arr)
    if n>1:
        mid =int(n/2)
        left= arr[0:mid]
        right=arr[mid:n]
        merge_sort(left)
        merge_sort(right)

        merge(left,right,arr)
    return arr
    
def merge(left,right,arr):
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1

        k+=1
    if i==len(left):
          for index in right[j:]:
            arr[k] = index
            k += 1
    else:
        for index in left[i:]: 
            arr[k] = index
            k += 1


    



arr1=[8,4,23,42,16,15]
arr2=[20,18,12,8,5,-2]
arr3=[5,12,7,5,5,7]
arr4=[2,3,5,7,13,11]
            


print(merge_sort(arr1))
print(merge_sort(arr2))
print(merge_sort(arr3))
print(merge_sort(arr4))


