# 숫자 카드 게임

# 내 답안
n, m = map(int,input().split())
min_value = []
result = 0

for _ in range(n):
  data = list(map(int,input().split()))
  data.sort()
  min_value.append(data[0])

for i in range(n-1):
  if min_value[i] < min_value[i+1]:
    result = min_value[i+1]
  else:
    result = min_value[i]

print(result)

# 교재 풀이
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력