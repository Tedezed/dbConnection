#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mysql_data(host_db, user_db, pass_db, nom_db):
    import MySQLdb

    query = "select nombre from autores;"

    #Conexion DB
    con_mysql = MySQLdb.connect(host=host_db, user=user_db, passwd=pass_db, db=nom_db)

    cursor = con_mysql.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close() 
    con_mysql.close()

    return data

def postgres_data(host_db, user_db, pass_db, nom_db):
    import psycopg2, psycopg2.extras

    query = "select nombre from autores;"

    conn = psycopg2.connect(database=nom_db ,user=user_db, password=pass_db, host=host_db)

    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return data

def oracle_data(host_db, user_db, pass_db, nom_db):
    import cx_Oracle

    conn_str = user_db + '/' + pass_db + '@' + host_db + ':1521/orcl'
    print conn_str

    #conn_str = 'HR/HR@127.0.0.1:1521/XE'
    query = "select * from cat"
    
    db_conn = cx_Oracle.connect(conn_str)
    cursor = db_conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print data
    cursor.close()
    db_conn.close()

    return data

def mongo_data(host_db, user_db, pass_db, nom_db, coleccion_db):
    from pymongo import MongoClient

    con = MongoClient('mongodb://' + user_db + ':' + pass_db + '@' + host_db + ':27017/' + nom_db)
    print con
    db = con[nom_db]
    coleccion = db[coleccion_db]
    data = coleccion.find()
    con.close()

    return data
