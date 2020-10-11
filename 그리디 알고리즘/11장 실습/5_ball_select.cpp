#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;
#define MAX_SIZE 1000000



int main(){
    int n, m;
	int result_cnt = 0;
	vector<int> v;
	scanf_s("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
	{
		int tmp;
		scanf_s("%d", &tmp);
		v.push_back(tmp);
	}

	for (int k = 0; k < v.size() - 1; k++)
	{
		for (int j = k+1; j < v.size(); j++)
		{
			if (v[k] != v[j])
				result_cnt++;
		}
	}

	printf("%d", result_cnt);
    return 0;
}

void best_answer()
{

	/*
	볼링의 각 무게들의 개수를 저장하는 변수를 만든다.
	A가 1의 무게를 선택했을 때, B는 1의 무게를 제외한 볼링공을 모두 선택할 수 있다.
	예를 들어 무게가 1 2 3 2 3인 볼링 공이 있을 경우
	A가 1의 무게를 선택했을 때, B는 무게 1과 다른 남은 볼링공이 4개 남았을 경우 4가지의 조합이 나타날 수 있다.
	마찬가지로 A가 2의 무게를 선택했을 때, 남은 공의 개수는 2개 이므로 4가지 조합이 나타난다.
	3을 선택한 경우 남은 공이 없으므로 0가지 조합이 나타난다. 즉 두 사람이 8가지의 조합으로 무게가 다른 공을 가질 수 있다.
	*/

	int n, m;
	int result_cnt = 0;
	int ball_list[11] = { 0 };
	vector<int> v;
	scanf_s("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
	{
		int tmp;
		scanf_s("%d", &tmp);
		v.push_back(tmp);
	}

	//무게별 볼의 개수를 저장
	for (int j = 0; j < v.size(); j++)
	{
		ball_list[v[j]] += 1;
	}

	for (int k = 1; k < 11; k++)
	{
		n -= ball_list[k];
		result_cnt += ball_list[k] * n;
		//printf("ball[%d] = %d\n", k,ball_list[k]);
	}
	printf("%d", result_cnt);
}