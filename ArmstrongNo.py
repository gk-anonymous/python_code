number = int(input("Enter a number"))
length = len(str(number))

temp = number
sum = 0 

while temp>0:
    digit = temp % 10
    sum = sum + digit ** length
    temp = temp // 10
    
if sum==number :
    print("THiis Armstromg no")
else:
    print("Not Armstrong No")   