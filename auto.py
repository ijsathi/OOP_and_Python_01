import pyautogui


def draw_pyramid(height):
    pyautogui.PAUSE = 0.1  
    width = height
    for i in range(1, height + 1):
        row = '#' * i
        pyautogui.typewrite(row)
        pyautogui.press('enter')


def main():
    while True:
        try:
            height = int(input("Take a number for the pyramid: "))
            if height <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")


    draw_pyramid(height)


main()