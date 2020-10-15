import sys
loc = sys.stdin.readline().rstrip()

row = [1,2,3,4,5,6,7,8]
col = ["a","b","c","d","e","f","g","h"]

arr = [[0]*8 for _ in range(8)]

row_index = 0
col_index = 0

for i in range(8):
    for j in range(8):
        arr[i][j] = col[j]+str(row[i])
        if(arr[i][j] == loc):
            row_index = i
            col_index = j

command = [[1, -2], [-1, -2], [1, 2], [-1, 2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
count = 0
for i in command:
    if ( (row_index + i[0] >= 0 and row_index + i[0] < 8) and (col_index + i[1] >= 0 and col_index + i[1] < 8)):
        count += 1
print(count)