
def insertion_sort(arr):
    if arr==[] or arr == None:
        raise Exception("empty or None array")
    
    for i in range(1, len(arr)):
        j= i-1
        temp = arr[i]
        while j>=0 and temp<arr[j]:
            arr[j+1]= arr[j]
            j-=1
            arr[j+1]= temp
    return arr



arr1=[8,4,23,42,16,15]
            


print(insertion_sort(arr1))

