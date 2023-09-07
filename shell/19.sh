#!/usr/bin/bash
i=0
while read line || [ -n "$line" ];
do
	countries[i]=$line
	i=$(( $i+1 ))
done
ext=()
for i in "${countries[@]}";
do
	ext+=( "."${i:1} )
done

echo ${ext[@]}
