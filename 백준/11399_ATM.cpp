#include <stdio.h>
#include <algorithm>
#include <vector>
#include <stdlib.h>

using namespace std;

/*
사람수가 5이고 각 사람마다 ATM기기 사용하는데 걸리는 시간이 있다.

해결법 
오름차 순으로 사용하는데 걸리는 시간을 정렬
첫 번째 사람이 사용하는데 걸리는 총 시간은 사람 수만큼 더해진다
두 번째 사람이 사용하는데 걸리는 총 시간은 사람수-1 만큼 더해진다
세 번째 사람이 사용하는데 걸리는 총 시간은 사람수-2 만큼 더해진다.
...

예시 사람 5명 { 3 2 1 3 4 }

1
1+2
1+2+3
1+2+3+3
1+2+3+3+4

가장 적게 걸리는 시간인 1은 5개
두 번째로 적게 걸리는 시간인 2는 4개
세 번째로 적게 걸리는 시간인 3은 3개
네 번째로 적게 걸리는 시간인 3은 2개
마지막으로 적게 걸리는 시간인 4는 1개

*/

int main(int argc, char* argv[])
{
	int n;
	int result = 0;
	vector<int> v;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		int tmp;
		scanf("%d", &tmp);
		v.push_back(tmp);
	}

	sort(v.begin(), v.end());
	int spent_time = 0;
	for (int i = 0; i < v.size(); i++)
	{
		result = spent_time + v[i];
		v[i] = result;
		spent_time = result;
	}
	result = 0;
	for (int i = 0; i < v.size(); i++)
	{
		result += v[i];
	}

	printf("%d", result);
	return 0;
}

void best_answer()
{
	int n;
	int result = 0;
	vector<int> v;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		int tmp;
		scanf("%d", &tmp);
		v.push_back(tmp);
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < v.size(); i++)
	{
		result += v[i] * (n - i);
	}
    printf("%d", result);
}