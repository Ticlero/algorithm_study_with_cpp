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


#define MAX_SIZE 1000000

char flip_char(char c)
{
	return c == '0' ? '1' : '0';
}

int main(void)
{
	string s;
	int cnt_zero = 0, cnt_one = 0, result = 0;

	cin >> s;

	if (s[0] == '1') {
		cnt_zero += 1;
	}
	else {
		cnt_one += 1;
	}

	// 두 번째 원소부터 모든 원소를 확인하며
	for (int i = 0; i < s.size() - 1; i++) {
		if (s[i] != s[i + 1]) {
			// 다음 수에서 1로 바뀌는 경우
			if (s[i + 1] == '1') cnt_zero += 1;
			// 다음 수에서 0으로 바뀌는 경우
			else cnt_one += 1;
		}
	}
	printf("%d", min(cnt_one, cnt_zero));
	return 0;
}