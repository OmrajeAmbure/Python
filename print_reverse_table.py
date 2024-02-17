"""
   print reverse table in python 
   
"""
num = int(input("Enter a number: "))

print(f"Reverse table of {num}:")
for i in range(10, 0, -1):
    result = num * i
    print(f"{num} x {i} = {result}")