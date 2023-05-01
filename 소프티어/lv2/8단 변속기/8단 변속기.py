import sys

input = sys.stdin.readline

line = list(map(int, input().split(" ")))

aflag, dflag = True, True

for idx in range(1, 8):
    if line[idx] - line[idx-1] != 1:
        aflag = False
    if line[idx] - line[idx-1] != -1:
        dflag = False

if aflag:
    print("ascending")
elif dflag:
    print("descending")
else:
    print("mixed")