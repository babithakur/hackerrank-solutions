#include<stdio.h>
int main() {
	int i, n, sum=0;
	scanf("%d", &n);
	for(i=0; i<5; i++){
		sum += n%10;
	}
	printf("%d", sum);	
	return 0;
}
