# 정렬된 배열에서 특정 수의 개수 구하기

# 내 풀이
import sys
n, x = map(int, input().split())
data = sys.stdin.readline().rstrip()
data = list(map(int, data.split()))

def binary_search(data, target, start, end):
	if start > end:
		return -1
	mid = (start + end) // 2
	if data[mid] > target:
		return binary_search(data, target, start, mid - 1)
	if data[mid] == target:
		return count_target(data, mid, target, start, end)
	if data[mid] < target:
		return binary_search(data, target, mid + 1, end)

def count_target(data, target_index, target, start, end):
        count = 0
	for i in range(target_index, start - 1, -1):
		if data[i] == target:
			count += 1
		else:
			break
	for i in range(target_index + 1, end + 1): # 위와 겹치지 않기 위해 target_index에 1을 더함
		if data[i] == target:
			count += 1
		else:
			break
	return count

print(binary_search(data, x, 0, n - 1))

# 교재 풀이
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
