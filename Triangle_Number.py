# Pattern of Triangle 1
n=int(input("Enter the number of rows: "))
for i in range(0,n):
    print(str(i)*i)
    
# Pattern of Triangle 2    
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(str(i)*i)

# Pattern of Triangle 3 with increasing numbers and same number in each row of the triangle
   
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(i), end="")
    print()
    
# Pattern of Triangle 4 with increasing numbers in each row of the triangle
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(j), end="")
    print()
