submit = [int(input()) for _ in range(10)]
number = [x%42 for x in submit]
print(len(set(number)))