import threading
import sqlite3 as lite
import kivy 
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup

import random

import openpyxl
from datetime import date

global prodInfo
prodInfo = ["Staff Name"]

global defaultNumMsg
defaultNumMsg = "ENTER THE QUANTITY"

global defaultProdMsg
defaultProdMsg = "ENTER THE PRODUCT"

global staffFile
staffFile = "C:/Users/Josefe Gillego/Documents/Special Project/Python/staff.txt"

with open(staffFile) as f:
    global staffList
    staffList = f.read().splitlines()
    print(staffList)
    f.close()

#Classes for the product slice
class ProdMod(Label):
    pass

class ProdScroll(BoxLayout):
    pass

class ProdSelection(BoxLayout):
    global curProd
    curProd = defaultProdMsg
    def onProdPress(self):
        global curProd
        curProd = self.ids.label1.text
        updateProd()
        
#Classes for the quantity slice
class KeyContainer(BoxLayout):
    pass

class KeyMod(Label):
    pass

class KeyPad(BoxLayout):
    global curNum
    curNum = defaultNumMsg
    def onKeyPress(self):
        global curNum
        global curProd
        global prodInfo
        if self.ids.button2.text == "DEL":
            curNum = defaultNumMsg
            updateKeys()
            print("Status: deleting quantity")
        elif self.ids.button2.text == "ENTER":
            if (curNum != defaultNumMsg and curProd != defaultProdMsg and int(curNum)*2 != 0):
                prodInfo = prodInfo + [str(curProd)]
                prodInfo = prodInfo + [str(curNum)]
                updateView()
                curNum = defaultNumMsg
                curProd = defaultProdMsg
                updateKeys()
                updateProd()
            else: 
                if (curNum == defaultNumMsg and curProd == defaultProdMsg): 
                    error = StaffError()
                    error.open()
                    error.title = "Error: No product or quantity chosen"
                    print("Error: quantity is zero or not stated ")
                elif (curNum == defaultNumMsg or int(curNum)*2 == 0): 
                    error = StaffError()
                    error.open()
                    error.title = "Error: No quantity entered or is zero"
                    print("Error: quantity is zero")
                elif (curProd == defaultProdMsg): 
                    error = StaffError()
                    error.open()
                    error.title = "Error: No product chosen"
                    print("Error: product is not stated ")
        else:
            if (curNum == "Default" or curNum == defaultNumMsg):
                curNum = ""
            curNum = curNum + str(self.ids.button2.text)
            updateKeys()

#Classes for overview slice
class ViewContainer(BoxLayout):
    pass

class ViewMod(Label):
    pass

class ViewScroll(BoxLayout):
    pass

class ViewPad(BoxLayout):
    def onClearPress(self):
        delElem()
        print(self.ids.button3.text)
    def onEnterPress(self):
        if (currStaff != ""):
            processData()
            print(self.ids.button4.text)
        else:
            error = StaffError()
            error.open()
            error.title = "Error: No staff selected"

class ViewSelection(BoxLayout):
    global index 
    index = 1
    def removeItem(self):
        global prodInfo
        prodInfo[self.index+1] = ""
        prodInfo[self.index] = ""
        print(self.index)
        print(prodInfo)
        self.parent.remove_widget(self)

#Classes for staff slice
class StaffPad(BoxLayout):
    def selectStaff(self):
        print("deselecting")
    def confirmStaff(self):
        updateCurrentStaff()
        
class StaffSelection(BoxLayout):
    global currStaff
    currStaff = ""
    def updateStaff(self):
        global currStaff
        currStaff = self.ids.staffTitle.text
        staffEntry.ids.currentStaff.text = currStaff
        confirmation = StaffConfirm()
        confirmation.open()
        confirmation.title = "Set <" + currStaff + "> as the current staff?"
        
class StaffConfirmation(Popup):
    def __init__(self, **kwargs):
        super(StaffConfirmation, self).__init__(**kwargs)
        for person in staffList:
            staffEntry = StaffSelection()
            staffEntry.ids.staffTitle.text = str(person)
            self.ids.staffContainer.add_widget(staffEntry)
    def confirmStaff(self):
        staffEntry = StaffSelection()
        global currInput
        currInput = self.ids.textInput.text
        if (currInput != ""):
            staffEntry.ids.staffTitle.text = currInput
            self.ids.staffContainer.add_widget(staffEntry)
            self.ids.textInput.text = currInput + " is successully added!"
            f = open(staffFile,"a+")
            f.write("\n")
            f.write(currInput)
            f.close()
        else:
            error = StaffError()
            error.open()
            error.title = "Error: No input"
    def clearField(self):
        self.ids.textInput.text = ""

class StaffError(Popup):
    pass

class StaffConfirm(Popup):
    def setStaff(self):
        self.dismiss()
        staffEntry.dismiss()
        updateCurrentStaff()

