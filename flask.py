import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'
    
@app.route("/caminhos_hora")
def caminhos_hora (dataHora = None):
    conn = pyodbc.connector.connect (host='database-2.cty7ngueirfy.us-east-1.rds.amazonaws.com', user='admin', passwd='admin', port='3306', database='smartcare_db')
    cursor = conn.cursor()
    qstr = "select A.DataHora , A.Valor , B.CodigoDispositivo , B.Eixo_X , B.Eixo_y , B.Orientacao case when B.Orientacao = '+X' then x = B.Eixo_X + (A.Valor * 0.5) and y = B.Eixo_y END when B.Orientacao = '+Y' then y = B.Eixo_y + (A.Valor * 0.5) and x = B.Eixo_X END when B.Orientacao = '-X' then x = B.Eixo_X _ (A.Valor * 0.5) and y = B.Eixo_y END when B.Orientacao = '-Y' then y = B.Eixo_y _ (A.Valor * 0.5) and x = B.Eixo_X END from Medicao A, Dispositivo B where A.IdDispositivo = B.IdDispositivo like A.DataHora =\'"+dataHora+"\'"
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret
