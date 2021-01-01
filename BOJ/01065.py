'''
재귀함수

첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

* 한수 : 어떤 양의 정수 X의 각 자리가 등차수열을 이루는 수
'''

num = int(input())
hansu = 0

for n in range(1, num+1) :
    if n <= 99 : # 1부터 99까지는 모두 한수
        hansu += 1 
    
    else :     
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
            hansu+=1
