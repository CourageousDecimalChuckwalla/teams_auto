import pyautogui

teams_a_new_message = pyautogui.locateCenterOnScreen('images\\a_new_message.png')
teams_a_new_conversation = pyautogui.locateCenterOnScreen('images\\a_new_conversation.png')
teams_taskbar_icon = pyautogui.locateCenterOnScreen('images\\teams_taskbar_icon.png')
message = 'test'


def initialize_again():
    print('inside initialize again')
    global teams_a_new_message
    global teams_a_new_conversation
    global teams_taskbar_icon
    teams_a_new_message = pyautogui.locateCenterOnScreen('images\\a_new_message.png')
    teams_a_new_conversation = pyautogui.locateCenterOnScreen('images\\a_new_conversation.png')
    teams_taskbar_icon = pyautogui.locateCenterOnScreen('images\\teams_taskbar_icon.png')
    pass


def click_and_write_something(clickable, writable=None):
    pyautogui.click(clickable)
    if writable is None:
        pyautogui.write('test')
    else:
        pyautogui.write(writable)
    pyautogui.press('enter')
    return 0


def activate_and_swap():
    print('inside activate_and_swap')
    pyautogui.click(teams_taskbar_icon)
    pyautogui.hotkey('win', 'shift', 'left')
    initialize_again()


if __name__ == "__main__":
    if teams_a_new_message is None and teams_a_new_conversation is None:
        print("Could not find \"teams - a new message\" or 'teams - a new conversation'")
        print("activating teams window")
        activate_and_swap()
        if teams_a_new_message is None and teams_a_new_conversation is None:
            activate_and_swap()

    if teams_a_new_message is not None:
        print("Found \"a new message\"")
        if (click_and_write_something(teams_a_new_message, message)) is 0:
            print('Executed Successfully')

    if teams_a_new_conversation is not None:
        print("Found 'a new conversation'")
        if (click_and_write_something(teams_a_new_conversation, message)) is 0:
            print('Executed Successfully')

print('Exiting...')

'''
must be:
    on same screen
    dark theme (teams)
    computer unlocked?
'''

# TODO implement loop to reduce code
