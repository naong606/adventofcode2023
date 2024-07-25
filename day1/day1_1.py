def getCalibrationValue(str):
    digits = [int(c) for c in str if c.isdigit()]
    return digits[0] * 10 + digits[-1]

# result = 0
# for s in ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]:
#     result += getCalibrationValue(s)
# print(result)

with open("input.txt", "r") as f:
    lines = f.readlines()
    print(sum(map(getCalibrationValue, lines)))