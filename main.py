import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
tx = []
all_sum = ''
biggest_exp = ''
err_txt = ''
category = ['education and culture','food','health and spents','taxes','entertaitment','other']
x = [0,0,0,0,0,0]
mcolors = ['brown','black','red','green','pink','purple']
mylabels = category

def minim(x):
    for num in x:
        if num != 0:
            tx.append(num)

def create_pie_graph(x):
    plt.figure(figsize =(3, 3))
    plt.pie(x,colors=mcolors)
    #plt.legend(labels=category,loc='upper right',prop={'size': 8})
    plt.legend(mylabels, bbox_to_anchor=(1,0), loc="lower right",bbox_transform=plt.gcf().transFigure)
    plt.title('expenses', fontsize=14)
    
    return plt.gcf()

def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()
    plt.close('all')

layout_l = [
    [sg.Text(err_txt,text_color="red",key='err')],
    [sg.Input(s=9,key=('inp')),sg.Combo(category, s=(15,22), enable_events=True, readonly=True, k='-COMBO-'),sg.Button('add',s=5,key="butt")],
    [sg.Text("  Result")],
    [sg.Text("the biggest expenses:")],
    [sg.Text(biggest_exp,key = 'biggest')],
    [sg.Text("the lowest expenses:")],
    [sg.Text(biggest_exp,key = 'lowest')],
    [sg.Text(all_sum,key = 'sum')],
    [sg.Exit()]
    ]

layout_r = [
    [sg.Canvas(key='-CANVAS-')],
    ]

layout = [
    [sg.Col(layout_l), sg.Col(layout_r)],
    ]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


window = sg.Window('account', layout, finalize=True, element_justification='upper right')

fig_agg = None
while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    elif event == "butt":
        not_none = True
        not_letter = True
        category_not_none = True
        not_minus = True

        categor = values["-COMBO-"]
        txt = values["inp"]
        if txt == '':
            err_txt = "input money" 
            not_none = False
            window['err'].update(err_txt)
        else:
            try:
                inp_val = int(txt)
                if inp_val<0:
                    not_minus = False
                    err_txt = "less than zero"
                    window['err'].update(err_txt)
            except:
                err_txt = "input number, not letters"
                not_letter = False
                window['err'].update(err_txt)
        if categor == '':
            err_txt = "choose the category"
            category_not_none = False   
            window['err'].update(err_txt)

        elif not_none == True and not_letter == True and category_not_none ==True and not_minus == True:
            for categ in category:
                if categ == categor:
                    x[category.index(categ)] = x[category.index(categ)]+inp_val
                    all_sum = 'all expenses: '+str(sum(x))
                    window['sum'].update(all_sum)
                    minim(x)
                    lowest_exp = category[x.index(min(x))]+" | "+str(min(tx))
                    biggest_exp = category[x.index(max(x))]+" | "+str(max(x))
                    window['biggest'].update(biggest_exp)
                    window['lowest'].update(lowest_exp)

            if fig_agg is not None:
                delete_fig_agg(fig_agg)
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas, create_pie_graph(x))
            
window.close()
