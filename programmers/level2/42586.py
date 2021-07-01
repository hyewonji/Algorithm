from math import ceil 

def solution(progresses, speeds):
    max_day = None
    count = 1
    answer = []
  
    # for p, s in zip(progresses, speeds): 
    # zip을 사용해 풀이 가능
    for i,v in enumerate(progresses):
      day = math.ceil((100-v)/speeds[i])
    
      if i == 0:
        max_day = day
      elif max_day >= day:
        count += 1
      else:
        answer.append(count)
        max_day = day
        count = 1
    answer.append(count)

    return answer
