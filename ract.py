import pytesseract as ocr
import cv2
import unicodedata
import re
import numpy as np

class Ract():

    phrase = ""

    def __init__(self, placa):

        img = cv2.imread('roi.jpg')
        img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #img_sim = cv2.GaussianBlur(img_cinza, (5, 5), 0)

        _, img_inv = cv2.threshold(img_cinza, 172, 255, cv2.THRESH_BINARY)
        cv2.imshow('teste', img_inv)

        phrase = ocr.image_to_string(img_inv)

        def removerAcentosECaracteresEspeciais(palavra):

            nfkd = unicodedata.normalize('NFKD', palavra)
            palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

            return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

        phrase = removerAcentosECaracteresEspeciais(phrase)

        finalPlaca = (phrase, "ABC1234")
        if(placa == finalPlaca):
            print("achou!")
        else:
            print("não achou!")


        print(phrase)

        cv2.waitKey(0)
        cv2.destroyAllWindows()



