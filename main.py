import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('income', size = (16, 1)), sg.InputText(size = (10, 1), key='-IN-')],
            [sg.Text('education and culture', size = (16, 1)), sg.InputText(size = (10, 1))],
            [sg.Text('food', size = (16, 1)), sg.InputText(size = (10, 1))],
            [sg.Text('health and sports', size = (16, 1)), sg.InputText(size = (10, 1))],
            [sg.Text('insurance and taxes', size = (16, 1)), sg.InputText(size = (10, 1))],
            [sg.Text('entertainment', size = (16, 1)), sg.InputText(size = (10, 1))],
            [sg.Text('other', size = (16, 1)), sg.InputText(size = (10, 1))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Accounting of expenses', layout)
window.get_screen_size(width = 200, height = 100)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()