# Ftp server
import crud,hashlib,time
import pyperclip,webbrowser,pickle
import os,subprocess
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

error=0

FTP_PORT = 2121
#---------------------------------------------------------------------------------------#

contador=0
contador1=0
salida=[]
def ip4():
	global ip3,contador,contador1
	contador=0
	contador1=0
	ip5=subprocess.check_output(["ipconfig"],shell=True,universal_newlines=True)
	ip5=ip5.split("\n")
	for i in range(0,len(ip5)):
		if ip5[contador]=="":
			contador=contador+1
		else:
			salida.append(ip5[contador])
			contador=contador+1
	ip3=[]
	for i in range(0,len(salida)):
		if "   Direcci¢n IPv4. . . . . . . . . . . . . . :" in salida[contador1]:
			ip3.append(salida[contador1])
			break
		else:
			contador1=contador1+1
	ip3=ip3[0].lstrip("   Direcci¢n IPv4. . . . . . . . . . . . . . :")
	ip3.rstrip(" ")
	ip.set(ip3)

	return ip3
	
#---------------------------------------------------------------------------------------#

def main():
	global server,FTP_DIRECTORY,status
	authorizer = DummyAuthorizer()
	if FTP_DIRECTORY=="":
		FTP_DIRECTORY=os.getcwd()
		directorio.set(os.getcwd())
	if ip.get()=="":
		ipauth.set("on")
		ip4()
	if annonimus=="on":
		authorizer.add_anonymous(FTP_DIRECTORY, perm='elr')
	else:
		authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')
	handler = FTPHandler
	handler.authorizer = authorizer
	handler.banner = 'Servidor FTP Listo'
	handler.passive_ports = range(60000, 65535)
	address = (ip.get(), port.get())
	server = FTPServer(address, handler)

	server.max_cons = 256
	server.max_cons_per_ip = 5
	save_all()
	
	web=Label(text="ftp://"+IP.get()+":"+str(port.get())+"\n"+"En el directorio: "+FTP_DIRECTORY,relief="sunken",justify="left")
	pyper=Button(text="Copiar",command=lambda:pyperclip.copy("ftp://"+IP.get()+":"+str(port.get())))
	pyper2=Button(text="Abrir navegador",command=lambda:webbrowser.open("ftp://"+IP.get()+":"+str(port.get())))
	
	pyper.place(x=120,y=450)
	pyper2.place(x=180,y=450)
	web.place(x=120,y=400)
	server.serve_forever()
	web.place_forget()
	pyper.place_forget()
	pyper2.place_forget()
	status="off"
    

def man():
	try:
		if ipauth.get()=="on":
			ip4()
		else:
			pass
		main()
	except OSError as error:
		if ipauth.get()=="off":
			messagebox.showwarning("Ip-port","El puerto-ip ya esta siendo utilizado")
			print(error)
			ftp.config(text="Start Ftp-server",command=ftpstart)
		else:
			port.set(int(port.get())+1)
			port2=io.open("port","w")
			port2.write(str(port.get()))
			port2.close()
			man()


#---------------------------------------------------------------------------------------#

from tkinter import *
from tkinter import messagebox,filedialog
import threading,io

status=""

root=Tk()
root.geometry("620x500")
root.config(bg="#bde0e9")
root.resizable(0,0)
root.title("FTP server")

#DEFS
def ftpstart():
	global status,t,FTP_USER,FTP_PASSWORD,FTP_DIRECTORY
	print(1)
	FTP_USER = user.get()
	FTP_PASSWORD = pass2.get()
	FTP_DIRECTORY = directorio.get()
	
	ftp.config(text="Stop Ftp-server",command=ftpstop)
	direct=directorio.get()
	use=user.get()
	pass3=pass2.get()
	if status=="on":
		pass
	else:
		status="on"
		t=threading.Thread(target=man)
		t.start()
		



def ftpstop():
	ftp.config(text="Start Ftp-server",command=ftpstart)
	server.close_all()


def show():
	if test.get()=="on":
		Pass.config(show="")
		crud.connect("configs\cfg.db")
		crud.update("configs","show","'"+test.get()+"'","id",1)
	else:
		Pass.config(show="*")
		crud.connect("configs\cfg.db")
		crud.update("configs","show","'"+test.get()+"'","id",1)
	crud.save()
	crud.close()

def change():
	global annonimus
	annonimus=test3.get()


def selecdir():
	dire=filedialog.askdirectory()
	if dire=="":
		directorio.set(os.getcwd())
		dir()
	else:
		directorio.set(dire)
		dir()

def pass_auth_def():
	if pass_auth.get()=="True":
		pass2.set(crud.password(10))
		save_all()

def aut():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_aut",test2.get(),"id",1)
	crud.save()
	crud.close()
def ann():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_ann",test3.get(),"id",1)
	crud.save()
	change()
	crud.close()
def ip_ch():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_ip","'"+ip.get()+"'","id",1)
	crud.save()
	crud.close()
def port_ch():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_port",port.get(),"id",1)
	crud.save()
	crud.close()
def dir():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_dir","'"+directorio.get()+"'","id",1)
	crud.save()
	crud.close()
def usr():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_usr","'"+crud.encode(user.get())+"'","id",1)
	crud.save()
	crud.close()
def pss():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_pass","'"+crud.encode(pass2.get())+"'","id",1)
	crud.save()
	crud.close()

def save_all():
	ip_ch()
	port_ch()
	dir()
	usr()
	pss()

