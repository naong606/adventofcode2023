digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def findFirstDigit(str):
    for i in range(len(str)):
        if str[i].isdigit():
            return int(str[i])
        for j, digit in enumerate(digits):
            if str[i:i+len(digit)] == digit:
                return j+1
    return -1

def findLastDigit(str):
    for i in range(len(str)-1, -1, -1):
        if str[i].isdigit():
            return int(str[i])
        for j, digit in enumerate(digits):
            if str[i:i+len(digit)] == digit:
                return j+1
    return -1

def getCalibrationValue(str):
    return findFirstDigit(str) * 10 + findLastDigit(str)

result = 0
for s in ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]:
    result += getCalibrationValue(s)
print("example result = {}".format(result))

with open("input.txt", "r") as f:
    lines = f.readlines()
    print(sum(map(getCalibrationValue, lines)))