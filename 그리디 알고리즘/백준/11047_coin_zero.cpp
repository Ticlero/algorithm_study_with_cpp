#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b)
{
    return a > b;
}

int main(int argc, char* argv[])
{
	int n, k, cnt = 0;
	vector<int> v;
	scanf("%d %d", &n, &k);
	//printf("k = %d", k);
	for (int i = 0; i < n; i++)
	{
		int tmp;
		scanf("%d", &tmp);
		v.push_back(tmp);
		
	}

	sort(v.begin(), v.end(), compare);

	for (int i = 0; i < v.size(); i++)
	{
		if (k / v[i] != 0) // v[i]가 더 크다면
		{
			cnt += (k / v[i]);
			k = k % v[i];
		}
	}

	printf("%d\n", cnt);

	return 0;
}