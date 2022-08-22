#Program to Find If a Number is Prime or Not without modulus(%) operator
input_Num= int(input("Enter your Number : "))
def prime(num):
    a=[]
    for i in range (1, num+1):
        if (num/i).is_integer():
            a.append(i)
    if len(a)==2:
        print("Prime")
    else:
        print("Not Prime")
prime(input_Num)
    
