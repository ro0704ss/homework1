def fibonacci(n):
    lsfibo = [1, 1]
    if n == 1:
        lsfibo.pop(1)
    else:
        for i in range(2, n):
            lsfibo.append(lsfibo[i-1]+lsfibo[i-2])
    return lsfibo

def num_list():
    lst = []
    while True:
        num = input()
        if num == 'done':
            break
        else:
            lst.append(int(num))
    return lst

def compare_abs_diff(lst):
    lastDiff = abs(lst[1] - lst[0])
    prevNum = lst[1]
    for i, x in enumerate(lst[2:]):
        diff = abs(x - prevNum)
        if diff <= lastDiff:
            return print('Were suck!')
        else:
            lastDiff = diff
            prevNum = x
    print('Expending')

def div_str(a, st):
    for i in range(1, len(st)):
        if not i % a == 0:
            print(st[i-1], end='')

def str_matrix(st1, st2):
    row1 = []
    row2 = []
    sorted_st1 = sorted(st1)
    for l in sorted_st1:
        if not l.isalpha():
            continue
        if l in row1:
            continue

        row1.append(l)
        if l in st2:
            row2.append(0)
        else:
            row2.append(1)

    sorted_st2 = sorted(st2)
    for l in sorted_st2:
        if not l.isalpha():
            continue
        if l in row1:
            continue
        row1.append(l)

        if l in st1:
            row2.append(0)
        else:
            row2.append(1)

    return [row1, row2]



