# Ftp server
import crud,hashlib,time
import pyperclip,webbrowser,pickle
import os,subprocess,getpass
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

users_count=0

def authorizer_def():
	global authorizer
	authorizer = DummyAuthorizer()
authorizer_def()
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
	global server,FTP_DIRECTORY,status,users_count,annonimus
	annonimus=test3.get()
	newuser()
	handler = FTPHandler
	handler.authorizer = authorizer
	handler.banner = 'Servidor FTP Listo'
	handler.passive_ports = range(60000, 65535)
	address = (ip.get(), port.get())
	server = FTPServer(address, handler)

	server.max_cons = 256
	server.max_cons_per_ip = 5
	save_all()
	
	web=Label(text="ftp://"+IP.get()+":"+str(port.get())+"\n"+"En el directorio: "+FTP_DIRECTORY,relief="sunken",justify="left",bg="#bee2b3")
	pyper=Button(text="Copiar",command=lambda:pyperclip.copy("ftp://"+IP.get()+":"+str(port.get())),bg="#bee2b3")
	pyper2=Button(text="Abrir navegador",command=lambda:webbrowser.open("ftp://"+IP.get()+":"+str(port.get())),bg="#bee2b3")
	
	pyper.place(x=120,y=580)
	pyper2.place(x=180,y=580)
	web.place(x=120,y=530)
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
		if ipauth.get()==0:
			messagebox.showwarning("Ip-port","El puerto-ip ya esta siendo utilizado")
			print(error)
			ftp.config(text="Start Ftp-server",command=ftpstart)
		else:
			port.set(int(port.get())+1)
			man()


#---------------------------------------------------------------------------------------#

from tkinter import *
from tkinter import messagebox,filedialog
import threading,io

status=""

root=Tk()
root.geometry("620x650")
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
	
	ftp.config(text="Parar servidor",command=ftpstop)
	direct=directorio.get()
	use=user.get()
	pass3=pass2.get()
	if status=="on":
		pass
	else:
		status="on"
		t=threading.Thread(target=man)
		t.start()
		

def anonimo():
	if test3.get()=="1":
		Pass.config(show="X")
		User.config(show="X")
	else:
		Pass.config(show="")
		User.config(show="")
def user_auth():
	if usr_ath.get()=="1":
		user.set(getpass.getuser())
		usr_ath_def()
def ftpstop():
	ftp.config(text="Iniciar Servidor",command=ftpstart)
	server.close_all()
	authorizer_def()
def show():
	crud.connect("configs\cfg.db")
	if test.get()=="on" and test3.get()=="0":
		Pass.config(show="")
		crud.update("configs","show","'"+test.get()+"'","id",1)
	elif test.get()=="off" and test3.get()=="0":
		Pass.config(show="*")
		crud.update("configs","show","'"+test.get()+"'","id",1)
	else:
		if test.get()=="on":
			test.set=="off"
			print(1)
		elif test.get()=="off":
			test.set("on")
			print(2)
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
	if pass_auth.get()=="1":
		pass2.set(crud.password(10))
		save_all()
	else:
		save_all()
def aut():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_aut",test2.get(),"id",1)
	crud.save()
	crud.close()
def ann():
	anonimo()
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
def usr_ath_def():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_usr_auth","'"+usr_ath.get()+"'","id",1)
	crud.save()
	crud.close()
def ip_port_auth():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_auth",ipauth.get(),"id",1)
	crud.save()
	crud.close()
def pass_auth_def_save():
	crud.connect("configs\cfg.db")
	crud.update("configs","cfg_pass_auth",pass_auth.get(),"id",1)
	crud.save()
	crud.close()
def save_all():
	pass_auth_def_save()
	ip_port_auth()
	ip_ch()
	usr_ath_def()
	port_ch()
	dir()
	usr()
	pss()
