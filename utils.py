import settings

#Calculate the sections height and width based on width and height of window
def height_percentage(percentage):
    return (settings.HEIGHT/ 100) * percentage

def width_percentage(percentage):
    return (settings.WIDTH / 100) * percentage