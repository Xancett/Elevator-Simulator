from elevator import Elevator
import threading

e = Elevator(10)
e.PushButton(True, 8)
e.PushButton(True, 2)
e.PushButton(False, 6)
e.PushButton(False, 4)
e.PushButton(True, 10)
# should be 2,8,10,6,4
# ended up being 10, 10, 4, 8, 6, 2, 10