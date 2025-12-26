t = int(input("Enter the number for the first part of the shape: "))

for i in range(t):
    print(" "*(t-i)+"*"*i+"*"+"*"*i)

for j in range(t+1):
    print(" "*j+"*"*(t-j)+"*"+"*"*(t-j))