def facto(num):
    
    fact = 1
    
    for i in range(1,num+1):
        fact*=i
    return fact 
        

d = facto(5)
print(d)