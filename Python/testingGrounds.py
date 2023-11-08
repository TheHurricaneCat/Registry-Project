import kivy 
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TestGrid(GridLayout):
    def __init__(self, **kwargs):
        super(TestGrid, self).__init__(**kwargs)
         
        #Main Grid
        self.cols = 3
        #Generate the title
        self.add_widget(Label(text="PRODUCT"))
        self.add_widget(Label(text="KEYPAD"))
        self.add_widget(Label(text="OVERVIEW"))
        
        #Product Slice
        self.prodGrid = GridLayout()
        self.prodGrid.cols = 3

        for num in range(1, 13):
            self.submit = Button(text="Product " + str(num))
            self.prodGrid.add_widget(self.submit)
        self.add_widget(self.prodGrid)
        
        
        #Keypad Slice
        self.keyGrid = GridLayout()
        self.keyGrid.cols = 3
        
        keys = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]
        for num in keys:
            self.submit = Button(text=str(num))
            self.keyGrid.add_widget(self.submit)
        self.submit = Button(text="ENTER")
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
        #Title
        self.add_widget(Label(text="Staff"))

        #Text input
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        #Button
        self.submit = Button(text="Submit")
        self.add_widget(self.submit)
        """

class TestApp(App):
    def build(self):
        return TestGrid()
    
if __name__ == '__main__':
    TestApp().run()