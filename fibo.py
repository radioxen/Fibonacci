# Fibonacci
#calculate fibonacci nth number
#run using Python3 fibo.py

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


if __name__ == __main__:
    n = eval(input("enter Nth number of Fibonacci series you want to calculate: "))
    print(Fibonacci(n))
