import cv2
import pytesseract as ocr
import unicodedata
import re
import numpy as np
import pymysql.cursors
from PIL import Image


def video():

    video = cv2.VideoCapture(0)

    classificador = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

    while(True):

        conectado, frame = video.read()  #Capturando o frame do video
        frame = cv2.resize(frame, (800, 400))

        img_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_simplificada = cv2.GaussianBlur(img_cinza, (5, 5), 0)  #Simplificando a imagem para o haarcascade
        deteccao = classificador.detectMultiScale(img_simplificada)

        for(x, y, largura, altura) in deteccao:

            cv2.rectangle(frame, (x, y), (x + largura, y + altura), (0,255,0), 2)
            roi = frame[y:y + altura, x:x + largura]
            cv2.imwrite('C:\\Users\\Vinicius\\Documents\\OpenCV\\Projeto TCC\\roi.jpg', roi)  #recortando e salvando a placa

            imagemPlaca(roi)

        cv2.imshow("Asio", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def imagemPlaca(img):


    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.resize(img_rgb, (200, 100))
    #_, img_invertida = cv2.threshold(img_cinza, 172, 255, cv2.THRESH_BINARY)
    npimagem = np.asarray(img_rgb).astype(np.uint8)

    npimagem[:, :, 0] = 0
    npimagem[:, :, 2] = 0

    img_cinza = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)

    ret, thresh = cv2.threshold(img_cinza, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img_sim = Image.fromarray(thresh)

    placa = ocr.image_to_string(img_sim)    #aplicando o pyTesseract

    def removerAcentosECaracteresEspeciais(palavra):
        nfkd = unicodedata.normalize('NFKD', palavra)
        palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

        return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

    placa = removerAcentosECaracteresEspeciais(placa)

    n = len(placa)

    if(n == 7):

        if(placa[0].isalpha() == True and placa[1].isalpha() == True and placa[2].isalpha() == True):

            print('Achou!')
            import principal
            principal.info(placa)
            placa_BD(placa)
            principal

    print(placa)

def placa_BD(placa):

    conexao = pymysql.connect(
        host='localhost',
        user='root',
        passwd='Python@2590',
        port=3306,
        db='controle_placa',
        cursorclass=pymysql.cursors.DictCursor
    )
    placa = placa.upper()

    cursor = conexao.cursor()
    cursor.execute("SHOW DATABASES;")
    cursor.execute("USE controle_placa;")
    cursor.execute("SHOW TABLES;")
    cursor.execute("SELECT * FROM historico")
    cursor.execute("INSERT INTO historico(data_hora, placa) VALUES(NOW(), %s)", placa)
    conexao.commit()
    conexao.close()


