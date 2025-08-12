print('Hello')

def sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print(f"Sum of squares from 1 to {n} is {sum_of_squares(n)}")
