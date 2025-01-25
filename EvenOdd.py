try:
    print("Enter The Number To Check Even or odd")
    number = int(input())
    if number%2==0:
        print("Enter Number is Even")
    elif number%2==1:
        print("Enter Number is odd")
    else:
        print("Enter Number is invalid")
except ValueError:
    print("Enter Value is Wrong")

