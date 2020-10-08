"""""""""
Simple code to grab important figures from Thomas' Calculus 13th Edition

by Daniel Li
"""""""""

import pyautogui
import pyscreenshot as ImageGrab

# configs determining whether or not to save the figures to the local disk as well as showing the images afterwards
SAVE_TO_DISK = True
SHOW_AFTER_FIND = False

# function to locate the figures within x amount of pages
def locate_figures(pages):
    # empty array to store image objects 
    figures = []

    for i in range(pages):
        try:
            # finds the coordinates of the light blue 'definition' box
            # uses OpenCV confidence parameter because sometimes, the blue edges are wacky
            tl_left, tl_top = pyautogui.locateCenterOnScreen(
                'topleft.png', confidence=0.8)
            br_left, br_top = pyautogui.locateCenterOnScreen(
                'bottomright.png', confidence=0.8)
        # Normally, you can't unpack return types of 'None' into two coordinates as shown above, but I created a workaround to do so.
        except TypeError:
            tl_left, tl_top = None, None
            br_left, br_top = None, None
        # Prints coords for debug purposes
        print(tl_left, tl_top)
        print(br_left, br_top)
        # Only take screenshot if coordinates exists
        if tl_left or tl_top or br_left or br_top is not None:
            ss_region = (tl_left, tl_top, br_left, br_top)
            # through testing, the 'mss' backend of screenshotting is the fastest
            image = ImageGrab.grab(
                bbox=ss_region, backend='mss', childprocess=False)
            figures.append(image)
        # supposed to scroll through page by page; doesn't work lol
        pyautogui.press('space')
    return figures


def show_figures(figures, save=False, show=True):
    if len(figures) == 0:
        print('No figures were found for the specified page range')
    else:
        if save:
            for i in range(len(figures)):
                figures[i].save(f'figure{i}.png')
        if show:
            for i in range(len(figures)):
                figures[i].show()


if __name__ == "__main__":
    figures = locate_figures(1)
    show_figures(figures, SAVE_TO_DISK, SHOW_AFTER_FIND)

    # color value of blue box for future reference: (15, 179, 236)
