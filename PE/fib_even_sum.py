a, b = input('Range from- '), input('Range to- ')
c, d = int(a), int(b)
first = 1
second = 2
next1 = 0
even_sum = 2
while next1 in range(c, d):
    #e = next1
    next1 = first + second	
    first = second
    second = next1
    #print( next1 ,' Fib series')
    if (next1 % 2) == 0:
       # print (next1,' Even Values')
        even_sum = even_sum + next1
print(even_sum) #Sum of even values.
	
        
    
