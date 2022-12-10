#https://www.bilibili.com/video/BV1B84y167SC/?spm_id_from=333.999.0.0&vd_source=03867f8876e8e07016615413fd5ed0b8
#用pyautogui插件实现文本自动输入
import time
import random
import pyautogui
time.sleep(2)#休眠2秒
words='i love you'
def write_line():
    for i in range(0, 10):
        pyautogui.write(words + ' ' + str(i))
        pyautogui.press('enter')
        time.sleep(2)

def write_char():

    with open("director\\1.txt",'r',encoding='u8') as f:
        lines = f.readlines()
    for i in lines:
        pyautogui.typewrite(i,interval="0.15")
        # pyautogui.typewrite(random.choice(lines),interval='0.15')
        pyautogui.press("enter")
        time.sleep(random.randint(1,3))

write_char()