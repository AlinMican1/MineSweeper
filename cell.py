from tkinter import Button, Label
import random
import settings
import ctypes
import sys
#We are making a cell for each square in the mine sweeper
class Cell:
    all = []
    cell_count_label_object = None

    cell_count = settings.CELL_COUNT
    #Initialize the cell giving a default value of false to the mine, and giving a none value to see if the button is a cell.
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.is_open = False
        self.is_mine_candidate = False

        #Append the object to the cell.all list so we can have all the instances in one place.
        #Cell.all is used to access the all variable
        Cell.all.append(self)
    
    #Create a button class that instantiates the button functionality to the cell
    #Give it a location to know in which frame to put the button in.
    def create_button_object(self, location):
        
        button = Button(
            location,
            width = 12,
            height= 4,
        )

        #Assign a event to a button
        #Bind is used to handle the pressed functionality, this <Button-1> represents left click. The second parameter is calling a function by REFERENCE.
        button.bind('<Button-1>', self.left_click_actions ) #LEFT CLICK
        button.bind('<Button-3>', self.right_click_actions ) #RIGHT CLICK
        self.cell_btn_object = button
    
    #Get a label to display all cells as a text.
    #It is a static method because we only need to call it once not all the time we instantiate a cell. Therefore we can remove self.
    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            text=f"Cells Left:{Cell.cell_count}",
            bg='black',
            fg='white',
            #can give it a font we want in the first parameter
            font=("",30)
        )
        Cell.cell_count_label_object = label


    #Event is used as a second parameter because TKinter passes two arguments.
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            #Check if the surrounded cells have 0 length if is true then we show
            #the surrounding cells aswell until one is not equl to 0.
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
    
    #Get cell object based on the value of x and y.
    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    #Makes it a read only so we dont change it
    @property
    def surrounded_cells(self):
        #Store the neightbours of the cell clicked so we can get if there is a mine or not
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x , self.y + 1),
        ]
        #Eliminate None values if corner cells are pressed e.g (0,0)
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    #Make it read only
    @property
    def surrounded_cells_mines_length(self):
        #Find the surrounding cells that are mines and return the count of nearby mines
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        
        return counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace the text of cell count label with newer count.
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                )
                #If this was a mine candidate then we should change the colour back to white
            self.cell_btn_object.configure(
                bg="SystemButtonFace"
            )
        #Mark this cell as opened so that we dont count cells twice
        self.is_open = True

    #Logic to interrupt the game and display msg that player lost    
    def show_mine(self):
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        self.cell_btn_object.configure(bg='red')
        sys.exit()

    
    #Right click button functionality
    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange',
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg = 'SystemButtonFace',
            )
            self.is_mine_candidate = False
    #A method that doesn't belong to each instance but instead the class is a static method
    @staticmethod
    def randomize_mines():
        #From all the cells pick 9 random ones to give it a mine.
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    #Magic methods are prebuilt methods, we are changing __repr__ to represent Cell.all data in a nicer way compare to a location in memory
    #like this <cell.Cell object at 0x0000028AB84E2740>
    def __repr__(self):
        return f"Cell({self.x},{self.y})"