#Forma Iterativa
def fib (n):
    aux=1
    fib=0
    for i in range (n):
        print(fib)
        aux += fib
        fib = aux - fib
fib(10)

print()

#Forma Recursiva
def fib_r(n):
    if n < 2:
        return n
    return fib_r(n-1) + fib_r(n-2)
for x in range(10):
    print(fib_r(x))
