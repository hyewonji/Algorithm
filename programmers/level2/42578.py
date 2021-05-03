'''
clothes가 주어질때, 서로 다른 옷의 조합의 수를 구해라.

1. clothes는 [의상의 이름, 의상의 종류]의 리스트이다.
2. len(clothes) <= 30
3. 같은 이름을 가진 의상은 존재하지 않는다.
4. clothes의 모든 원소는 길이 1 이상 20 이하의 문자열이다.
5. 스파이는 하루에 최소 한 개의 의상을 입는다.
'''


# 첫번째 풀이 - 시간초과
from itertools import combinations
from functools import reduce

def solution(clothes):

  clothes_obj = {}
  answer = 0

  for cloth in clothes:
    cloth_type = cloth[1]
    if cloth_type in clothes_obj.keys():
      clothes_obj[cloth_type] += 1
    else:
      clothes_obj[cloth_type] = 1

  if len(clothes_obj) == 1:
    answer = len(clothes)
  else: 
    for i in range(len(clothes_obj)):
      nums_comb = list(combinations(clothes_obj.values(),i+1))
      for nums in nums_comb:
        answer += reduce(lambda x, y: x * y, nums)

  return answer


# 두번째 풀이
# combination을 사용할 필요가 없다.(collections함수 이용)
import collections

def solution(clothes):
    answer = 1
    kind = []
    
    for a, b in clothes:
        kind.append(b)
        
    kind = collections.Counter(kind)
    
    for i in kind.values():
    	answer *= (i + 1)
    
    return answer - 1
