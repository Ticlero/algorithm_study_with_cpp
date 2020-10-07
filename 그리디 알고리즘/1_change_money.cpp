/*
 * 거스름돈 문제 
 * 
*/
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[]) 
{
  int coin[4] = {500, 100, 50, 10};
  int n, cnt = 0;
  scanf("%d",&n);
  int i = 0;
  while(i < 4)
  {
    int tmp = n / coin[i];
    cnt += tmp;
    printf("%d\n", cnt);
    n %= tmp * coin[i];
    if(n == 0)
      break;
    i++;

  }

  printf("%d",cnt);
}