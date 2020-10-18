import sys

result = 1
n, m = sys.stdin.readline().rstrip().split()
loc_info = sys.stdin.readline().rstrip().split()

pos = [int(loc_info[0]), int(loc_info[1])]
direction = int(loc_info[2])

#print(n, m)
#print(pos, direction)
map_info = [[0]*int(m) for _ in range(int(n))]
for i in range(int(n)):
    line = sys.stdin.readline().rstrip().split()
    for j in range(int(m)):
        map_info[i][j] = int(line[j])

#북 동 남 서
move = [[-1,0], [0,1], [1, 0], [0, -1]]
pre_moved = [[pos[0], pos[1]]]
cnt = 0
while (True):
    tmp_dir = direction-1 if direction-1 >= 0 else 3 #방향 설정
    tmp_row = pos[0] + move[tmp_dir][0] # 방향에 따라 상하 이동 row 이동
    tmp_col = pos[1] + move[tmp_dir][1] # 방향에 따라 좌우 이동 col 이동
    if(map_info[tmp_row][tmp_col] != 1 and cnt < 4): # 이동한 곳이 바다가 아니라면
        if(len(pre_moved) > 0): #방문 리스트에 데이터가 있다면
            flag = False
            for i in pre_moved:
                if([tmp_row, tmp_col] == i): #방문 리스트에 이동하려 하는 좌표가 이미 존재 하는지 판단
                    flag = True
                    cnt += 1
                    direction = tmp_dir
                    break
            
            if(flag == False): #방문했던 기록이 없으면
                pre_moved.append([tmp_row,tmp_col]) # 좌표 등록
                direction = tmp_dir
                pos[0] = tmp_row
                pos[1] = tmp_col
                result += 1
                cnt = 0
        # else:
        #     pre_moved.append([tmp_row,tmp_col])
        #     direction = tmp_dir
        #     pos[0] = tmp_row
        #     pos[1] = tmp_col
        #     result += 1
        #     cnt = 0
    elif cnt>3:
        if direction == 0:
            pos[0] -= 1
        elif direction == 1:
            pos[1] -= 1
        elif direction == 2:
            pos[0] += 1
        else:
            pos[1] += 1

        if(map_info[pos[0]][pos[1]] == 1):
            break
        else:
            cnt = 0
    else:
        direction = tmp_dir
        cnt+=1

print(result)