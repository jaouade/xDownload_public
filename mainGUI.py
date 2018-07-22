from tkinter import *
from tkinter import ttk
import os

def btnBuscarEBaixar_Click():
    pesquisa = str(txtAssunto.get())
    pagina_ini = str(txtPgIni.get())
    pagina_fin = str(txtPgFin.get())
    servidor = str(cbServidor.get())
    pasta_saida = str(txtSaida.get())
    # ordem: servidor, pesquisa, pagina inicial, pagina final, pasta de saida
    comando = 'start python main.py ' + servidor + ' ' + pesquisa + ' ' + pagina_ini + ' ' + pagina_fin + ' ' + pasta_saida
    os.system(comando)
    pass


linha1 = 10
linha2 = 35
linha3 = 60
linha4 = 85
linha5 = 110

mainGUI = Tk()
mainGUI.title("xDownload V 1.0")
mainGUI.geometry("270x155+300+300")
mainGUI.resizable(0, 0)

lblAssunto = Label(mainGUI, text="Pesquisa:")
lblAssunto.place(x=10, y=linha1)

txtAssunto = ttk.Entry(mainGUI, width=30)
txtAssunto.place(x=70, y=linha1)

lblIntervalo = Label(mainGUI, text="Intervalo:")
lblIntervalo.place(x=10, y=linha2)

txtPgIni = ttk.Entry(mainGUI, width=5)
txtPgIni.place(x=70, y=linha2)

lblAte = Label(mainGUI, text="até")
lblAte.place(x=110, y=linha2)

txtPgFin = ttk.Entry(mainGUI, width=5)
txtPgFin.place(x=140, y=linha2)

lblServidor = Label(mainGUI, text="Servidor:")
lblServidor.place(x=10, y=linha3)

box_value = StringVar()
cbServidor = ttk.Combobox(mainGUI, textvariable=box_value, width=27)
cbServidor.place(x=70, y=linha3)
cbServidor['values'] = ('XVideos','YouPorn', 'RedTube')

lblSaida = Label(mainGUI, text="Pasta de Saída:")
lblSaida.place(x=10, y=linha4)
txtSaida = ttk.Entry(mainGUI, width=25)
txtSaida.place(x=98, y=linha4)

btnBuscarEBaixar = ttk.Button(mainGUI, text = "Buscar e Baixar", command=btnBuscarEBaixar_Click, width=39)
btnBuscarEBaixar.place(x=12, y=linha5)

mainGUI.mainloop()