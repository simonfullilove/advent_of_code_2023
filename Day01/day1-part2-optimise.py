from word2number import w2n

import time

# get the start time
st = time.time()

res = 0
digit3Words = ["one", "two", "six"]
digit4Words = ["four", "five", "nine"]
digit5Words = ["three", "seven", "eight"]

f = open("input.txt")
for line in f:
    numChars = ''
    for i in range(len(line)):
        if line[i].isnumeric():
            numChars += line[i]
        if line[i:i+3] in digit3Words:
            numChars += str(w2n.word_to_num(line[i:i+3]))
        if line[i:i+4] in digit4Words:
            numChars += str(w2n.word_to_num(line[i:i+4]))
        if line[i:i+5] in digit5Words:
            numChars += str(w2n.word_to_num(line[i:i+5]))
    val = numChars[0] + numChars[len(numChars)-1]
    res += int(val)

print(res)




# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')