/*
    ! Metodo Factorial
    * Permite calcular la multiplicación de n*(n-1)*(n-2)...*(n-k) donde (n-k)>=1
    @ author edgar.benedetto@unah.hn
    @ version 0.1

    ! Para compilar codigo de c++ 
    ! g++ -o factorial factorial.cpp; ./factorial
    * g++ es el programa compilador.
    * -o es una banderá que le indica al compilador que el siguiente elemento es el archivo ejecutable y como se llamara.
    * ejecutable es el nombre del archivo que se ejecutara.
    * holaMundo.cpp es el nombre del código fuente.

*/

#include <iostream>

using namespace std;
int factorial(int);
int main(void) {
   int numero;
   cout<<"Factorial de 5 es: "<<factorial(5)<<endl;
   return 0;
}
int factorial(int n) {
   if(n < 0){
       return 0;
   }
   else if(n < 2){
       return 1;
   } 
   return n*factorial(n-1);
}
