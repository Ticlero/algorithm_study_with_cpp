#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <stdio.h>
#include <string.h>

using namespace std;

#define MAX_SIZE 21

int plus_fun(int x, int y)
{
	return x + y;
}

int multi_fun(int x, int y)
{
	return x * y;
}

int main(void)
{
	int result = 0;
	//char* s = (char*)malloc(sizeof(char) * 100);

	char* s = new char[MAX_SIZE];
	fgets(s, sizeof(char) * MAX_SIZE, stdin);
	s[strlen(s) - 1] = '\0';
	printf("%s\n", s);
	for (int i = 0; s[i] != '\0'; i++)
	{
		if (s[i] == '0' || s[i] == '1' || result == 1 || result == 0 ) {
			//char형 int로 바꾸는 방법 - '\0' 을 붙여준다.
			//숫자 0~9의 시작은 아스키넘버 48이다 48을 빼주면 정수를 얻을 수 있다.
			result = plus_fun(result, s[i]-48);
			printf("1. s[%d] = %d\n",i, s[i]);
		}
		else {
			result = multi_fun(result, s[i] - 48);
		}
	}

	printf("%d", result);
	/*string s;
	getline(cin, s);
	printf("%s", s.c_str());*/
	

	
	return 0;
}