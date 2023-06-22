"""_summary_
"""
set_a = set(map(int, input().split()))
time = int(input())
FLAG = 0

for i in range(time):
    set_b = set(map(int, input().split()))
    if set_a.issuperset(set_b):
        FLAG += 1
    else:
        FLAG = 0
if FLAG > 1:
    print(True)
else:
    print(False)
    
