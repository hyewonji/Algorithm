'''
H-index 문제

길이 n의 배열에서 h 이상인 수가 h개 이상인 최대값 h 구해라.
'''

# 첫번째 풀이
# for 중첩문 일때는 return으로 바로 값을 반환해 주면 for 문을 여러번 break할 필요가 없다.
def solution(citations):
  citations = sorted(citations)[::-1]

  if len(citations) == 1:
    return 1

  for i in range(citations[0],0,-1):
    for j,v in enumerate(citations):
      if v >= i and j+1 >= i:
        return i

  return 0

# 두 번째 풀이
# for문을 2개 쓸 필요가 없다.
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
