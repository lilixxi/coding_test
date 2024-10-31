number = list(map(int, input().split()))
for i in range(len(number)):
    number[i] = int(str(number[i])[::-1])
print(max(number))