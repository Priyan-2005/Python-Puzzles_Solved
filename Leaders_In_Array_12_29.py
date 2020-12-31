a = [3, 4, 12, 4, 3, 6, 4, 1]
Leader = []
SP = 1
print(a)
for t in a:
    for x in range(SP, len(a)):
        if t < a[x]:
            leader_Q = 0
            break
        elif t > a[x]:
            leader_Q = 1
    if leader_Q == 1:
        Leader.append(t)
    SP += 1
print(Leader)



