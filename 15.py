s = [i / 4 for i in range(57000 * 4, 978000 * 4)]
mn = 10000
for index1 in range(len(s) - 1):
    for index2 in range(index1 + 1, len(s)):
        start, end = s[index1], s[index2]
        k = 0
        for x in s:
            f = (123456<=x<=760123) <= (not(57892<=x<=478683) <= ((not(592916<=x<=977654) and (not(start<=x<=end))) <= (not(123456<=x<=760123))))
            if f == 0:
                k += 1
        if k == 0:
            mn = min(mn, end - start)
print(mn)
