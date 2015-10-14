#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from db_exec import *
import MySQLdb

class Principal(QWidget): 
    def __init__(self, *args):

        QWidget.__init__(self, *args)
 
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)

        #Definir contenido
        self.setWindowTitle('DBConnection')

        usuario = QLabel("Usuario", self).move(10, 0)
        key = QLabel("Pass", self).move(10, 30)
        ip_server = QLabel("IP Server", self).move(10, 60)
        ip_server = QLabel("Coleccion", self).move(10, 90)
        db = QLabel("Nombredb", self).move(10, 120)

        global entrada_usuario
        global entrada_key
        global entrada_ip_server
        global entrada_coleccion
        global entrada_puerto
        global entrada_db

        entrada_usuario = QLineEdit(self)
        entrada_key = QLineEdit(self)
        entrada_key.setEchoMode(QLineEdit.Password)
        entrada_ip_server = QLineEdit(self)
        entrada_coleccion = QLineEdit(self)
        entrada_db = QLineEdit(self)

        bt_mongo = QPushButton('Mongodb', self)
        self.connect(bt_mongo, SIGNAL("clicked()"), self.db_mongodb)

        bt_mysql = QPushButton('MySQL', self)
        self.connect(bt_mysql, SIGNAL("clicked()"), self.db_mysql)

        bt_postgres = QPushButton('Postgres', self)
        self.connect(bt_postgres, SIGNAL("clicked()"), self.db_postgres)

        bt_oracle = QPushButton('Oracle', self)
        self.connect(bt_oracle, SIGNAL("clicked()"), self.db_oracle)

        #Tamaño ventana
        self.setGeometry(300, 300, 400, 200)

        entrada_usuario.move(80, 0)
        entrada_key.move(80, 30)
        entrada_ip_server.move(80, 60)
        entrada_coleccion.move(80, 90)
        entrada_db.move(80, 120)

        bt_mongo.move(230, 0)
        bt_mysql.move(230, 30)
        bt_postgres.move(230, 60)
        bt_oracle.move(230, 90)    

    def db_mysql(self):
        ventana = mysql().exec_()

    def db_postgres(self):
        ventana = postgres().exec_()

    def db_oracle(self):
        ventana = oracle().exec_()

    def db_mongodb(self):
        ventana = mongodb().exec_()

class mysql(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
 
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)

        #Definir contenido
        self.setWindowTitle('MySQL')
        
        data = mysql_data(str(entrada_ip_server.text()),
                            str(entrada_usuario.text()), 
                            str(entrada_key.text()), 
                            str(entrada_db.text()))
        for r in data:
            for i in r:
                resultado = QLabel(QString(i), None)
                contenedor.addWidget(resultado)

        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)

        #Tamaño ventana
        self.setGeometry(300, 300, 400, 200)

 
    def salir(self):
        exit()

class postgres(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
 
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)

        #Definir contenido
        self.setWindowTitle('Postgres')
        
        data = postgres_data(str(entrada_ip_server.text()),
                            str(entrada_usuario.text()), 
                            str(entrada_key.text()), 
                            str(entrada_db.text()))

        for r in data:
            for i in r:
                resultado = QLabel(QString(i), None)
                contenedor.addWidget(resultado)

        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)

        #Tamaño ventana
        self.setGeometry(300, 300, 400, 200)

 
    def salir(self):
        exit()

class oracle(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
 
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)

        #Definir contenido
        self.setWindowTitle('Oracle')
        
        data = oracle_data(str(entrada_ip_server.text()),
                            str(entrada_usuario.text()), 
                            str(entrada_key.text()), 
                            str(entrada_db.text()))

        for r in data:
            resultado = QLabel(QString(r[0]), None)
            contenedor.addWidget(resultado)

        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)

        #Tamaño ventana
        self.setGeometry(300, 300, 400, 200)

 
    def salir(self):
        exit()

class mongodb(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
 
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)

        #Definir contenido
        self.setWindowTitle('Mongodb')
        
        data = mongo_data(str(entrada_ip_server.text()),
                            str(entrada_usuario.text()), 
                            str(entrada_key.text()), 
                            str(entrada_db.text()),
                            str(entrada_coleccion.text()))

        #print data[0]['nombre']

        for r in data:
            resultado = QLabel(QString(r['nombre']), None)
            contenedor.addWidget(resultado)

        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)

        #Tamaño ventana
        self.setGeometry(300, 300, 400, 200)

 
    def salir(self):
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    sys.exit(app.exec_())
