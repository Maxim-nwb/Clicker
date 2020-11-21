import GUI
import keyboard
import mouse

# variables for storing the number of actions
cliks = 0
keystrokes = 0
# function for counting actions
def pressed(action, window):
    # checking the type to determine
    if isinstance(action, keyboard.KeyboardEvent):
        global keystrokes
        keystrokes += 1
        window.count_keystrokes.config(text="{0}".format(keystrokes))
    elif action == "c":
        global cliks
        cliks += 1
        window.count_cliks.config(text="{0}".format(cliks))

# main loop
window = GUI.Tk()
my_gui = GUI.MainWindow(window)
keyboard.on_press(lambda x: pressed(x, my_gui))
mouse.on_button(callback = pressed, args=("c", my_gui), buttons=('left', 'middle', 'right'), types=('down', 'double'))
window.mainloop()




