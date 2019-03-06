from pynput.mouse import Button, Controller
from time import sleep
import keyboard
import math

passme = True
pyn = Controller()
print("What is the time gap between each click (Can be a decimal)")
num = float(input())
print("Press S To Start and W To Stop)

print(num)
def check():
    if keyboard.is_pressed('w'):
        print("Quiting...")
        sleep(3)
        quit()


while True:
    if keyboard.is_pressed('s'):
        print("Starting...")
        sleep(1)
        for i in range(1,10000):
            check()
            sleep(num)
            check()
            pyn.press(Button.left)
            pyn.release(Button.left)
            check()
            print(i)
            check()
