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

else

	echo "$num is less than 10"

fi