'''
1. nums 배열 중, 3개의 수를 고른다.
2. 세 수의 합이 소수인 경우의 수를 구한다.
'''

# 첫번째 풀이
# is_prime에서 3000까지의 소수를 구한 후 combination의 합과 비교
def is_prime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

def solution(nums):
  from itertools import combinations
  answer = 0

  prime_nums = []
  for i in range(3001):
    if(is_prime(i)):
      prime_nums.append(i)

  for i in combinations(nums,3):
    if sum(i) in prime_nums:
      answer += 1
      print(i, answer)

  return answer


# 개선된 코드
# combination의 합에 해당하는 슷자만 소수인지 확인
def solution(nums):
    
  from itertools import combinations as cb
  answer = 0

  for i in cb(nums,3):
    sum_i = sum(i)
    for j in range(2,sum_i):
        if sum_i%j==0:
            break
    else:
        answer += 1
      
  return answer
