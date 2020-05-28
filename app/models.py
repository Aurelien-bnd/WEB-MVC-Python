import pymysql as sql
from flask import jsonify
from flask import render_template
from flask import Flask, request
from app import *
import config

def check_for_username(username):
    cnx = sql.connect(host=config.DATABASE_HOST,
                    user=config.DATABASE_USER,
                    password=config.DATABASE_PASS,
                    db=config.DATABASE_NAME,
                    unix_socket=config.DATABASE_SOCK)
    cursor = cnx.cursor()
    sql_code = (
        "SELECT username FROM user WHERE username=%s"
    )
    data = (username)
    cursor.execute(sql_code, data)
    row = cursor.rowcount
    if row == 1:
        return 1
    else:
        return 0

def check_for_password(password):
    cnx = sql.connect(host=config.DATABASE_HOST,
                    user=config.DATABASE_USER,
                    password=config.DATABASE_PASS,
                    db=config.DATABASE_NAME,
                    unix_socket=config.DATABASE_SOCK)
    cursor = cnx.cursor()
    sql_code = (
        "SELECT password FROM user WHERE password=%s"
    )
    data = (password)
    cursor.execute(sql_code, data)
    row = cursor.rowcount
    if row == 1:
        return 1
    else:
        return 0

def check_if_user_exist(username):
    cnx = sql.connect(host=config.DATABASE_HOST,
                    user=config.DATABASE_USER,
                    password=config.DATABASE_PASS,
                    db=config.DATABASE_NAME,
                    unix_socket=config.DATABASE_SOCK)
    cursor = cnx.cursor()
    sql_code = (
        "SELECT username FROM user WHERE username=%s"
    )
    data = (username)
    cursor.execute(sql_code, data)
    row = cursor.rowcount
    cursor.close()
    if row != 0:
        return (1)
    else:
        return (0)


def create_user(username, password):
    user_exist = check_if_user_exist(username)
    if user_exist != 0:
        return (0)
    cnx = sql.connect(host=config.DATABASE_HOST,
                    user=config.DATABASE_USER,
                    password=config.DATABASE_PASS,
                    db=config.DATABASE_NAME,
                    unix_socket=config.DATABASE_SOCK)
    cursor = cnx.cursor()
    sql_code = (
        "INSERT INTO user (username, password)"
        "VALUE (%s, %s)"
    )
    data = (username, password)
    cursor.execute(sql_code, data)
    cnx.commit()
    cursor.close()
    return (1)

def log_user(username, password):
    check_user = check_for_username(username)
    check_passwrd = check_for_password(password)
    if check_user == 1 and check_passwrd == 1:
        return (1)
    else:
        return (0)


def add_task(task_name):
    cnx = sql.connect(host=config.DATABASE_HOST,
                    user=config.DATABASE_USER,
                    password=config.DATABASE_PASS,
                    db=config.DATABASE_NAME,
                    unix_socket=config.DATABASE_SOCK) 
    cursor = cnx.cursor()
    sql_code = (
        "INSERT INTO task (title)"
        "VALUE (%s)"
    )
    data = (task_name)
    cursor.execute(sql_code, data)
    cnx.commit()
    cursor.close()

def get_task():
    cnx = sql.connect(host=config.DATABASE_HOST,
                    user=config.DATABASE_USER,
                    password=config.DATABASE_PASS,
                    db=config.DATABASE_NAME,
                    unix_socket=config.DATABASE_SOCK)    
    cursor = cnx.cursor()
    sql_code = (
        "SELECT title FROM task"
    )
    cursor.execute(sql_code)
    nb_row = cursor.fetchall()
    all_task = [i[0] for i in nb_row]
    return all_task

def del_task(id_task):
    cnx = sql.connect(host=config.DATABASE_HOST,
                user=config.DATABASE_USER,
                password=config.DATABASE_PASS,
                db=config.DATABASE_NAME,
                unix_socket=config.DATABASE_SOCK)
    cursor = cnx.cursor()
    sql_code = (
        "DELETE FROM task WHERE title=%s"
    )
    data = (id_task)
    cursor.execute(sql_code, data)
    cnx.commit()
    cursor.close()
    return 1
