count = int(input())
scores = list(map(int, input().split()))
max_score = max(scores) 
for i in range(count):
    scores[i] = scores[i] / max_score * 100 
print(sum(scores) / len(scores))  