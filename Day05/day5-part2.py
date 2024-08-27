"""
with each seed

for each mapping option:
  if the seed is bigger than the source number (middle number) and smaller than the source number plus the stepcount (third number):
    mapping result is first number + (seed number - source number)
if no match made, output = seed number

"""

import re

f = open("input.txt")
seeds = [int(x) for x in re.findall(r'\d+', f.readline())]
seedRanges = list(zip(seeds[::2], seeds[1::2]))

# get map names and associated number ranges
mapsSplit = re.findall(r'([a-z-]+) map:|(\d+\s\d+\s\d+)+', f.read().replace("\n", " "))

# create a dictionary where Key = 'Map Name' and Values = a list of dictionaries, one dictionary per line, containing
# the Destination, Source, and RangeLength number values for each line.
# Simultaneously creates an ordered list of the maps since we need to know the order to do the data translation
mapsDict = {}
mapsOrdered = []
mapName = ""
for match in mapsSplit:
    if match[0]:
        mapName = match[0]
        mapsDict[mapName] = []
        mapsOrdered.append(mapName)
    else:
        destination, source, rangeLength = match[1].split()
        mapsDict[mapName].append({'destination': int(destination), 'source': int(source), 'rangeLength': int(rangeLength)})

locations = []

def attempt_translation(input, cypher):
    if cypher['source'] <= input <= (cypher['source'] + cypher['rangeLength']):
        # print(input, "is more than or equal to", cypher["source"], "and smaller than or equal to", (cypher['source'] + cypher['rangeLength']))
        return cypher['destination'] + (input - cypher['source'])
    else:
        return False


for seedRangeStart, seedRangeLength in seedRanges:
    for i in range(seedRangeStart, seedRangeStart + seedRangeLength):
        currentNumber = i
        print("working on:", seedRangeStart, ", current number:", currentNumber)
        for map in mapsOrdered:
            # print(map)
            for cypher in mapsDict[map]:
                # print("currentNumber:", currentNumber, "cypher:", cypher)
                translatedNumber = attempt_translation(currentNumber, cypher)
                if translatedNumber:
                    currentNumber = translatedNumber
                    break
        locations.append(currentNumber)

print(locations)
print(min(locations))