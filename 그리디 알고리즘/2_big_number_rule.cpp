/*
    큰 수의 법칙
*/

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    vector<int> v;
    int n,m,k, sum = 0;

    scanf("%d %d %d",&n, &m, &k);
    if(k > m)
      return -1;
  
    for(int i=0; i < n; i++){
      int tmp;
      scanf("%d", &tmp);
      v.push_back(tmp);
    }
    
    sort(v.begin(), v.end());
    int first = v[n-1], second = v[n-2];

    printf("%d, %d\n", first, second);

    int s = (first * k) + second; 
    sum += s * (m/(k+1));
    int mod = m % (k+1);
    if( mod != 0)
    {
      sum += first * mod;
    }
    printf("%d", sum);
}