def newuser():
	global users_count,FTP_USER,FTP_PASSWORD,FTP_DIRECTORY,annonimus
	annonimus=test3.get()
	print(annonimus)
	FTP_USER = user.get()
	FTP_PASSWORD = pass2.get()
	FTP_DIRECTORY = directorio.get()
	if FTP_DIRECTORY=="":
		FTP_DIRECTORY=os.getcwd()
		directorio.set(os.getcwd())
	if ip.get()=="":
		ipauth.set("on")
		ip4()
	try:
		if annonimus=="1":
			authorizer.add_anonymous(FTP_DIRECTORY, perm=perm.get())
			messagebox.showinfo("Usuario añadido","El usuario anonimo fue añadido con exito\nPermiso:"+perm.get())
		else:
			authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm=perm.get())
			messagebox.showinfo("Usuario añadido","El usuario "+user.get()+" fue añadido con exito\nPermiso:   "+perm.get()+"\n"+"Password: "+"*"*len(pass2.get()))
	except ValueError:
		messagebox.showwarning("Usuario denegado","El usuario "+user.get()+" ya existe")
	users_count=users_count+1
	save_all()
def reset():
	ip.set(ip4())
	port.set(2121)
	directorio.set(os.getcwd())
	user.set("admin")
	pass2.set("admin")
	perm.set("elradfmw")
	test2.set("0")
	usr_ath.set(0)
	pass_auth.set(0)
	ipauth.set(1)
	test.set(1)
	test3.set(0)
	save_all
	pass
#Buttons
ftp=Button(text="Iniciar Servidor",command=ftpstart,bg="#bde0e9")
ftp.config(relief="groove",bd=10)
ftp.place(x=250,y=250)
Button(text="Seleccionar Directorio",command=lambda:selecdir(),bg="#bee2b3").place(x=120,y=420)

Button(text="Guardar cambios",command=lambda:save_all(),bg="#bee2b3").place(x=120,y=450)

Button(text="Añadir usuario",command=lambda:newuser(),bg="#bee2b3").place(x=320,y=420)

Button(text="Resetear cambios",command=lambda:reset(),bg="#bee2b3").place(x=320,y=450)

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
usr_ath=StringVar()
pass_auth=StringVar()
perm=StringVar()
#Variables
annonimus=test3.get()
portauth.set("off")
#checkbuttons
Label(text="__________________________________________________________________________",justify="left",bg="#bde0e9",fg="#000000").place(y=300,x=120)
Checkbutton(text="Ejecutar server al inicio",variable=test2,onvalue="1",offvalue="0",command=aut,bg="#bde0e9").place(y=360,x=120)
Checkbutton(text="Usuario automático",variable=usr_ath,onvalue=1,offvalue=0,command=user_auth,bg="#bde0e9").place(y=390,x=120)
Checkbutton(text="Contraseña automática",variable=pass_auth,onvalue=1,offvalue=0,command=pass_auth_def,bg="#bde0e9").place(y=390,x=320)
Checkbutton(text="ip-port Automatico",variable=ipauth,onvalue=1,offvalue=0,bg="#bde0e9",command=ip_port_auth).place(x=320,y=330)
Checkbutton(text="Mostrar contraseña",variable=test,onvalue="on",offvalue="off",command=show,bg="#bde0e9").place(y=360,x=320)
Checkbutton(text="Anonimo",variable=test3,onvalue=1,offvalue=0,command=ann,bg="#bde0e9").place(y=330,x=120)
Label(text="__________________________________________________________________________",justify="left",bg="#bde0e9",fg="#000000").place(y=480,x=120)

#Menu
menu=Menu(root)
root.config(menu=menu)


ftp1=Menu(menu,tearoff=0)
x=ftp1.add_command(label="Iniciar servidor",command=lambda:ftpstart())
x=ftp1.add_command(label="Parar servidor",command=lambda:ftpstop())

menu.add_cascade(label="ftp",menu=ftp1)

