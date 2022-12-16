import PySimpleGUI as sg
import random

sg.theme("black")

# create a layout
layout = [
    [sg.Text('Dice Game')],
    [sg.Text('Enter your name')],
    [sg.InputText()],
    [sg.Button('Roll'), sg.Button('Exit')]
]

# create a window
window = sg.Window('Dice Game', layout)

# event loop
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Roll':
        print(f'{values[0]} rolled a {random.randint(1, 6)}')

window.close()