#Main Grid
class TestGrid(Widget):
    def __init__(self, **kwargs):
        super(TestGrid, self).__init__(**kwargs)

        #Generate the Product List 

        prodTitle = ProdMod()
        self.ids.prodGrid.add_widget(prodTitle)

        addProdScroll = ProdScroll()
        self.ids.prodGrid.add_widget(addProdScroll)
        
        products =  ["Apple", "Banana", "Berry", "Watermelon", "Grapes", "Strawberry", "Pineapple", "Lemon","Apple", "Banana", "Berry", "Watermelon", "Grapes", "Strawberry", "Pineapple", "Lemon"]
        for num in products:
            productButton = ProdSelection()
            productButton.ids.varcont = num
            productButton.ids.label1.text = num
            addProdScroll.ids.prodContainer.add_widget(productButton)
        
        #Generate the Keypad
        keyTitle = KeyMod()
        self.ids.keyGrid.add_widget(keyTitle)

        addKeys = KeyContainer()
        self.ids.keyGrid.add_widget(addKeys)
        
        keys = [7, 8, 9, 4, 5, 6, 1, 2, 3,"ENTER", 0, "DEL"]
        for num in keys:
            keyButton = KeyPad()
            keyButton.ids.button2.text = str(num)
            addKeys.ids.keyContainer.add_widget(keyButton)

        #Generate the overview

        viewTitle = ViewMod()
        self.ids.viewGrid.add_widget(viewTitle)
        
        addViewScroll = ViewScroll()
        self.ids.viewGrid.add_widget(addViewScroll)
        
        addConfirm = ViewContainer()
        self.ids.viewGrid.add_widget(addConfirm)
        
        confirmButton = ViewPad()
        addConfirm.ids.viewContainer.add_widget(confirmButton)

        #Update changes
        global updateProd
        global updateKeys
        global updateView
        global updateCurrentStaff
        global delElem
        global processData
        def updateProd():
            prodTitle.text = str(curProd)
        def updateKeys():
            keyTitle.text = str(curNum)
        def updateView():
            global index
            addProductView = ViewSelection()
            addProductView.ids.viewTitle.text = prodInfo[-1-1]
            addProductView.ids.viewQuantity.text = str("Qty:") + " " + prodInfo[-1]
            addProductView.index = index
            addViewScroll.ids.viewScrollContainer.add_widget(addProductView)
            index = index+2
            print(prodInfo)
        def updateCurrentStaff(): 
            print("updating")
            self.ids.staffTitle.text = "Current Staff: " + currStaff
            prodInfo[0] = currStaff
        def processData():
            for space in prodInfo:
                if (space == ""):
                    del prodInfo[space]
            excelProcess()
            delElem()
        def delElem():
            row = [i for i in addViewScroll.ids.viewScrollContainer.children]
            for child in row:
                addViewScroll.ids.viewScrollContainer.remove_widget(child)
            prodInfo[1:] = ""
            global index
            index = 1
            print(prodInfo)
        def excelProcess():
            wb = openpyxl.load_workbook(r"C:/Users/Josefe Gillego/Documents/Special Project/Python/TestFile.xlsx")
            ws = wb["Sheet1"]

            # Get the column length and ignore whitespaced cells
            currentLocation = 1
            for i in range(1, ws.max_row):
                if ws["A" + str(i)].value != None:
                    print(currentLocation)
                    currentLocation += 1

            # Write data in excel
            colNames = ["A", "B", "C", "D", "E"]

            # Initialize invoice number
            invNum = str(ws["D" + str(currentLocation - 1)].value)
            print(invNum)
            print(prodInfo)

            for column in range(5):
                # writing the date, staff and invoice number
                def writeExcel(identifier, data):
                    ws[str(colNames[column]) + str(currentLocation + item - identifier)] = data
                
                for item in range(1, int((len(prodInfo)) / 2) + 1):
                    if (column == 0): 
                        writeExcel(1, date.today())
                    if (column == 3): 
                        multi = False
                        if (multi == False):
                            writeExcel(1, int(date.today().strftime('%y%m%d') + format(int(invNum[6:]) + 1, '004d')))
                            multi = True
                        else:
                            writeExcel(1, int(ws[str(colNames[column]) + str(currentLocation - 1)]))
                    if (column == 4):
                            writeExcel(1, prodInfo[0])
                # write the product code and quantity
                identA = 1
                identB = 2
                for item in range(1, len(prodInfo)):
                    if (column == 1 and item%2 != 0):
                        writeExcel(identA, prodInfo[item])
                        identA += 1
                    if (column == 2 and item%2 == 0): 
                        writeExcel(identB, int(prodInfo[item]))
                        identB += 1

            wb.save(r"C:/Users/Josefe Gillego/Documents/Special Project/Python/TestFile.xlsx")
            print("excel written")

    def activatePopup(self):
        global staffEntry
        staffEntry = StaffConfirmation()
        staffEntry.open()
        self.ids.staffTitle.background_color = random.uniform(0.5, 0.8), random.uniform(0.5, 0.8), random.uniform(0.5, 0.8), 1
    
class TestApp(App):
    def build(self):
        Window.size = 1100, (4*120)
        return TestGrid()
    
if __name__ == '__main__':
    TestApp().run()
