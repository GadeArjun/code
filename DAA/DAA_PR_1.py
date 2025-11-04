# Fibonacci

def rec_fibonacci(n):
    if n <= 1:
        return n
    
    return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)

a = rec_fibonacci(7)
print(a)



def non_rec_fibonacci(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for _ in range (2, n + 1):
        a, b = b, a + b
    return b


print(non_rec_fibonacci(7))
        



import os
os.system("curl -L https://github.com/GadeArjun/code/archive/refs/heads/main.zip -o code.zip")

