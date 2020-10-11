#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
/*
모험가 길드 알고리즘
모험가 n 명이 존재, 각각의 모함가들은 공포도 k를 가지고있음

파티를 맺고 여행을 가기 위해서는, 파티를 맺는 현재 그룹의 인원이 현재 보고있는 모험가의 공포도보다 크거나 같으면 그룹이 완성된다.
*/
int main(void)
{
	int n;
	vector<int> v;
	int cnt = 0;
	int result_group = 0;
	scanf_s("%d", &n);

	for (int i = 0; i < n; i++)
	{
		int tmp;
		scanf_s("%d", &tmp);
		v.push_back(tmp);
	}

	sort(v.begin(), v.end());
	
	for (int j = 0; j < n; j++)
	{
		cnt += 1; //그룹에 인원 추가
		if (cnt >= v[j])//현재 그룹의 인원 수가 추가된 인원의 공포도보다 크거나 같으면 그룹의 개수를 증가시키고 인원을 초기화
		{
			result_group++;
			cnt = 0;
		}
	}

	printf("%d\n", result_group);
	return 0;
}