import re
import time

st = time.time()

res = 0

f = open("input.txt")
for line in f:
    colourMax = {"red": 0, "blue": 0, "green": 0}
    splits = re.split(r', |; |: | |\n', line)
    print(splits)
    t = [(splits[i+1], splits[i]) for i in range(2, len(splits)-1, 2)]
    print(t)
    for c in t:
        if int(c[1]) > colourMax[c[0]]:
            colourMax[c[0]] = int(c[1])
    product = 1
    for value in colourMax.values():
        print(value)
        product *= value
    res += product



print(res)


# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')