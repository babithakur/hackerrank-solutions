#!/usr/bin/bash
read exp

result=`echo $(( $exp )) | bc -l`
rounded=`printf "%.3f" $result`
echo $rounded

