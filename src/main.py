from elevator import Elevator
from gui import GUI
import threading

e = Elevator(10)
view = GUI(e)
view.CreateWindow()
e.PushButton(True, 8)
e.PushButton(True, 2)
e.PushButton(False, 6)
e.PushButton(False, 4)
e.PushButton(True, 10)
