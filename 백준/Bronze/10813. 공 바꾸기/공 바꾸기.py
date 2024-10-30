n,m = map(int,input().split()) # 입력을 받는다 
busket = list(range(1,n+1)) # 1부터 n까지 있는 busket 을 만들어준다 
for _ in range(m) : # 교환 횟수(m) 만큼 반복해서 
  i,j = map(int,input().split()) # 바꿀 번호의 입력을 받아서 
  temp = busket[i-1]
  busket[i-1] = busket[j-1] # 서로 교환해준다 
  busket[j-1] = temp # 교환시 temp 필요 

for i in busket:
  print(i)