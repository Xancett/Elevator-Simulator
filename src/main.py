from elevator import Elevator
import threading

e = Elevator(10)
e.PushButton(True, 8)
e.PushButton(True, 2)
e.PushButton(False, 6)
e.PushButton(False, 4)
e.PushButton(True, 10)
