/comment 
    # ! Metodo Factorial
    # * Permite calcular la multiplicación de n*(n-1)*(n-2)...*(n-k) donde (n-k)>=1
    #@author edgar.benedetto@unah.hn
    #@version 0.1
uncomment/

def factorial(n)
    if n<2
        return 1
    end
    n*factorial(n-1)
end

n=5
#En ruby los datos no se devuelven como tuplas sino como arreglos
puts("El factorial en Python de '%d' es %d " % [n,factorial(n)])