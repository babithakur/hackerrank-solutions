#!/usr/bin/bash
read x
read y

if [ $x -eq $y ]
then
	echo "X and Y are equal"
elif [ $x -lt $y ]
then
	echo "X is less than Y"
else
	echo "X is greater than Y"
fi
