import PySimpleGUI as sg
import hashlib

sg.theme('Black')

layout = [[sg.Text("Enter username:", sg.Input(key='-USERNAME-', do_not_clear=True, size=(20, 1)))],
        [sg.Text("Enter password:"), sg.InputText('', key='-PASSWORD-', password_char='*', size=(20, 1))],
        [sg.Button("Submit"), sg.Button("Exit")]]

password_window = sg.Window('Login', layout, modal=True)

def verify_password(password):
        hash = ''
        password_utf = password.encode('utf-8')
        password_hash = hashlib.sha256(password_utf).hexdigest()
        if hash == password_hash:
            return True
        return False
    
def verify_username(username):
    user_username = []
    if username in user_username:
        return True
    return False

while True:
    event = password_window.read()
    values = password_window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        exit()
    elif event == "Submit":
        username_input_value = values['-USERNAME-']
        password_input_value = values['-PASSWORD-']
        if verify_password(password_input_value) and verify_username(username_input_value):
            break
        else:
            continue
    password_window.close()
