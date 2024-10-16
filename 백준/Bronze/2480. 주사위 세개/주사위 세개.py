def dice():
  a,b,c = map(int, input().split())
  if a==b==c :
    return 10000 + a*1000
  elif (a==b) or (a==c) :
    return 1000 + a*100
  elif b==c :
    return 1000 + b*100
    # 따로 해준이유 곱해주는 값의 기준이 달라지기에
  else :
    return max(a,b,c)*100
print(dice())