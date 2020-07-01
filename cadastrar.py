from tkinter import *
import tkinter.font as tkFont
import pymysql.cursors
import principal


def Cadastrar():
  janela3 = Tk()
  janela3.title("Asio")
  janela3['bg'] = "#1D1D1D"
  janela3.geometry('500x500+400+70')
  janela3.iconbitmap('Logo3.ico')
  janela3.resizable(False,False)

  def Fechar():
      janela3.destroy()
      principal.Principal()

  def Limpar():
      ed_marca.delete(0, 'end')
      ed_modelo.delete(0, 'end')
      ed_placa.delete(0, 'end')
      ed_cor.delete(0, 'end')

  def Cadastro():
    conexao = pymysql.connect(
      host='localhost',
      user='root',
      passwd='Python@2590',
      port=3306,
      db='controle_placa',
      cursorclass=pymysql.cursors.DictCursor
    )

    cursor = conexao.cursor()
    marca = ed_marca.get()
    modelo = ed_modelo.get()
    placa = ed_placa.get()
    cor = ed_cor.get()

    cursor.execute("insert into cadastro(modelo, marca, placa, cor) values(%s, %s, %s, %s)", (modelo,marca,placa,cor))
    conexao.commit()
    conexao.close()

  fontStyle = tkFont.Font(family="Arial", size=25)
  lb_cadastro = Label(janela3, text="Cadastro", foreground='white', background='#1D1D1D', font= fontStyle)
  lb_cadastro.place(x=30,y=30)

  fontStyle2 = tkFont.Font(family="Arial", size=16)
  lb_marca = Label(janela3,text="Marca", foreground='white', background='#1D1D1D',font=fontStyle2)
  lb_marca.place(x=30,y=130)
  ed_marca = Entry(janela3, width=50)
  ed_marca.place(x=30, y=170)

  lb_modelo= Label(janela3,text="Modelo", foreground='white', background='#1D1D1D',font=fontStyle2)
  lb_modelo.place(x=30,y=210)
  ed_modelo = Entry(janela3, width=50)
  ed_modelo.place(x=30, y=250)

  lb_placa= Label(janela3,text="Placa", foreground='white', background='#1D1D1D',font=fontStyle2)
  lb_placa.place(x=30,y=290)
  ed_placa = Entry(janela3, width=50)
  ed_placa.place(x=30, y=330)

  lb_cor= Label(janela3,text="Cor", foreground='white', background='#1D1D1D',font=fontStyle2)
  lb_cor.place(x=30,y=370)
  ed_cor = Entry(janela3, width=50)
  ed_cor.place(x=30, y=410)

  logo = PhotoImage(file="Logo3(1).png")
  lb_imagem = Label(janela3, image=logo, background='#1D1D1D')
  lb_imagem.place(x=390,y=10)

  bt_cadastrar = Button(janela3, width=10, text="Cadastrar", command=Cadastro)
  bt_cadastrar.place(x=30,y=455)

  bt_limpar = Button(janela3, width=10, text="Limpar", command=Limpar)
  bt_limpar.place(x=250,y=455)

  bt_fechar = Button(janela3, width=10, text="Fechar", command=Fechar)
  bt_fechar.place(x=400,y=455)



  janela3.mainloop()
