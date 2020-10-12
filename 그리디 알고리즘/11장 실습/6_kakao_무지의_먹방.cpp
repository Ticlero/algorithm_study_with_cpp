#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <stdio.h>
#include <string.h>
#include <queue>

using namespace std;
#define MAX_SIZE 1000000

/*
이 문제를 다루는데 있어 생각 했어야만 한 것들

1. 음식을 모두 먹는데 걸리는 시간이 오류가 나는 시간보다 작거나 같을 경우 남은 음식은 0이기 때문에 -1 반환

2. 음식들 중 가장 적게 걸리는 시간을 순서로 정렬 여기서는 우선순위 큐에 넣어 자동으로 오름차 순으로 정렬

3. 가장 적게 걸리는 음식을 모두 섭취하는데 걸리는 시간은
'시간 * 남아있는 음식의 개수' 이다.
다 먹었기 때문에 우선순위 큐에서 뺀다.

총 섭취 시간 += 주어진 시간 - 가장 적게 걸리는 음식을 모두 소비하는데 걸린 시간
남은 음식 -= 1
주어진 시간이 0과 같거나 작은지 비교


4. 그 다음 다 먹는데 가장 적게 시간이 걸리는 음식에 대해 같은 연산을 해준다.

'(시간 - 이전 음식 먹는데 소비되는 시간) * 남아있는 음식의 개수
총 섭취 시간 += 주어진 시간 - 두 번째로 적게 걸리는 음식을 모두 소비하는데 걸린 시간
남은 음식 -= 1
주어진 시간이 0과 같거나 작은지 비교

...


*/

int solution(vector<int> food_times, long long k);
bool compare(pair<int, int> p1, pair<int, int> p2)
{
	return p1.second < p2.second;
}

int main(void)
{
	vector<int> v;
	v.push_back(8);
	v.push_back(6);
	v.push_back(4);
	long long k = 15;

	printf("%d\n", solution(v, k));

	return 0;
}

int solution(vector<int> food_times, long long k) {


	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

	//음식을 다 먹는데 걸리는 시간이 주어진 시간이랑 같거나 작으면 남은 음식이 없는 것이므로 -1을 반환

	long long summary = 0;
	for (int i = 0; i < food_times.size(); i++)
	{
		summary += food_times[i];
	}

	if (summary <= k) return -1;

	//시간이 작은 음식부터 걸러내야 하므로 우선순위 큐를 이용
	for (int i = 0; i < food_times.size(); i++)
	{
		//(음식 시간, 번호) 형태로 우선순위 큐 삽입
		pair<int, int> p = make_pair(food_times[i], i + 1);
		pq.push(p);
	}

	summary = 0; //먹기 위해 사용한 시간
	long long previous = 0; //직전에 다 먹은 음식 시간
	long long length = food_times.size(); //남은 음식의 개수

	//먹기위해 사용한 시간 + ((현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수)와 k 비교
	while (summary + ((pq.top().first - previous) * length) <= k)
	{
		int now = pq.top().first;
		pq.pop();
		summary += (now - previous) * length;
		length -= 1; // 다 먹은 음식 제외
		previous = now; // 이전 음식 시간 재설정
	}

	// 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
	vector<pair<int, int> > result;
	while (!pq.empty()) {
		int food_time = pq.top().first;
		int num = pq.top().second;
		pq.pop();
		result.push_back({ food_time, num });
	}
	sort(result.begin(), result.end(), compare); // 음식의 번호 기준으로 정렬

	return result[(k - summary) % length].second;
}