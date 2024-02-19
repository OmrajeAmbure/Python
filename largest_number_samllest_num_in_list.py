"""
write a program calculat the largest number of list

"""
list1 = [10,208,333,659,526]
# for maximum number find out
maxi = 0
for i in list1:
        if i>=maxi:
           maxi = i 
print(maxi)  

# for minimum number find out
mini = list1[0]
for a in list1:
    if a < mini:
       mini = a
print(mini)   

# but in python can provide bulit in function
min_value = min(list1)
max_value = max(list1)
print('The Max value is ',max_value,'\nThe Min value is ',min_value)