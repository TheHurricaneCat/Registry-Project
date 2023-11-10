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

class prodMod(Label):
    pass

class scroll(BoxLayout):
    pass

class ProductSelection(BoxLayout):
    def onProdPress(self):
        prodGrid = prodMod()
        global curProd
        curProd = self.ids.label1.text
        update()
        
class KeyPad(BoxLayout):
    pass 

#Main Grid
class TestGrid(Widget):
    def __init__(self, **kwargs):
        super(TestGrid, self).__init__(**kwargs)

        prodTitle = prodMod()
        self.ids.prodGrid.add_widget(prodTitle)
        
        global update
        def update():
            prodTitle.text = str(curProd)

        addScroll = scroll()
        self.ids.prodGrid.add_widget(addScroll)
        
        #Generate the Product List 
        for num in range(1, 13):
            productButton = ProductSelection()
            productButton.ids.varcont = str(num)
            productButton.ids.label1.text = str(num)
            addScroll.ids.prodContainer.add_widget(productButton)
        
        #Generate the Keypad
        keys = [7, 8, 9, 4, 5, 6, 1, 2, 3,"ENTER", 0, "DEL"]
        for num in keys:
            keyButton = KeyPad()
            keyButton.ids.button2.text = str(num)
            self.ids.keyContainer.add_widget(keyButton)

class TestApp(App):
    def build(self):
        Window.size = 730, (4*95)
        return TestGrid()
    
if __name__ == '__main__':
    TestApp().run()