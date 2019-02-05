#include <stdio.h>
#include <math.h>

int atoi(char * string){
	int i = num = sequence = 0;
	int sign = 1;
	int temp[10];
	for(;string[i] != '\0'; i++){
		if(string[i] == ' ')  continue;
		if(string[i] == '-' || string[i] == '+') {
			sign = 1 - 2 * (string[i] == '-'); 
			continue;
		}
		if(isIteger(string[i]) == -1) return 0;
		if(!sequence){
			sequence = i;
		}else{
			if (sequence+1 != i) return 0;
		}
		temp[num++] = isIteger(string[i]);
	}
	int value;
	num--;
	for(i = 0; num >= 0; num--){
		value += temp[i] * pow(10,num);
		i++;
	}
	return (value * sign);
}

int isInteger(char c){
	char[10] s = {'0','1','2','3','4','5','6','7','8','9'};
	int i;
	for(i = 0; i < 10; i++){
		if(c == s[i]){
			return i;
		}
	} 
	return -1;
}