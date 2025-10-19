
# Reverse an array

def reverse_array(arr,left,right):
    
    if  right<left:
        return arr
    
    arr[left],arr[right] = arr[right],arr[left]

    return reverse_array(arr,left+1,right-1)
     
result = reverse_array([1,2,3,4,5],0,4)
print(result)

