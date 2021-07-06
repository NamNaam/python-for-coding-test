#상하좌우

# 내 풀이
n = int(input())
command = list(input().split())
count = len(command)
x = 1
y = 1
i = 0

while count > 0 :
  if command[i] == 'R' :
    i += 1
    count -= 1
    if y == n :
      continue
    y += 1
  elif command[i] == 'L' :
    i += 1
    count -= 1
    if y == 1 :
      continue
    y -= 1
  elif command[i] == 'U' :
    i += 1
    count -= 1
    if x == 1 :
      continue
    x -= 1
  elif command[i] == 'D' :
    i += 1
    count -= 1
    if x == n :
      continue
    x += 1
  else :
    print('잘못된 입력')
    break

print(x, y)

# 교재 풀이
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
