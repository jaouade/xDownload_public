from tkinter import *
from tkinter import ttk
import os

def btnSearchAndDownload_Click():
    search = str(txtSearch.get()).replace(" ", "+") # replace spaces by +
    first_page = str(txtFirstPage.get())
    last_page = str(txtLastPage.get())
    server = str(cbserver.get())
    output_dir = str(txtOutput.get())
    # ordem: server, search, firt page, last page, output dir
    command = 'start python main.py ' + server + ' ' + search + ' ' + first_page + ' ' + last_page + ' ' + output_dir
    os.system(command)


line1 = 10
line2 = 35
line3 = 60
line4 = 85
line5 = 110
line6 = 135

mainGUI = Tk()
mainGUI.title("xDownload V 1.0")
mainGUI.geometry("270x150+300+300")
mainGUI.resizable(0, 0)

lblSubject = Label(mainGUI, text="Search:")
lblSubject.place(x=10, y=line1)

txtSearch = ttk.Entry(mainGUI, width=30)
txtSearch.place(x=70, y=line1)

lblInterval = Label(mainGUI, text="Range:")
lblInterval.place(x=10, y=line2)

txtFirstPage = ttk.Entry(mainGUI, width=5)
txtFirstPage.place(x=70, y=line2)

lblTo = Label(mainGUI, text="to")
lblTo.place(x=112, y=line2)

txtLastPage = ttk.Entry(mainGUI, width=5)
txtLastPage.place(x=140, y=line2)

lblPages = Label(mainGUI, text="<- (Pages)")
lblPages.place(x=180, y=line2)

lblserver = Label(mainGUI, text="Server:")
lblserver.place(x=10, y=line3)

box_value = StringVar()
cbserver = ttk.Combobox(mainGUI, textvariable=box_value, width=27)
cbserver.place(x=70, y=line3)
cbserver['values'] = ('XVideos',
                      'YouPorn',
                      'RedTube',
                      'PornHub',
                      'Beeg',
                      'XHamster',
                      'EPorner',
                      'Porn')

lblOutPut = Label(mainGUI, text="Output dir:")
lblOutPut.place(x=10, y=line4)
txtOutput = ttk.Entry(mainGUI, width=25)
txtOutput.place(x=98, y=line4)

btnSearchAndDownload = ttk.Button(mainGUI, text = "Search and Download", command=btnSearchAndDownload_Click, width=39)
btnSearchAndDownload.place(x=12, y=line5)

#lblInfo = Label(mainGUI, text="Info:")
#lblInfo.place(x=10, y=line6)

mainGUI.mainloop()