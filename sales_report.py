# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:48:01 2020

@author: Edgar
"""

import mysql.connector
from mysql.connector import Error
import csv
import os

from datetime import datetime
from uuid import uuid4

#---------------------------------------
#Funciones de utilidad

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexion a base MySQL establecida")
    except Error as e:
        print(e)

    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(e)
        
def create_csv(name, data):
    with open(name, 'w', newline='') as f:
        thewriter=csv.writer(f)
        
        #Create header
        thewriter.writerow(['AÑO', 'MES', 'DIA', 'VTA_DET_SUBTOTAL'])
        #Mes num a nombre
        meses = {
                 1 : 'Enero',
                 2 : 'Febrero',
                 3 : 'Marzo',
                 4 : 'Abril',
                 5 : 'Mayo',
                 6 : 'Junio',
                 7 : 'Julio',
                 8 : 'Agosto',
                 9 : 'Septiembre',
                 10 : 'Octubre',
                 11 : 'Noviembre',
                 12 : 'Diciembre'
        }
        
        #Crear filas
        for row in data:
            #Crear data para escribir
            date = row[7]
            year = date.year
            month = meses[date.month]
            day = date.day
            
            vta_det_subtotal = round(float(row[5]),2)
            
            linea_para_escribir = [year, month, day, vta_det_subtotal]

            #Escribir
            thewriter.writerow(linea_para_escribir)
    
#---------------------------------------
#Environment variables
import environment_variables

environment_variables.main()
#---------------------------------------
#Creacion de reporte

host_name = os.environ.get("host_name")
user_name = os.environ.get("user_name")
user_password = os.environ.get("user_password")
db_name = os.environ.get("db_name")
connection = create_connection(host_name, user_name, user_password,db_name)

query = os.environ.get("query")

data = execute_read_query(connection, query)

eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
os.environ['report_name'] = 'Reporte_' + eventid + '.csv'
create_csv(os.environ.get('report_name'), data)


#---------------------------------------
#Mandar email
mandar_email = True

if mandar_email:
    import send_report
    
    send_report.main()




    




        
