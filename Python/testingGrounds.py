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

global prodInfo
prodInfo = [""]

global defaultMsg
defaultMsg = "ENTER THE QUANTITY"

#Classes for the product slice
class ProdMod(Label):
    pass

class ProdScroll(BoxLayout):
    pass

class ProdSelection(BoxLayout):
    global curProd
    curProd = defaultMsg
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
    curNum = defaultMsg
    def onKeyPress(self):
        global curNum
        global curProd
        global prodInfo
        if self.ids.button2.text == "DEL":
            curNum = defaultMsg
            updateKeys()
            print("Status: deleting quantity")
        elif self.ids.button2.text == "ENTER":
            if (curNum != defaultMsg and curProd != defaultMsg and int(curNum)*2 != 0):
                prodInfo = prodInfo + [str(curProd)]
                prodInfo = prodInfo + [str(curNum)]
                updateView()
                curNum = defaultMsg
                curProd = defaultMsg
                updateKeys()
                updateProd()
            else: 
                print("Error: quantity is zero or not stated ")
        else:
            if (curNum == "Default" or curNum == defaultMsg):
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
        print(self.ids.button4.text)

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
        global delElem
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
        def delElem():
            row = [i for i in addViewScroll.ids.viewScrollContainer.children]
            for child in row:
                addViewScroll.ids.viewScrollContainer.remove_widget(child)

class TestApp(App):
    def build(self):
        Window.size = 1100, (4*95)
        return TestGrid()
    
if __name__ == '__main__':
    TestApp().run()