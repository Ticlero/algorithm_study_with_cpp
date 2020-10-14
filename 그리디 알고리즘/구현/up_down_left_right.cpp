#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
   int n;
   char* command = new char[200];
   vector<vector<pair<int, int>>> v;
   vector<pair<char, pair<int, int>>> comm_v;

   scanf("%d", &n);
   getchar();//stdin 버퍼 비우기
   fgets(command, sizeof(char) * 200, stdin);
   command[strlen(command) - 1] = '\0';

   for (int i = 0; command[i] != '\0'; i++)
   {
      switch (command[i])
      {
      case 'L':
         comm_v.push_back(make_pair(command[i], make_pair(0, -1)));
         break;
      case 'R':
         comm_v.push_back(make_pair(command[i], make_pair(0, 1)));
         break;
      case 'U':
         comm_v.push_back(make_pair(command[i], make_pair(-1, 0)));
         break;
      case 'D':
         comm_v.push_back(make_pair(command[i], make_pair(1, 0)));
         break;
      }
   }

   for (int i = 0; i < n; i++)
   {
      vector<pair<int, int>> tmp_v;
      for (int j = 0; j < n; j++)
      {
         pair<int, int> p = make_pair(i + 1, j + 1);
         tmp_v.push_back(p);
      }
      v.push_back(tmp_v);
   }
   int x = 0, y = 0;

   for (int i = 0; i < comm_v.size(); i++)
   {
      int tmp_x = x + comm_v[i].second.first;
      int tmp_y = y + comm_v[i].second.second;
      x = (tmp_x >= 0 && tmp_x < n)  ? tmp_x : x;
      y = (tmp_y >= 0 && tmp_y < n)  ? tmp_y : y;
   }

   printf("%d, %d\n", v[x][y]);

   return 0;
}