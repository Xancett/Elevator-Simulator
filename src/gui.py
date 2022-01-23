import PySimpleGUI as sg
class GUI:
    def __init__(self, model):
        self.model = model
        model.PassGUI(self)
    def CreateWindow(self):
        floors = []
        for k in range(1,11):
            floors.append('Floor ' + str(k))
        leftColumn = [
            [sg.Text('Outside')],
            [sg.Text('Floor '), sg.InputCombo(floors, key='-floorSelection-', default_value='Floor 1', enable_events=True)],
            [sg.Button('Up', disabled_button_color='Gray')],
            [sg.Button('Down', disabled=True, disabled_button_color='Gray')]
        ]
        rightColumn = [
            [sg.Text('Inside')],
            [sg.Button(button_text=i) for i in range(1,4)],
            [sg.Button(button_text=i) for i in range(4,7)],
            [sg.Button(button_text=i) for i in range(7,10)],
            [sg.Button(button_text=i) for i in range(10,11)]
        ]
        myLayout = [
            [sg.Text('Elevator location: '), sg.Text('1', key='-location-')],
            [sg.Column(leftColumn), sg.VSeperator(), sg.Column(rightColumn)]
        ]
        self.myWindow = sg.Window(title="Elevator Simulator", layout=myLayout, margins=(400, 400))
        while True:
            event, values = self.myWindow.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            # Check if picking a floor
            if event.isnumeric():
                self.model.ChooseFloor(int(event))
            # Check if a floor is requested
            else:
                if (event == "Up" or event == "Down"):
                    print("Request at floor, ", values['-floorSelection-'])
                else:
                    # Set buttons to disabled/enabled if on top or bottom floor
                    self.myWindow['Up'].update(disabled=(values['-floorSelection-'] == "Floor 10"))
                    self.myWindow['Down'].update(disabled=(values['-floorSelection-'] == "Floor 1"))
        self.myWindow.close()
    def UpdateElevatorLocation(self, location):
        self.myWindow['-location-'].update(location)
        print("Location: ", location)
        self.myWindow.refresh()
        