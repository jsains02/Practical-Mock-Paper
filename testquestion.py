s = [1]
NUMBER_TO = 500
perfect = []
ZERO = 0
calculate = ZERO
for i in range(NUMBER_TO+1):
    for j in range(2, i):
        if i % j == 0:
            s.append(j)
    for a in s:
        calculate += int(a)
    if calculate == i:
        perfect.append(i)
    s=[1]
    calculate = ZERO

print(perfect)