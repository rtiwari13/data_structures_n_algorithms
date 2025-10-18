# Functional  Recursion 
# sum of n numbers 

def sum_of_n(N,sum):
    if N < 1:
        return sum
    
    return sum_of_n(N-1,sum+N)

add = sum_of_n(7,0)
print(add)


# another way 
def add_n(N):
    if N<1:
        return 0

    return N + add_n(N-1) 

sum = add_n(7)
print(sum)