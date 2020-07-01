import pymysql.cursors
import placa

from ract import Ract


conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Python@2590',
    port = 3306,
    db = 'controle_placa',
    cursorclass = pymysql.cursors.DictCursor
)
x = 'dom1700'
y = 'ok'
print('ok BD')
placaFinal = placa.placa_final()

cursor = conexao.cursor()
cursor.execute("SHOW DATABASES;")
cursor.execute("USE controle_placa;")
cursor.execute("SHOW TABLES;")
cursor.execute("SELECT * FROM historico")
cursor.execute("INSERT INTO historico(placa) VALUES(%s)", placaFinal)
conexao.commit()
conexao.close()

#row = cursor.fetchone()

#p1 = Ract(row)

#print(row)

#if(row == x):
 #   print('ok string')
#else:
   # print('não achou!')

for x in cursor:
    print(x)