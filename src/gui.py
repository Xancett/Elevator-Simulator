import PySimpleGUI as sg
class GUI:
    def __init__(self, model):
        self.model = model
        model.PassGUI(self)
    def CreateWindow(self):
        sg.Window(title="Elevator Simulator", layout=[[]], margins=(400, 400)).read()
    def UpdateElevatorLocation(self, location):
        print("Change label to ", location)