N,M = map(int,input().split())
busket = list(range(1,N+1))
for _ in range(M): 
  i,j = map(int,input().split())
  busket[i-1:j] = busket[i-1:j][::-1]
  # i-1 : 1부터 인덱스가 시작하니 
  # [::-1] 로 역순으로 바꿔준다 

for _ in busket:
  print(_,end=' ')