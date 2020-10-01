'''
N개의 수와 출력할 K번째 수가 입력된다.
N개의 수를 오름차순 정렬 후 K번째 수를 출력
'''

N, K = input().split()
arry = sorted(list(map(int,input().split())))
print(arry[int(K)-1])
