import PySimpleGUI as sg
import random as rd
yes = sg.Button("Click Here to see your computer specs")
yes1 = sg.Text("Computer Specs")
layout = [[yes1], [yes]]
window = sg.Window("Computer Specs", layout, margins=(600, 500))
def popup():
    hello = 0
    while hello < 100:
        x = rd.randint(0, 1700)
        y = rd.randint(-100,500)
        sg.popup_error('File Error', background_color='white', auto_close=False, text_color='black', location=(x, y))
        hello+=1
        if hello == 100:
            window.close()

while True:
    event, values = window.read()
    if event == "Click Here to see your computer specs":
        popup()
    if event == sg.WIN_CLOSED:
        break