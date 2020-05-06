# Version 2
# Teams daily check-in scheduler

import pyautogui
import time
from datetime import datetime

# Locations of images
teams_a_new_message_location = 'images\\a_new_message.png'
teams_a_new_conversation_location = 'images\\a_new_conversation.png'
teams_taskbar_icon_location = 'images\\teams_taskbar_icon.png'
teams_a_new_message = teams_a_new_conversation = teams_taskbar_icon = None
message = 'test'
monitors = 2


def initialize():
    global teams_a_new_message
    global teams_a_new_conversation
    global teams_taskbar_icon
    teams_a_new_message = pyautogui.locateCenterOnScreen(teams_a_new_message_location)
    teams_a_new_conversation = pyautogui.locateCenterOnScreen(teams_a_new_conversation_location)
    teams_taskbar_icon = pyautogui.locateCenterOnScreen(teams_taskbar_icon_location)


def click_and_write_something(click_location, message):
    # Main function of program. This is the most direct way to end the program.
    # Click, write, and send message.
    pyautogui.click(click_location)
    pyautogui.write(message)
    pyautogui.press('enter')
    exitProgramSuccessfully()


def exitProgramSuccessfully():
    print('---SUCCESS---, Exiting Program...')
    exit()


def attempt():
    if teams_a_new_message is not None:
        click_and_write_something(teams_a_new_message, message)
    if teams_a_new_conversation is not None:
        click_and_write_something(teams_a_new_conversation, message)
    print("Could not find Teams text box.")


# Brings Teams to foreground and moves it across screens.
# In the case of multiple monitors.
def activate_and_swap():
    pyautogui.click(teams_taskbar_icon)
    time.sleep(1)
    initialize()
    attempt()
    pyautogui.hotkey('win', 'shift', 'left')


if __name__ == "__main__":
    print("This program should be started with Teams and the desired chat/converation"
          "already on the Primary monitor and in the Foreground.")
    print("This version only runs once. Must be started again manually before the desired message sending time.")

    now = datetime.now()
    print(now.strftime('%H:%M:%S'))
    while True:
        time.sleep(1)
        now = datetime.now()
        print('Now = ', now.strftime('%H:%M:%S'))
        if now.strftime('%H') == '08':
            if now.strftime('%M') == '30':
                print("past main hurdle")
                initialize()
                attempt()
                time.sleep(1)
                break



    # The program should end successfully before this line.
    # However, we attempt to correct the situation
    # and bring Teams to the foreground on the primary monitor.
    for tries in range(monitors * 2):
        activate_and_swap()
        # TODO tries * 2 as a lazy work around. Clicking on taskbar icon can undesirably minimize teams.

print("Unsuccessful, exiting.")

'''
must be:
    on same screen
    'dark' theme (teams)
    computer unlocked?
'''

# TODO implement loop to reduce code. Done.
# TODO implement timing feature so program can be activated at certain times
# TODO allow program to be left open indefinitely so it never closes but still functions once a day.
# TODO more comments?
