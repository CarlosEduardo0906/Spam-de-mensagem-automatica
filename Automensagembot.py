#Usar no terminal caso pyauto não esteja disponivel#
#pip install autogui#
import pyautogui as auto
from time import sleep

while True:
    auto.write('esse é o bot')
    auto.press('enter')
    sleep(0)