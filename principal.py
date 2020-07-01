from tkinter import *
import cadastrar
import placa
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
historico = ""

def Principal():

  janela2 = Tk()
  janela2.title("Asio")
  janela2['bg'] = "#1D1D1D"
  janela2.geometry('1280x720+130+70')
  janela2.iconbitmap('Logo3.ico')
  janela2.resizable(False,False)

  def Sair():
    janela2.destroy()

  def Cadastrar():
      janela2.destroy()
      cadastrar.Cadastrar()

  def Iniciar():
    placa.video()

  logo = PhotoImage(file="Logo3(1).png")
  lb_imagem = Label(janela2, image=logo, background='#1D1D1D')
  lb_imagem.place(x=1150,y=25)

  lb_video = Label(janela2, background='black', width=130, height=40,text='Sem Vídeo', foreground='white')
  lb_video.place(x=50,y=50)

  lb_entrada = scrolledtext.ScrolledText(janela2, width=30, height=32, background='black', foreground='white')
  lb_entrada.place(x=1000,y=138)
  lb_entrada
  lb_entrada.config(state=DISABLED)

  menubar = Menu(janela2)
  janela2.config(menu=menubar)
  filemenu = Menu(menubar)
  filemenu2 = Menu(menubar)
  filemenu3 = Menu(menubar)
  filemenu4 = Menu(menubar)
  menubar.add_cascade(label='Arquivo', menu=filemenu)
  menubar.add_cascade(label='Placas', menu=filemenu2)
  menubar.add_cascade(label='Ajuda', menu=filemenu3)
  filemenu.add_cascade(label='Iniciar', command=Iniciar)
  filemenu.add_cascade(label='Parar')
  filemenu.add_cascade(label='Sair', command=Sair)
  filemenu2.add_cascade(label='Cadastrar', command=Cadastrar)


  janela2.mainloop()

def info(placa_entrada):
  historico = placa_entrada