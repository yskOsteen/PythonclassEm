#write a program that prompts users to enter three numbers and returns the largest number

a, b, c = map(int,input("Enter three numbers: ").split())

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:" , c)