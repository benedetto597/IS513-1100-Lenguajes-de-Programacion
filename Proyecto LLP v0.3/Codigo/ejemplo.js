
   
function factorial(n){
   

    if(n==1) return 1;

    if(n<1) return 0;

    return n*factorial(n-1);

}


function isInStock(n){

    if (n<1){
        console.log("Hay en Stock!");
    }else{
        console.error("No hay en Stock!");
    }
    while(n == 1){
        console.log("Bye!");
        break;
    }
    if(n<2) console.error("lo iso");
    while(n == 1){
        console.error("error");
        console.error("total");
        break;
    }

    for(s=0;s<5;s++){
        console.error("Entro");
    }
    ultra = n;

} 

isInStock(1);
console.log("El factorial de 4 es:", factorial(4));
