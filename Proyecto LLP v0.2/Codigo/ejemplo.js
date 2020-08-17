
function factorial(n){

    if(n==1) return 1;

    if(n<1) return 0;

    return n*factorial(n-1);

}


function isInStock(n,m){

    if (n<m){
        console.log("Hay en Stock!");
    }else{
        console.error("No hay en Stock!");
    }
    while(n != m){
        console.error("Bye!");
        break;
    }
} 

isInStock(1,6);
console.log("El factorial de 4 es:", factorial(4));









