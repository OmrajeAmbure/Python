print("Enter The Markas your FIVE Subject : ")
sub1 = int(input("sub1"))
sub2 = int(input("sub2"))
sub3 = int(input("sub3")) 
sub4 = int(input("sub4"))
sub5 = int(input("sub5"))

sum = (sub1+sub2+sub3+sub4+sub5)
avg = sum/500*100

print("The sum of student = ",sum,"And Avrage is : ",avg)

if(avg >= 40 and avg <= 60):
    print("Grade : Second Class")
if(avg >= 60 and avg <= 75):
    print("Garde : First Class")
if(avg >= 75 and avg <= 90):
    print("Garde : First Class Dist")
if(avg >= 90 and avg <= 100):
    print("Grade : Distanction")
else:
    print("Your Fail")