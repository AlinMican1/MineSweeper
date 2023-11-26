from tkinter import Button
import random
#We are making a cell for each square in the mine sweeper
class Cell:
    all = []
    #Initialize the cell giving a default value of false to the mine, and giving a none value to see if the button is a cell.
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #Append the object to the cell.all list so we can have all the instances in one place.
        #Cell.all is used to access the all variable
        Cell.all.append(self)
    
    #Create a button class that instantiates the button functionality to the cell
    #Give it a location to know in which frame to put the button in.
    def create_button_object(self, location):
        
        button = Button(
            location,
            text=f'{self.x},{self.y}',
            width = 12,
            height= 4,
        )

        #Assign a event to a button
        #Bind is used to handle the pressed functionality, this <Button-1> represents left click. The second parameter is calling a function by REFERENCE.
        button.bind('<Button-1>', self.left_click_actions ) #LEFT CLICK
        button.bind('<Button-3>', self.right_click_actions ) #RIGHT CLICK
        self.cell_btn_object = button
    
    #Event is used as a second parameter because TKinter passes two arguments.
    def left_click_actions(self, event):
        print("I am batman")
    
    #Right click button functionality
    def right_click_actions(self, event):
        print("I am retarded")

    #A method that doesn't belong to each instance but instead the class is a static method
    @staticmethod
    def randomize_mines():
        pass

    
    #Magic methods are prebuilt methods, we are changing __repr__ to represent Cell.all data in a nicer way compare to a location in memory
    #like this <cell.Cell object at 0x0000028AB84E2740>
    def __repr__(self):
        return f"Cell({self.x},{self.y})"