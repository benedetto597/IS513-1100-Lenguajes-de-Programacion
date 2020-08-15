/comment


    # ! Método factorial.

    # * Permite calcular la multiplicación de n*(n-1)*(n-2)*...*(n-k), donde n-k >= 1

    # @author swd

    # @version 0.1


uncomment/
# Pruebe para que encuentre la solución en sus propias prácticas.

def factorial n

    if n<2

        return 1

    end

    puts "Hello World"
    n*factorial(n-1)
    puts 'Enter your name:'

end


name = "gets"
puts ("El factorial en Ruby para" n "es:" factorial(n) )

n = 5

def fact(n)
    if n == 0
      1
    else
      n * fact(n-1)
    end
  end

















