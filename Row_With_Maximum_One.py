DA = [[1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]]

c = list(range(0, len(DA), 1))
temp = []
lower = 1
upper = len(DA[0])
Mid = round((upper - lower)/2)
cnt = 0
max_one = 0


def ctc(i_a, mid):

    global max_one, c, lower, upper, DA, temp
    print(lower, upper, mid)
    temp = []
    for b in c:
        if i_a[b][mid] == 1:
            print("t")
            max_one = b
            temp.append(b)

    if len(temp) == 0:
        print("Test 0", len(c))
        upper = mid
        mid = upper - round((upper - lower) / 2)
        ctc(DA, mid)
    elif len(temp) > 1:
        print("Test >1", len(c))
        lower = mid
        mid = lower + round((upper - lower) / 2)
        print(lower, upper, mid)
        c.clear()
        c = temp
        ctc(DA, mid)


ctc(DA, 4)
print(max_one + 1)

