from tkinter import *
import pymysql.cursors
import principal

conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='Python@2590',
            port=3306,
            db='controle_placa',
            cursorclass=pymysql.cursors.DictCursor
          )

def click_entrar():
    #lb_erro["text"] = "Senha Incorreta!"
    senha = ed_senha.get()
    usuario = ed_usuario.get()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuario WHERE login = %s AND senha = %s", (usuario, senha))
    resultado = cursor.fetchall()

    if resultado == ():
        lb_erro["text"] = "Senha Incorreta!"

    else:
        janela.destroy()
        principal.Principal()


janela = Tk()
janela.title('Asio')
janela['bg'] = '#1D1D1D'
janela.geometry('200x180+650+250')
janela.iconbitmap('Logo3.ico')
janela.resizable(False,False)

bt_entrar = Button(janela, width=10, text="Entrar", command=click_entrar)
bt_entrar.place(x=60, y=130)

lb_login = Label(janela, text="Login:",background='#1D1D1D', foreground='white')
lb_login.place(x=10,y=30)

lb_senha = Label(janela, text="Senha:",background='#1D1D1D', foreground='white')
lb_senha.place(x=10,y=70)

lb_erro = Label(janela, text="",background='#1D1D1D', foreground='red')
lb_erro.place(x=50,y=100)

ed_usuario = Entry(janela, width=19)
ed_usuario.place(x=60, y=30)

ed_senha = Entry(janela, width=19, show="•")
ed_senha.place(x=60, y=70)



janela.mainloop()