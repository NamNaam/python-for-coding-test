# 내 풀이
spot = list(input())

# 좌표로 변환
x = int(spot[1])
input_y = ['a','b','c','d','e','f','g','h']
for i in range(len(input_y)):
  if spot[0] == input_y[i] :
    y = i+1

# 총 경우의 수
dx = [-1, -2, -1, -2, 1, 2, 1, 2] # 위1 위2 위1 위2 아1 아2 아1 아2
dy = [-2, -1, 2, 1, -2, -1, 2, 1] # 왼2 외1 오2 오1 왼2 왼1 오2 오1

# 이동 가능 여부 확인
count = 0
for i in range(8) :
  if not (x + dx[i] < 1 or x + dx[i] > 8 or y + dy[i] < 1 or y + dy[i] > 8) :
    count += 1

print(count)

# 교재 풀이
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
