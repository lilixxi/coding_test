N,M = map(int,input().split())
bag = [0] * N 

for _ in range(M):
  i,j,k = map(int,input().split())
  for x in range(i-1,j):
    bag[x] = k 

print(' '.join(map(str,bag)))