from word2number import w2n

import time

# get the start time
st = time.time()

res = 0
digitWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

f = open("input.txt")
for line in f:
    numChars = ''
    for i in range(len(line)):
        if line[i].isnumeric():
            numChars += line[i]
        for digitWord in digitWords:
            if line[i:i+len(digitWord)] == digitWord:
                numChars += str(w2n.word_to_num(digitWord))
    val = numChars[0] + numChars[len(numChars)-1]
    res += int(val)

print(res)




# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')