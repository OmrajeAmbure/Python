"""
sum of natural number 

"""
num = int(input("Enter the number you wnat to print natural number :- "))
sum_n1 = 0
sum_n2 = 0
# it is run from liner time O(n)
for i in range(1, num+1):
    sum_n1 +=  i
print(f'output is : {sum_n1}')
# it is run form constant time O(1)
# it is much more faster algorithm 
sum_n2 = (num*num+num)/2
print (f'output is :- {sum_n2}')
    