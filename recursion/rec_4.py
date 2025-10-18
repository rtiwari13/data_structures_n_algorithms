# Parameterised  Recursion 
# sum of n numbers 
 
# counting upwards from 1 to N
def sum_of_numbers(i, n , total):
    if  i>n:
        print(total)
        return  
    sum_of_numbers(i+1,n, total+i)      
sum_of_numbers(1,7 , 0)


# counting downwords from N to 1
def sum_of_n(i, total):
    if  i<1:
        print(total)
        return    
    sum_of_n(i-1, total+i) 
sum_of_n(7,0)