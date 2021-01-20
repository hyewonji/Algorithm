'''
문장의 개수 T와 문장이 주어졌을 때, 
단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 
단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있으며 단어와 단어 사이에는 공백이 하나 있다.
'''


#import sys를 이용해 시간 단축
import sys
T = int(input())

for i in range(T):
  a = sys.stdin.readline().split()
  for j in a:
    print(j[::-1],end=" ")
