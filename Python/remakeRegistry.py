import openpyxl
from datetime import date

wb = openpyxl.load_workbook(r"C:/Users/Josefe Gillego/Documents/Special Project/Python/TestFile.xlsx")
ws = wb["Sheet1"]

# Get the column length and ignore whitespaced cells
currentLocation = 0
for i in range(1, ws.max_row):
    if ws["A" + str(i)].value != None:
        currentLocation = i

# Date | Product Code | Quantity | Invoice Number | Staff
colNames = ["A", "B", "C", "D", "E"]

# first element should be the staff 
itmDetails = [""]
line = 0

print("Enter the staff")
itmDetails[0] = input()

# handle multiple purchases
while (True):
    print("Enter the product code: ")
    itmDetails = itmDetails + [input()]
    if (itmDetails[line+1] == "D"):
        break
    line += 1
    print("Enter the item quantity")
    itmDetails = itmDetails + [input()]
    line += 1

# Initialize invoice number
invNum = str(ws["D" + str(currentLocation)].value)

# Write data
for column in range(5):
    for item in range(1, len(itmDetails)):
        if (column == 0): # write the date
            ws[str(colNames[column]) + str(currentLocation + 1 + item)] = date.today()
        elif (column == 1 and item%2 == 0 ): # write the product code
            ws[str(colNames[column]) + str(currentLocation + 1 + item)] = itmDetails[item]
        elif (column == 2 and item%2 > 0 ): # write the product code
            ws[str(colNames[column]) + str(currentLocation + 1 + item)] = itmDetails[item]
        elif (column == 3): # write the invoice number
            multi = False
            if (multi == False):
                ws[str(colNames[column]) + str(currentLocation + 1 + item)] = int(date.today().strftime('%y%m%d') + format(int(invNum[6:]) + 1, '004d'))
            else:
                ws[str(colNames[column]) + str(currentLocation + 1 + item)] = int(date.today().strftime('%y%m%d') + format(int(invNum[6:]), '004d'))
        elif (column == 4):
            ws[str(colNames[column]) + str(currentLocation + 1 + item)] = itmDetails[0]

wb.save(r"C:/Users/Josefe Gillego/Documents/Special Project/Python/TestFile.xlsx")

