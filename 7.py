# 내 풀이
n = int(input())
x = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
count = 0

for i in range(n+1) :
    for j in range(60) :
        for k in range(60) :
            for three in x :
                if i == three :
                    count += 1
                    break
                if j == three :
                    count += 1
                    break
                if k == three :
                    count += 1
                    break
                print(i,j,k,count,three)

print(count)

# 교재 풀이
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
