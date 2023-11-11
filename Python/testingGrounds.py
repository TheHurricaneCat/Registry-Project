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
from kivy.uix.layout import Layout
from kivy.properties import StringProperty

import random

global prodInfo
prodInfo = [""]

# classes for the product slice
class prodMod(Label):
    pass

class scroll(BoxLayout):
    pass

class ProductSelection(BoxLayout):
    global curProd
    curProd = "Default"
    def onProdPress(self):
        global curProd
        curProd = self.ids.label1.text
        updateProd()
        
# classes for the quantity slice
class KeyContainer(BoxLayout):
    pass

class KeyMod(Label):
    pass

class KeyPad(BoxLayout):
    global curNum
    curNum = "Default"
    curNum = ""
    def onKeyPress(self):
        global curNum
        global prodInfo
        if self.ids.button2.text == "DEL":
            curNum = "ENTER THE QUANTITY"
            updateKeys()
            curNum = "Default"
        elif self.ids.button2.text == "ENTER":
            prodInfo = prodInfo + [str(curProd)]
            prodInfo = prodInfo + [str(curNum)]
            
            if(curProd != "Default" and curNum != "Default"):
                updateView()
                curNum = ""
            else:
                print("NO SELECTED ITEMS")
        else: 
            if (curNum == "ENTER THE QUANTITY" or curNum == "Default"):
                curNum = ''
            curNum = curNum + str(self.ids.button2.text)
            updateKeys()
    pass 

# classes for overview slice
class ViewContainer(BoxLayout):
    pass

class ViewMod(Label):
    pass

class ViewPad(BoxLayout):
    def onClearPress(self):
        print(self.ids.button3.text)
    def onEnterPress(self):
        print(self.ids.button4.text)

#Main Grid
class TestGrid(Widget):
    def __init__(self, **kwargs):
        super(TestGrid, self).__init__(**kwargs)

        #Generate the Product List 

        prodTitle = prodMod()
        self.ids.prodGrid.add_widget(prodTitle)

        addScroll = scroll()
        self.ids.prodGrid.add_widget(addScroll)
        
        products =  ["Apple", "Banana", "Berry", "Watermelon", "Grapes", "Strawberry", "Pineapple", "Lemon"]
        for num in products:
            productButton = ProductSelection()
            productButton.ids.varcont = num
            productButton.ids.label1.text = num
            addScroll.ids.prodContainer.add_widget(productButton)
        
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
        
        addConfirm = ViewContainer()
        self.ids.viewGrid.add_widget(addConfirm)
        
        confirmButton = ViewPad()
        addConfirm.ids.viewContainer.add_widget(confirmButton)

        #Update changes
        global updateProd
        global updateKeys
        global updateView
        def updateProd():
            prodTitle.text = str(curProd)
            prodTitle.background_color = (random.uniform(0, 0.5),random.uniform(0, 0.5),random.uniform(0, 0.5),1)
        def updateKeys():
            keyTitle.text = str(curNum)
        def updateView():
            viewTitle.text = str(prodInfo)
            curProd = "Default"
            curNum = "Default"
            prodTitle.text = "ENTER THE PRODUCT"
            prodTitle.background_color = (0,0,0,1)
            keyTitle.text = "ENTER THE QUANTITY"
            

class TestApp(App):
    def build(self):
        Window.size = 730, (4*95)
        return TestGrid()
    
if __name__ == '__main__':
    TestApp().run()