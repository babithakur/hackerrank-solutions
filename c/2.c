#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>

int main(){
	char ch;
	char w[40];
	char s[100];
	scanf("%c\n", &ch);
	scanf("%s\n", &w);
	scanf("%[^\n]*c", &s);
	printf("%c\n", ch);
	printf("%s\n", w);
	printf("%s\n", s);

	return 0;
}

	
