import pyautogui
import time

class Ms_Bomb:
    def bomb(self):
        while True:
            time.sleep(3)
            pyautogui.typewrite(input("Enter Message: "))
            pyautogui.press('enter')

message_bomb = Ms_Bomb()       

message_bomb.bomb()
