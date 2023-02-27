import PySimpleGUI as sg
import sqlite3
from db_interface import insert_contact

username = ''
password = ''

#Рядок виконання

def progress_bar():
    sg.theme('LightBlue2')
    layout = [[sg.Text('Creating your account...')],
            [sg.ProgressBar(300, orientation='h', size=(20, 20), key='progbar')],
            [sg.Cancel()]]
    
    window = sg.Window('Working...', layout)
    for i in range(300):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 10)
    window.close()

#Реєстрація

def create_account():
    #Вікно реєстрації
    
    sg.theme('LightBlue2')
    layout = [[sg.Text("Sign Up", size =(15, 1), font=40, justification='c')],
#             [sg.Text("E-mail", size =(15, 1),font=16), sg.InputText(key='-email-', font=16)],   Електронна пошта
             [sg.Text("Create Username", size =(15, 1), font=16), sg.InputText(key='-username-', font=16)],
             [sg.Text("Create Password", size =(15, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
             [sg.Text("Re-enter Password", size =(15, 1), font=16), sg.InputText(key='-rpassword-', font=16, password_char='*')],
             [sg.Button("Submit"), sg.Button("Cancel"), sg.Button("Sign in")]]

    window = sg.Window("Sign Up", layout)

    #Створення акаунту

    while True:
        event,values = window.read()
        connection = sqlite3.connect('contact_information.db')
        q = connection.cursor()
        q.execute('SELECT username FROM CONTACT_INFORMATION WHERE username = ?', (values['-username-'],))
        row = q.fetchone()
        connection.close()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Submit":
            if values["-password-"] == '' or values["-username-"] == '':
                sg.popup_error("Text is not defined", font=16)
            elif values['-password-'] != values['-rpassword-']:
                sg.popup_error("Incorrect password", font=16)
                continue
            elif row is None and values['-password-'] == values['-rpassword-']:
                window.close()
                progress_bar()
                insert_contact(values['-username-'], values['-password-'])
                login()
                break
            else:
                sg.popup_error("This account already exists", font=16)
        elif event == "Sign in":
            window.close()
            login()
            break
    window.close()

#Логін

def login():
    #Вікно логіна
    
    sg.theme("LightBlue2")
    layout = [[sg.Text("Sign In", size =(15, 1), font=40)],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-usrnm-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-pwd-', password_char='*', font=16)],
            [sg.Button('Ok'),sg.Button('Back')]]

    window = sg.Window("Log In", layout)

    #Перевірка

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Ok":
            connection = sqlite3.connect('contact_information.db')
            q = connection.cursor()
            q.execute('SELECT password FROM CONTACT_INFORMATION WHERE username = ?', (values['-usrnm-'],))
            row = q.fetchone()[0] #edited
            connection.close()
            if row:
                if values['-pwd-'] == row:   #Тут проблема
                    sg.popup("Welcome!")
                    break
                elif row != values['-pwd-']:
                    sg.popup("Invalid username or password. Try again")
                    continue
        elif event == "Back":
            window.close()
            create_account()

    window.close()


create_account()
