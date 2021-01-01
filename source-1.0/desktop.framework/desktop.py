from tkinter import *

PATH = '/Users/solomonwood/Desktop/SolOS/'
desktop = Tk()
desktop.title('Desktop')
desktop.attributes('-fullscreen',True)

logo_png = PhotoImage(file='logo.png')

menubar = Menu(desktop)
desktop.config(menu=menubar)

menubar_main = Menu(menubar)
menubar.add_cascade(image=logo_png,menu=menubar_main)

menubar_main.add_command(label='New Window')
menubar_main.add_command(label='Browse Apps')
menubar_main.add_command(label='My Computer')

menubar_main_shutdown = Menu(menubar)
menubar_main.add_cascade(label='Shutdown',menu=menubar_main_shutdown)
