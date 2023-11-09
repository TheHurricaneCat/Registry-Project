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

class ProductSelection(BoxLayout):
    pass

class KeyPad(BoxLayout):
    pass 

class TestGrid(Widget):
    def __init__(self, **kwargs):
        super(TestGrid, self).__init__(**kwargs)
        
        #Generate the Product List
        for num in range(1, 13):
            productButton = ProductSelection()
            productButton.ids.label1.text = str(num)
            self.ids.prodContainer.add_widget(productButton)

        #Generate the Keypad
        keys = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0, "ENTER", "DEL"]
        for num in keys:
            keyButton = KeyPad()
            keyButton.ids.button2.text = str(num)
            self.ids.keyContainer.add_widget(keyButton)

class TestApp(App):
    def build(self):
        return TestGrid()
    
if __name__ == '__main__':
    TestApp().run()

    """
        #Main Grid
        self.cols = 3
        
        #Generate the title
        self.add_widget(Label(text="PRODUCT", 
            size_hint_y = None,
            height=100,
            ))
        self.add_widget(Label(text="KEYPAD", 
            size_hint_y = None,
            height=100
            ))
        self.add_widget(Label(text="OVERVIEW", 
            size_hint_y = None,
            height=100
            ))
        
        #Product Slice
        self.prodGrid = GridLayout()
        self.prodGrid.cols = 3

        for num in range(1, 13):
            self.submit = Button(text="Product " + str(num),
                size_hint_y = None, 
                height = 100,
                size_hint_x = None, 
                width = 100
                )
            self.prodGrid.add_widget(self.submit)
        self.add_widget(self.prodGrid)
        
        
        #Keypad Slice
        self.keyGrid = GridLayout()
        self.keyGrid.cols = 3
        
        keys = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0, "ENTER", "DEL"]
        for num in keys:
            self.submit = Button(text=str(num),
                size_hint_y = None, 
                height = 100,
                size_hint_x = None, 
                width = 100
                )
            self.keyGrid.add_widget(self.submit)
        
        self.add_widget(self.keyGrid)
       

        #Display and Enter Slice
        self.dispGrid = GridLayout()
        self.dispGrid.cols = 1
        
        self.dispGrid.add_widget(Label(text="LIST HERE"))
        
        self.submit = Button(text="ENTER")
        self.dispGrid.add_widget(self.submit)
        self.add_widget(self.dispGrid)
        """