import time
import cv2

class Img():

    def __init__(self):

      video = cv2.VideoCapture('TCC_videoteste.mov')

      #img = cv2.imread('placa01.jpg')
      classificador = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

      while(True):

          conectado, frame = video.read()
          frame = cv2.resize(frame, (600, 300))

          img_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          img_sim = cv2.GaussianBlur(img_cinza, (5, 5), 0)
          deteccao = classificador.detectMultiScale(img_sim)

          for(x, y, l, a) in deteccao:
              cv2.rectangle(frame, (x,y), (x + l, y + a), (0, 255, 0), 2)
              roi = frame[y:y + a, x:x + l]
              cv2.imwrite('C:\\Users\\Vinicius\\Documents\\OpenCV\\Projeto TCC\\roi.jpg', roi)

          cv2.imshow("Deteccao", frame)

          if cv2.waitKey(1) == ord('q'):
              break

      video.release()
      cv2.destroyAllWindows()
