#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	//makeMaxNum();

	int n, m;
	vector<vector<int>> v;
	vector<int> arranged_v;
	scanf_s("%d %d", &n, &m);
	if ((n < 1 || n > 100) && (m < 1 || m > 100)) {
		return -1;
	}
	for (int i = 0; i < n; i++)
	{
		vector<int> tmp_v;
		for (int j = 0; j < m; j++)
		{
			int tmp;
			scanf_s("%d", &tmp);

			if (tmp < 1 || tmp > 10000)
				return -1;

			tmp_v.push_back(tmp);
		}
		v.push_back(tmp_v);
	}

	for (int k = 0; k < n; k++)
	{
		sort(v[k].begin(), v[k].end());
		arranged_v.push_back(v[k][0]);
	}
	sort(arranged_v.begin(), arranged_v.end());

	printf("%d", arranged_v[n - 1]);
	return 0;
}

void best(){
    int n, m;
    int result = 0;

    scanf_s("%d %d", &n, &m);

    for(int i = 0; i < n; i++)
    {
        int min_v = 100001;
        for(int j = 0; j < m; j++)
        {  
            int tmp;
            scanf_s("%d", &tmp);
            min_v = min(min_v, tmp);
        }
        result = max(result, min_v);
    }

    printf("%d", result);
}