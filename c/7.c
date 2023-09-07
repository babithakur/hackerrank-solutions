#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
int main(){
	int a, b;
	scanf("%d\n%d", &a, &b);
	char *words[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "even", "odd"};
	for(int i=a; i<=b; i++){
		if(i <= 9){
			printf("%s\n", words[i-1]);
		}
		if(i > 9 && i%2==0){
			printf("%s\n", words[10]);
		}else if(i > 9 && i%2==1){
			printf("%s\n", words[11]);
		}
	}

	return 0;
}
