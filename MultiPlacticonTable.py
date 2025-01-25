class MultPlactionTable:
    num1 = 0;
    def __init__(self,n1):
        self.num1 = n1;
    def printtable(self):
        for i in range(1,10):
            print(f"{self.num1} X {i} = ",self.num1*i)

def main():
    print("Enter The NUmber You Want To Display :- ")
    tablenum = int(input())
    table = MultPlactionTable(tablenum)
    table.printtable();

if __name__ == "__main__":
    main()


