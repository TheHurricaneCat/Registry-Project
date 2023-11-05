"""
# Title, Qty, Staff, Invoice Number
titles = ["A", "B", "C", "D"]

cColumn = None
for i in range(2, 19):
    cRow = i
    rangelimit = 4
    
    for j in range(4):
        cColumn = titles[j] + str(cRow)
        if j == 3:
            print(currentSheet[cColumn].value)
        else:
            print(currentSheet[cColumn].value, end = " ")

print(currentSheet.max_row)
"""
"""
userInput = [""]
inputIndex = 0

while(userInput[inputIndex] != "D"):
    print("Enter an Element, otherwise enter D: ")
    userInput = userInput + [input()]
    inputIndex += 1
    

for element in userInput:
    print(element)
"""