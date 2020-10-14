import sqlite3
import random

def connect(name):
	"""
	_________________________________________
	Crea una conexion a una database indicada
	_________________________________________
	"""
	global database,db_cursor
	database=sqlite3.connect(name)
	db_cursor=database.cursor()

def runcode(args):
	"""
	______________________
	Ejecuta codigo sqlite3
	______________________
	"""
	db_cursor.execute(args)

def create(args1,args2):
	"""
	_________________________
	CRUD
	^
	CREATE = CREA un registro
	_________________________
	"""
	db_cursor.execute("INSERT INTO "+args1+" VALUES("+args2+")")

def read(args1,*args2):
	"""
	______________________
	CRUD
	 ^
	READ = LEE un registro
	______________________
	"""
	try:
		data=db_cursor.execute("SELECT * FROM "+str(args1)+" WHERE "+str(args2[0])+"="+str(args2[1]))
	except:
		data=db_cursor.execute("SELECT * FROM "+str(args1))
	return data.fetchall()

def update(args1,*args2):
	"""
	______________________________
	CRUD
	  ^
	UPDATE = ACTUALIZA un registro
	______________________________
	"""
	db_cursor.execute("UPDATE "+str(args1)+" SET "+str(args2[0])+" = "+str(args2[1])+" where "+str(args2[2])+" = "+str(args2[3])+"")

def delete(args1,args2,args3):
	"""
	____________________________
	CRUD
	   ^
	DELETE = ELIMINA un registro
	____________________________
	"""
	db_cursor.execute("DELETE FROM "+args1+" WHERE "+args2+"="+args3)

def save():
	"""
	_____________________
	Guarda los cambios
	hechos en la database
	_____________________
	"""
	database.commit()

def close():
	"""
	__________________
	Cierra la conexión
	__________________
	"""
	database.close()
def crud_doc():
	print("connect"+connect.__doc__)
	print("runcode"+runcode.__doc__)
	print("create"+create.__doc__)
	print("read"+read.__doc__)
	print("update"+update.__doc__)
	print("delete"+delete.__doc__)
	print("save"+save.__doc__)
	print("close"+close.__doc__)


import base64
contador=0
contador1=0

def encode(texto):
	text=texto.encode("UTF-8")
	code=base64.b64encode(text).decode("UTF-8")
	return code

def decode(texto):
	text=texto
	code=base64.b64decode(text)
	return code.decode("UTF-8")

def encode_list(list2encode,encode2list):
	global contador
	for i in range(0,len(list2encode)):
		encode2list.append(encode(list2encode[contador]))
		contador=contador+1

def decode_list(list2decode):
	global contador1
	decode2list=[]
	for i in range(0,len(list2decode)):
		decode2list.append(decode(list2decode[contador1]))
		contador1=contador1+1
	return decode2list



alphabet={
1:"a",
2:"b",
3:"c",
4:"d",
5:"e",
6:"f",
7:"g",
8:"h",
9:"i",
10:"j",
11:"k",
12:"l",
13:"m",
14:"n",
15:"ñ",
16:"o",
17:"p",
18:"q",
19:"r",
20:"s",
21:"t",
22:"u",
23:"v",
24:"w",
25:"x",
26:"y",
27:"z",
28:"1",
29:"2",
30:"3",
31:"4",
32:"5",
33:"6",
34:"7",
35:"8",
36:"9",
37:"0",
38:"=",
39:".",
40:"?"
}

passw=""

def password(len):
	global passw
	for i in range(0,len):
		passw=passw+alphabet[random.randint(1,40)]
	return passw

