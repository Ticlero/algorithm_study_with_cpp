#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;
#define MAX_SIZE 1000000



int main(void)
{
	int n;
	int min_res = 1;
	vector<int> v;
	scanf("%d", &n);
	for(int i=0; i < n; i++){
		int tmp;
		scanf("%d", &tmp);
		v.push_back(tmp);
	}
	sort(v.begin(), v.end());
	
	for (int i = 0; i < v.size(); i++)
	{
		if (min_res < v[i])
			break;
		min_res += v[i];
	}

	printf("%d", min_res);

	return 0;
}