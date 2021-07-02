# 곱하기 혹은 더하기

# 내 답안
s = list(map(int,input()))
sum = 0

if (s[0] == 0 or s[1] == 0) or (s[0] == 1 or s[1] == 1) :
  sum = s[0] + s[1]
else :
  sum = s[0] * s[1]
  
for i in range(2,len(s)) :
  if s[i] == 0 or s[i] == 1 :
    sum += s[i]
    if sum >= 2000000000 :
      sum -= s[i]
      break
  else :
    sum *= s[i]
    if sum >= 2000000000 :
      sum /= s[i]
      break

print(int(sum))


# 답
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
