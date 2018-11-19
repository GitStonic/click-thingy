import pyautogui, threading, time

def start_app():
    print('Press Ctrl-C to quit')
    try:
        while True:
            pyautogui.press('esc')
            time.sleep(2)
            pyautogui.moveTo(1633, 933, 1.00)
            pyautogui.click(1633, 933)

            time.sleep(2)
            pyautogui.moveTo(646, 455, 1.00)
            pyautogui.click(646, 455)
            pyautogui.press('f2')

            time.sleep(10)
    except KeyboardInterrupt:
        print('\nDone.')

start_app()