import PySimpleGUI as sg
import cv2
import pymysql.cursors

class tela:

    def __init__(self):
        self.video = cv2.VideoCapture('TCC_videoteste.mov')

        sg.change_look_and_feel('DarkGrey6')
        #layout
        layout = [
           [sg.Text('Login',size=(5,0)), sg.Input(size=(15,0), key='login')],
           [sg.Text('Senha',size=(5,0)), sg.Input(size=(15,0), key='senha', password_char='•')],
           [sg.Button('Entrar', key= 'entrar')]
        ]
        layout2=[
            [sg.Text('Senha ou Login incorretos', key='incorreto'),
             sg.Button('Fechar', size=(7, 0), key='fechar')
             ]
        ]

        #janela
        self.janela = sg.Window('Login').layout(layout)
        self.janela2 = sg.Window('Erro').layout(layout2)
        #extrair info

    def iniciar(self):

        while True:

          self.button, self.values = self.janela.Read()

          print(self.values)
          login = self.values['login']
          senha = self.values['senha']

          conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='Python@2590',
            port=3306,
            db='controle_placa',
            cursorclass=pymysql.cursors.DictCursor
          )

          cursor = conexao.cursor()
          cursor.execute("SELECT * FROM usuario WHERE login = %s AND senha = %s", (login, senha))
          resultado = cursor.fetchall()
          print(resultado)
          conexao.commit()
          conexao.close()
          if resultado == ():
             self.button = self.janela2.Read()
             self.button = self.janela2.Close()

          else: break

Tela = tela()
Tela.iniciar()