#Buttons
ftp=Button(text="Start Ftp-server",command=ftpstart,bg="#bde0e9")
ftp.config(relief="groove",bd=10)
ftp.place(x=250,y=250)
Button(text="Seleccionar",command=lambda:selecdir(),bg="#bde0e9").place(x=400,y=120)

#StringVar and IntVar
ip=StringVar()
directorio=StringVar()  
user=StringVar()
pass2=StringVar()
port=IntVar()
portauth=StringVar()
test2=StringVar()
test3=StringVar()
test=StringVar()
ipauth=StringVar()
pass_auth=StringVar()
#Variables
annonimus=test3.get()
portauth.set("off")

#checkbuttons
Label(text="__________________________________________________________________________",justify="left",bg="#bde0e9",fg="#000000").place(y=300,x=120)
Checkbutton(text="Ejecutar server al iniciar la app",variable=test2,onvalue="1",offvalue="0",command=aut,bg="#bde0e9").place(y=340,x=200)
Checkbutton(text="Contraseña automática",variable=pass_auth,onvalue="True",offvalue="False",command=pass_auth_def,bg="#bde0e9").place(y=360,x=200)
Checkbutton(text="Automatico",variable=ipauth,onvalue="on",offvalue="off",bg="#bde0e9").place(x=400,y=80)
Checkbutton(text="show",variable=test,onvalue="on",offvalue="off",command=show,bg="#bde0e9").place(y=200,x=400)
Checkbutton(text="Anonimo",variable=test3,onvalue=1,offvalue=0,command=ann,bg="#bde0e9").place(y=160,x=400)

#Menu
menu=Menu(root)
root.config(menu=menu)


ftp1=Menu(menu,tearoff=0)
x=ftp1.add_command(label="Iniciar servidor",command=lambda:ftpstart())
x=ftp1.add_command(label="Para servidor",command=lambda:ftpstop())

menu.add_cascade(label="ftp",menu=ftp1)

ayuda=Menu(menu,tearoff=0)
ayuda.add_command(label="IP",command=lambda:subprocess.Popen(["python","help\Ftp_help.py"]))
ayuda.add_command(label="Directorio",command=lambda:subprocess.Popen(["python","help\Ftp_help1.py"]))
ayuda.add_command(label="USR-PSS",command=lambda:subprocess.Popen(["python","help\Ftp_help2.py"]))
menu.add_cascade(label="Ayuda",menu=ayuda)

#Banner
Banner=Label(text="Servidor FTP local V2.6",bg="#bee2b3")
Banner.config(relief="sunken", bd=5, font=("Arial",20),fg="#323836")
Banner.place(x=155)


#IDUP
Label(text="IP",bg="#bde0e9").place(x=120,y=80)
Label(text=":",font=("Arial",15),bg="#bde0e9").place(x=307,y=73)
IP=Entry(textvariable=ip,bg="#bde0e9")
IP.place(x=180,y=80)
Entry(textvariable=port,width=5,bg="#bde0e9").place(x=320,y=80)
Label(text="Directorio",bg="#bde0e9").place(x=120,y=120)
Entry(textvariable=user,width=29,bg="#bde0e9").place(x=180,y=160)
Label(text="User",bg="#bde0e9").place(x=120,y=160)
Pass=Entry(textvariable=pass2,width=29)
Pass.config(show="*",bg="#bde0e9")
Pass.place(x=180,y=200)
Label(text="Password",bg="#bde0e9").place(x=120,y=200)
Entry(textvariable=directorio,width=29,bg="#bde0e9").place(x=180,y=120)

#Llamadas a funciones necesarias

try:
	os.mkdir("configs")
except:
	pass
crud.connect("configs\cfg.db")

try:
	crud.runcode("""CREATE TABLE configs(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	cfg_aut boolean,
	cfg_ann boolean,
	cfg_ip,
	cfg_port INTEGER,
	cfg_dir,
	cfg_usr,
	cfg_pass,
	show
	)""")
	crud.create("configs","NULL,FALSE,TRUE,'"+ip4()+"',2121,"+"'"+os.getcwd()+"'"+",'"+crud.encode("admin")+"','"+crud.encode("admin")+"','off'")
	crud.save()
	read_db=crud.read("configs")
	b64=read_db[0][6],read_db[0][7]
	b64=crud.decode_list(b64)
	print(read_db)
	cfg=read_db[0][1]
	test2.set(str(read_db[0][1]))
	test3.set(str(read_db[0][2]))
	ip2=read_db[0][3]
	port2=read_db[0][4]
	directorio.set(read_db[0][5])
	
	user.set(b64[0])
	pass2.set(b64[1])
	test.set(read_db[0][8])
	show()
	crud.close()
except:
	read_db=crud.read("configs")
	b64=read_db[0][6],read_db[0][7]
	b64=crud.decode_list(b64)
	print(read_db)
	cfg=read_db[0][1]
	test2.set(str(read_db[0][1]))
	test3.set(str(read_db[0][2]))
	ip2=read_db[0][3]
	port2=read_db[0][4]
	directorio.set(read_db[0][5])
	
	user.set(b64[0])
	pass2.set(b64[1])
	test.set(read_db[0][8])
	show()
	crud.close()



if cfg==True:
	ftpstart()
	test2.set("1")
else:
	test2.set("0")

pass_auth.set("False")
show()
ipauth.set("off")
port.set(port2)
ip.set(ip2)
root.mainloop()
