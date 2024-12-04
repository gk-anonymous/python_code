def compound_int(p,r,t):
    amount = p * (pow((1+(r/100)),t))
    ci = amount - p 
    return ci
    
res = compound_int(10000, 10.25, 5)
print(res)