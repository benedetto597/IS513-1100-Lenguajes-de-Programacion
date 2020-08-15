#!/bin/bash
#Ejemplo1
# our comment is here

echo "The current directory is:"


echo "The user logged in is:"

#Ejemplo2
# User variables

grade = 5

person="Adam"

echo "$person is a good boy, he is in grade $grade"

#Ejemplo3
var1=$(( 5 + 5 ))
var2=$(( 5 + 5 * 4 ))
var3=$(( 5 + 5 / 4 + $(($var1 + 2)) ))

echo $var1

var2=$(( $var1 * 2 ))

echo $var2

#Ejemplo4
num=11

if [ $num -gt 10]; then

	echo "$num is bigger than 10"

elif [ $num -le 10]; then

	echo "$num is less than 10"

else 

	echo "$num is less than 10"
fi

#Ejemplo5
user="likegeeks"
user1="likegeeks"

if [ $user = $user1 ]; then

	echo "The user $user; is the current logged in $user1"

fi

#Ejemplo6
v1=text

v2="another text"

if [$v1 \> "$v2" ]; then

	echo "$v1 is greater than $v2"

else

	echo "$v1 is less than $v2"

fi

#Ejemplo7
for i in 1 2 3 4 5
do
 echo "Hello $i"
done

#Ejemplo8
for i in {1..5}
do
  if [["$i" == '4' ]]
  then
    continue
  fi
  echo "Hai $i4"
done

#Ejemplo9
for ciudad in Manila Bangkok Yakarta Kuala Lumpur
do
  if [[ "$ciudad" == 'Yakarta' ]]; then
    break
  fi
  echo "ciudad: $ciudad"
done

echo 'Sí, ¡eso es todo!'

#Ejemplo10
for i in {1..5}
do
  if [[ "$i" == '4' ]]
  then
    continue
  fi
  echo "Hai $i4"
done

#Ejemplo11
for ((i=1;i<$t;i++))
do
    if [ i % 4]
    then
        echo $i
    fi
done

#Ejemplo12
for ((i=1;i<=1000;i++))
do
    echo "$i.- Si yo hice algo malo y nadie me atrapó, ¿eso me hace bueno?"
done

#Ejemplo13
while :
do
	echo "infinite loops [ hit CTRL+C to stop]"
done

#Ejemplo14
x=1
while [ $x -le 5 ]
do
  echo "Welcome $x times"
  x=$(( $x + 1 ))
done

#Ejemplo15
counter=$t
factorial=1
while [ $counter -gt 0 ]
do
   factorial=$(( $factorial * $counter ))
   counter=$(( $counter - 1 ))
done
echo $factorial

#Ejemplo16
i=0
while [ $i -lt 1000 ]
do
    echo 'Cemento Fresco, no hay letrero más bello… bueno, sólo Alto Voltaje.'
    ((i++))
done

#Ejemeplo17

#initialize factorial
factorial=1
 
#for loop
for ((i=1;i<=num;i++))
do
    factorial=$(($factorial*$i))
done
 
echo "Factorial of $num is $factorial"