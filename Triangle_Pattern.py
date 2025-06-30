n=int(input("Enter the number of rows: "))

for i in range(n+1):
    print("*"*i+" "*(n-i))
# This code prints a right-angled triangle pattern of asterisks
# where the number of rows is specified by the user input n.


m=int(input("Enter the number of rows: "))
for i in range(m):
    for j in range(i+1):
        print("*", end=" ")
    print()