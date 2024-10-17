num = []
for i in range(9) : 
  number = int(input())
  num.append(number)
print(max(num))
print(num.index(max(num))+1)