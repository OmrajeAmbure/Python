class SumOfNaruralNumber:
    num1 = 0;
    def __init__(self,num):
        self.num1 = num
    def printSum(self):
        sum = 0
        for i in range(1,self.num1+1):
            print(i)
            sum = sum + i
        return sum

def main():
    print("Enter The Nmber To perform Sum Natural Number :- ");
    n = int(input());
    sumofnat = SumOfNaruralNumber(n)
    print(sumofnat.printSum());

if __name__ == "__main__":
    main()