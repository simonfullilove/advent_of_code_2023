import re
import time
st = time.time()

res = 0
colourLimits = {"red": 12,
                "green": 13,
                "blue": 14}

f = open("input.txt")
for line in f:
    possible = True
    splits = re.split(r', |; |: | |\n', line)
    print(splits)
    t = [(splits[i+1], splits[i]) for i in range(2, len(splits)-1, 2)]
    print(t)
    for c in t:
        if int(c[1]) > colourLimits[c[0]]:
            possible = False
            break
    if possible:
        res += int(splits[1])


print(res)


# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')