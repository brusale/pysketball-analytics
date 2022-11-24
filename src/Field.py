import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from src.ShotCheck import *

class Field:

    def __init__(self):
        plt.rcParams['toolbar'] = 'None'

        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        
        self.ax.axis("off") #remove axes

        im = plt.imread("img/nba_court.jpg")
        self.ax.imshow(im)

        plt.connect('button_press_event', Field.AddEvent)
        
        plt.show()
        plt.draw()


    def AddEvent(event):
    
        if event.button is MouseButton.LEFT:
            shot = ShotCheck(event.xdata, event.ydata).TwoOrThreePoints()
            print(shot + " - MADE")
            plt.scatter(event.xdata, event.ydata, s=50, marker="o", color="red")

        if event.button is MouseButton.RIGHT:
            shot = ShotCheck(event.xdata, event.ydata).TwoOrThreePoints()
            print(shot + " - MISSED")
            plt.scatter(event.xdata, event.ydata, s=50, marker="x", color="red")
        
        plt.draw()
