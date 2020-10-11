#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minus_fun(int x)
{
	return x - 1;
}

int divide_fun(int x, int k) {
	return x / k;
}

int main(void)
{
	int n, k;
	int cnt = 0;
	while(1){
		printf("입력>>");
		scanf_s("%d %d", &n, &k);
		if (n < k)
			return -1;
		if (n < 2 || n > 100000)
			return -1;
		if (k < 2 || k>100000)
			return -1;

		while (n != 1)
		{
			if (n % k != 0){
				n = minus_fun(n);
				cnt++;
			}
			else{
				n = divide_fun(n, k);
				cnt++;
			}
		}

		printf("%d\n", cnt);
	}
	
	return 0;
}