ayuda=Menu(menu,tearoff=0)
ayuda.add_command(label="IP",command=lambda:subprocess.Popen(["python","help\Ftp_help.py"]))
ayuda.add_command(label="Directorio",command=lambda:subprocess.Popen(["python","help\Ftp_help1.py"]))
ayuda.add_command(label="USR-PSS",command=lambda:subprocess.Popen(["python","help\Ftp_help2.py"]))
ayuda.add_command(label="Permisos",command=lambda:subprocess.Popen(["python","help\Ftp_help3.py"]))
menu.add_cascade(label="Ayuda",menu=ayuda)

#Banner
Banner=Label(text="Servidor FTP local V3.7",bg="#bee2b3")
Banner.config(relief="sunken", bd=5, font=("Arial",20),fg="#323836")
Banner.place(x=155)


#IDUP
Label(text="IP",bg="#bde0e9").place(x=120,y=80)
Label(text=":",font=("Arial",15),bg="#bde0e9").place(x=337,y=73)
Label(text="P",bg="#bde0e9").place(x=305,y=159)
Label(text="Directorio",bg="#bde0e9").place(x=120,y=120)
Label(text="User",bg="#bde0e9").place(x=120,y=160)
Label(text="Password",bg="#bde0e9").place(x=120,y=200)

IP=Entry(textvariable=ip,bg="#bde0e9")
Dir=Entry(textvariable=directorio,width=29,bg="#bde0e9",)
Dir.place(x=210,y=120)
Port=Entry(textvariable=port,width=5,bg="#bde0e9")
Port.place(x=350,y=80)
User=Entry(textvariable=user,width=15,bg="#bde0e9",justify="center")
User.place(x=210,y=160)
Perm=Entry(textvariable=perm,width=10,bg="#bde0e9",justify="center")
Perm.place(x=325,y=160)
Pass=Entry(textvariable=pass2,width=29,justify="center")

IP.place(x=210,y=80)
Pass.config(show="*",bg="#bde0e9")
Pass.place(x=210,y=200)
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
	cfg_usr_auth boolean,
	cfg_ip,
	cfg_port INTEGER,
	cfg_dir,
	cfg_usr,
	cfg_pass,
	show,
	cfg_auth INTEGER,
	cfg_pass_auth INTEGER
	)""")
	crud.create("configs","NULL,FALSE,TRUE,0,'"+ip4()+"',2121,"+"'"+os.getcwd()+"'"+",'"+crud.encode("admin")+"','"+crud.encode("admin")+"','off',1,0")
	crud.save()
	read_db=crud.read("configs")
	b64=read_db[0][7],read_db[0][8]
	b64=crud.decode_list(b64)
	print(read_db)
	cfg=read_db[0][1]
	test2.set(str(read_db[0][1]))
	test3.set(str(read_db[0][2]))
	ip2=read_db[0][4]
	port2=read_db[0][5]
	directorio.set(read_db[0][6])
	if read_db[0][3]==1:
		usr_ath.set(1)
		user_auth()
	else:
		usr_ath.set(0)
		user.set(b64[0])
	pass2.set(b64[1])
	test.set(read_db[0][9])
	ipauth.set(read_db[0][10])
	pass_auth.set(read_db[0][11])
	show()
	crud.close()
except:
	read_db=crud.read("configs")
	b64=read_db[0][7],read_db[0][8]
	b64=crud.decode_list(b64)
	print(read_db)
	cfg=read_db[0][1]
	test2.set(str(read_db[0][1]))
	test3.set(str(read_db[0][2]))
	ip2=read_db[0][4]
	port2=read_db[0][5]
	directorio.set(read_db[0][6])
	if read_db[0][3]==1:
		usr_ath.set(1)
		user_auth()
	else:
		usr_ath.set(0)
		user.set(b64[0])
	pass2.set(b64[1])
	test.set(read_db[0][9])
	ipauth.set(read_db[0][10])
	pass_auth.set(read_db[0][11])
	show()
	crud.close()



if cfg==True:
	ftpstart()
	test2.set("1")
else:
	test2.set("0")

anonimo()
perm.set("elradfmw")
show()
port.set(port2)
ip.set(ip2)
root.mainloop()
