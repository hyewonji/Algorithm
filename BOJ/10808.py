'''
알파벳 소문자로만 이루어진 단어 S에 각 알파벳이 몇 개가 포함되어 있는지 확인하기

ex)
baekjoon
->
1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
'''

S = input()
alp = [0]*26
for i in S:
  alp[ord(i)-ord('a')]+=1
print(*alp)
