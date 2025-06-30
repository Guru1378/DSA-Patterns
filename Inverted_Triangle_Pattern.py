# Inverted Triangle Pattern 1
n=int(input("Enter the number of rows: "))
for i in range(n):
    print("*"*(n-i)+" "*(i))
    
# Inverted Triangle Pattern  with nested loops
n=int(input("Enter the number of rows: "))
for i in range (n,0,-1):
    for j in range (1,i+1):
        print("*",end="")
    print()
# This code prints an inverted right-angled triangle pattern of asterisks

# Inverted Triangle Pattern with decreasing numbers
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    print(str(i)*i)
   
# Inverted Trangle Pattern with nested loops
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(str(i), end="")
    print()
    
# Inverted Triangle Pattern with increasing numbers
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    print(str(n-i+1)*i)
# Inverted Triangle Pattern with nested loops and increasing numbers
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range (1,i+1):
        print(str(n-i+1), end="")
    print()
    
# inverted Triangle Pattern with increasing numbers in each row
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(str(j),end="")
    print()