"""
    ! Metodo Factorial
    * Permite calcular la multiplicación de n*(n-1)*(n-2)...*(n-k) donde (n-k)>=1
    @author edgar.benedetto@unah.hn
    @version 0.1
"""

def factorial(n):
    if(n<2): return 1
    return n*factorial(n-1)

m = 5
n = m
print("El factorial en Python de '%d' es %d" % (n,factorial(n)))