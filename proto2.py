import json
from json import load, dump
import sys


from mariadb import connect, Error as MDBError
data = {}
cursors = []
connects = []
def Init():
    global data
    file = open("./data.json", "r")
    data = load(file)
    file.close()



def Connection():
    global data, cursors, connects
    for i in data.keys():
        user = data[i]["User"]
        password = data[i]["Password"]
        host = data[i]["Host"]
        port = data[i]["Port"]
        database = data[i]["Database"]
        print(f"User: {user}, Password: {password}, Host: {host}, Port: {port}, Database: {database}")


Init()
Connection()





