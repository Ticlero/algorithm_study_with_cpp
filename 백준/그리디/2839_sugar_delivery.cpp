#include <stdio.h>
#include <algorithm>
#include <vector>
#include <stdlib.h>

using namespace std;
/*
설탕 가게에 정확히 N 킬로그램을 모두 배달해야 함
설탕은 봉지에 담겨져 있는데 3킬로그램과 5킬로그램의 봉지가 있음
N킬로그램의 설탕을 배달할 때 가장 적게 드는 봉지 수를 구해라

처음에 생각했던 것..
3의 배수 개수와 5의 배수 개수들 사이의 연관 관계를 파악하려다 시간을 너무 많이 잡아먹음
5로 나누었을 때 가장 빠르게 해답이 나올 것이라 생각해여 나눗셈 연산으로 접근하여 복잡해 짐

풀이법
5의 배수의 숫자는 5로 나눈 몫이 가장 작은 숫자
이외에는 N킬로그램을 3으로 빼서 5의 배수로 만들어야 함
*/

int main(int argc, char* argv[])
{
	int n;
	int result = -1;

	scanf("%d", &n);

	if (n < 3){
		result = -1;
	}
	else
	{
		result = 0;
		while ( n >= 0)
		{

			if (n % 5 == 0) {
				break;
			}
			else {
				n -= 3;
				result++;
			}
		}

		if (n < 0)
			result = -1;
		else
			result += n / 5;
	}

	printf("%d", result);
	return 0;
}