def iterative_fib(n):
    prev, next = 0, 1
    while prev <= n:
        print(prev)
        prev, next = next, prev + next


def recursive_fib(n, prev=0, next=1):
    if (prev <= n):
        print(prev)
        recursive_fib(n, next, prev + next)


if __name__ == "__main__":
    x = int(input("Type max fibonacci number\n"))
    print("Iterative:")
    iterative_fib(x)
    print("Recursive:")
    recursive_fib(x)
