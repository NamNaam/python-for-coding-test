# 떡볶이 떡 만들기

# 내 풀이 (오답)
import sys

def binsearch(data, target, start, end):
	sum = 0
	if start > end:
		return not_find_data(data, target, data[end - 1], data[end])
	mid = (start + end) // 2
	for i in range(mid):
		sum += data[i] - data[mid]
	if sum < target :
		return binsearch(data, target, mid + 1, end)
	elif sum > target :
		return binsearch(data, target, start, mid - 1)
	else : # sum == target
		return data[mid]

def not_find_data(data, target, start, end):
	sum = 0
	if start < end:
		return start
	mid = (start + end) // 2
	for i in data:
		if i > mid:
			sum += i - mid
	if sum < target :
		return not_find_data(data, target, mid - 1, end)
	elif sum > target :
		return not_find_data(data, target, start, mid + 1)
	else : # sum == target
		return mid

n, m = map(int, input().split())
input_data = sys.stdin.readline().rstrip()
input_data = list(map(int, input_data.split()))
input_data.sort(reverse = True)
print(binsearch(input_data, m, 0, n - 1))

# 교재 풀이
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)
