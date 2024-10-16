import sys
# 입력의 종료조건이 없는 경우 
for line in sys.stdin:
    try:
        A, B = map(int, line.split())
        print(A + B)
    except:
        break