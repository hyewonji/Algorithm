'''
1부터 N까지의 수로 이루어진 순열이 있다.
이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성해라.
'''

N = int(input())
pmt = list(map(int,input().split()))

def next_permutation(num,arr):
  k = num-2
  if num == 1 : 
    print(-1)
  else:

    # 순열 뒤에서부터 arr[k]<arr[k-1]인 경우를 찾는다
    while True:
      if arr[k]<arr[k+1]:
        l = num-1

        # arr[k] 뒤에 오는 숫자 중, arr[k]보다 크고 가장 먼 인덱스 l을 찾는다.
        # arr[k]와 arr[l]을 바꿔준다.
        # arr[k] 뒤에 있는 숫자들을 뒤집는다.
        while True:
          if arr[k]<arr[l]:
            prop = arr[k]
            arr[k] = arr[l]
            arr[l] = prop
            arr[k+1:]=arr[k+1:][::-1]
            print(*arr)
            break
          else:
            l -= 1
        break
      else: 
        if k == 0:
          print(-1)
          break
        k -= 1

next_permutation(N,pmt)
