import PySimpleGUI as sg
class GUI:
    def __init__(self, model):
        self.model = model
        model.PassGUI(self)
    def CreateWindow(self):
        myLayout = [
            [sg.Text('Elevator location: '), sg.Text('0', key='-location-')]
        ]
        self.myWindow = sg.Window(title="Elevator Simulator", layout=myLayout, margins=(400, 400))
    def UpdateElevatorLocation(self, location):
        self.myWindow['-location-'].update(location)
        self.myWindow.refresh()
        