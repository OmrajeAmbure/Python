print("Enter any Three Number to compare ==> ")
num1 = input("enter the number num1 : ")
num2 = input("enter the number num2 : ")
num3 = input("enter the number num3 : ")

if(num1 > num2 and num1 > num3):
    print("largest number is ",num1)
elif(num2 > num1 and num2 > num3):
    print("largest number is ",num2)
elif(num3 > num1 and num3 > num2):
    print("largest number is ",num3)
