# 구현

# r과 c는 1부터 시작
# 맨해튼 거리 사용
# 0은 빈 칸, 1은 집, 2는 치킨집
# 도시의 치킨 거리=각 집의 치킨 거리합
from itertools import combinations
import math

N,M = map(int,input().split())
# graph=[]
houses=[]
chicken=[]
for i in range(N):
    temp=input().split()
    for j in range(N):
        if(temp[j]=='1'):
            houses.append((i,j))
        elif(temp[j]=='2'):
            chicken.append((i,j))
            # temp[j]=='0'
    # graph.append(temp)
    
# 조합으로 M개의 치킨집을 뽑아야함 <- key idea
combis = combinations(chicken,M)

d_min=math.inf
for combi in combis:
    # for i,j in combi:
    #     graph[i][j]='2'

    # 새로 만든 그래프에서 dfs로 치킨 거리 구하기 -> 어차피 house의 좌표를 알고, 치킨집의 좌표를 다 아니까 맨해튼 거리 차이의 min 값으로 구하면 되지 않나??
    sum=0
    for i,j in houses:
        d=[abs(c[0]-i)+abs(c[1]-j) for c in combi]
        sum+=min(d)
    if sum<d_min:
        d_min=sum

print(d_min)

# 그래프를 저장할 필요가 없었던 문제
