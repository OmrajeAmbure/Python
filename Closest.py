class ClosestNumberOfDivision:
    def __init__(self, n, m):
        """Constructor to initialize n and m."""
        self.n = n
        self.m = m

    def printClosest(self):
        """Method to find and return the closest number divisible by m."""
        m = abs(self.m)  # Ensure m is positive
        for i in range(m + 1):
            if (self.n - i) % m == 0:  # Check smaller numbers
                return self.n - i
            elif (self.n + i) % m == 0:  # Check larger numbers
                return self.n + i

def main():
    # Example usage
    n = 27
    m = 4
    closest = ClosestNumberOfDivision(n, m)
    result = closest.printClosest()
    print(f"The closest number to {n} that is divisible by {m} is: {result}")


if __name__ == "__main__":
    main()
