#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>

using namespace std;

int main(void)
{
   int n, cnt = 0;;
   scanf("%d", &n);

   if (n < 0 || n > 23)
      return -1;

   for (int i = 0; i <= n; i++)
   {
      string h = to_string(i);   
      for (int j = 0; j < 60; j++)
      {
         string m = to_string(j);
         for (int k = 0; k < 60; k++)
         {
            string s = to_string(k);
            if ((h.find('3', 0) != string::npos) || (m.find('3', 0) != string::npos) || (s.find('3', 0) != string::npos))
            {
               cnt++;
            }
         }
      }
   }

   printf("%d\n", cnt);
   return 0;
}