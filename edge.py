# https://supermarioemulator.com/mario.php

import sched
from time import sleep, time
import win32gui, win32ui, win32con, win32api

# http://www.kbdedit.com/manual/low_level_vk_list.html
VK_KEY_W = 0x57
VK_KEY_A = 0x41
VK_KEY_S = 0x53
VK_KEY_D = 0x44
VK_KEY_P = 0x50
VK_SHIFT = 0xA0

def main():
    # init window hanle
    window_name = "Super Mario Bros in HTML5 - Profile 1 - Microsoft​ Edge"
    #hwnd = win32gui.FindWindow(None, window_name)
    hwnds = find_all_windows(window_name)
    print("Num windows:" + str(len(hwnds)))

    sleep(1.0)

    s = sched.scheduler(time, sleep)

    offset_secs = 1.0
    for hwnd in hwnds:
        press_key(hwnd, s, VK_KEY_P, 0.1 + offset_secs, 0.1)
        press_key(hwnd, s, VK_KEY_D, 0.6 + offset_secs, 1.95)
        press_key(hwnd, s, VK_KEY_W, 2.5 + offset_secs, 0.9)
        press_key(hwnd, s, VK_KEY_D, 3.3 + offset_secs, 1.05)
        press_key(hwnd, s, VK_KEY_W, 3.5 + offset_secs, 0.8)

        offset_secs += 3.31
   
    s.run()

    
# send a keyboard input to the given window
def press_key(hwnd, s, key, start_sec, hold_sec):
    priority = 2
    duration = start_sec + hold_sec

    s.enter(start_sec, priority, win32api.SendMessage, 
            argument=(hwnd, win32con.WM_KEYDOWN, key, 0))      
    s.enter(duration, priority, win32api.SendMessage, 
            argument=(hwnd, win32con.WM_KEYUP, key, 0))

    # win32gui.SetForegroundWindow(hwnd)
    # win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    # sleep(sec)
    # win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)


def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds


def find_all_windows(name):
    result = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == name:
            result.append(hwnd)
    win32gui.EnumWindows(winEnumHandler, None)
    return result


main()
#list_window_names()
