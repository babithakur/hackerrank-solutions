#!/usr/bin/bash
declare countries=()

i=0
while read line || [ -n "$line" ];
do
	countries[i]=$line
	i=$(( $i+1 ))
done

concat=("${countries[@]}" "${countries[@]}")
echo ${concat[@]}

