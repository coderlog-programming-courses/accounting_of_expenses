import PySimpleGUI as sg
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
numbs = [12,56,100,200,5]
mcolors = ['blue','pink','red','green','black']
mylabels = ['education and culture','food','health and spents','taxes','entertainment']
def create_pie_graph(numbs):
    plt.figure(figsize =(7,5)) # graph size
    plt.pie(numbs)
    plt.legend(labels =mylabels,loc='upper right')
    plt.title('expenses',fontsize=50)
    
    
    return plt.gcf()

layout = [
    [sg.Canvas(size=(100,100), key='-CANVAS-')]
    ]



def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


window = sg.Window('window name', layout, finalize=True, element_justification='center')

draw_figure(window['-CANVAS-'].TKCanvas, create_pie_graph(numbs))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
        
window.close()