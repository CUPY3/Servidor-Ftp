# Ftp server
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
	ip2=io.open("ip","w")
	ip2.write(str(ip.get()))
	ip2.close()
	
#---------------------------------------------------------------------------------------#

def main():
	global server,FTP_DIRECTORY
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
	savedir(FTP_DIRECTORY)
	admin()
	adminpass()
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
	
	FTP_USER = user.get()
	FTP_PASSWORD = pass2.get()
	FTP_DIRECTORY = directorio.get()
	
	ip2=io.open("configs\ip","w")
	ip2.write(str(ip.get()))
	ip2.close()
	
	port2=io.open("configs\port","w")
	port2.write(str(port.get()))
	port2.close()
	
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
	else:
		Pass.config(show="*")	

def conf():
	cfg=io.open("configs\cfg","w")
	cfg.write(test2.get())
	cfg.close()

def change():
	global annonimus
	annonimus=test3.get()

def savedir(dir2):
	dirn=io.open("configs\dir","w")
	dirn.write(dir2)
	dirn.close()
def admin():
	use=io.open("configs\.User","w")
	use.write(user.get())
	use.close()
def adminpass():
	use=io.open("configs\pss","w")
	use.write(pass2.get())
	use.close()
def selecdir():
	dire=filedialog.askdirectory()
	if dire=="":
		directorio.set(os.getcwd())
	else:
		directorio.set(dire)


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
#Variables
annonimus=test3.get()
portauth.set("off")

#checkbuttons
Label(text="__________________________________________________________________________",justify="left",bg="#bde0e9",fg="#000000").place(y=300,x=120)
Checkbutton(text="Ejecutar server al iniciar la app",variable=test2,onvalue="on",offvalue="off",command=conf,bg="#bde0e9").place(y=340,x=200)
Checkbutton(text="Automatico",variable=ipauth,onvalue="on",offvalue="off",bg="#bde0e9").place(x=400,y=80)
Checkbutton(text="show",variable=test,onvalue="on",offvalue="off",command=show,bg="#bde0e9").place(y=200,x=400)
Checkbutton(text="Anonimo",variable=test3,onvalue="on",offvalue="off",command=change,bg="#bde0e9").place(y=160,x=400)

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
Banner=Label(text="Servidor FTP local V2.2",bg="#bee2b3")
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
	cfg=io.open("configs\cfg","r")
except:
	os.system("mkdir configs")
	cfg=io.open("configs\cfg","w")
	cfg.write("off")
	cfg.close()
	cfg=io.open("configs\cfg","r")


if cfg.read()=="on":
	ftpstart()
else:
	test2.set("off")
cfg.close()

try:
	ip1=io.open("configs\ip","r")
	ip2=ip1.read()
	ip1.close()
except:
	ip1=io.open("configs\ip","w")
	ip1.write("127.0.0.1")
	ip1.close()
	ip1=io.open("configs\ip","r")
	ip2=ip1.read()
	ip1.close()
try:
	port1=io.open("configs\port","r")
	port2=port1.read()
	port1.close()
except:
	port1=io.open("configs\port","w")
	port1.write("2121")
	port1.close()
	port1=io.open("configs\port","r")
	port2=port1.read()
	port1.close()

try:
	dirn=io.open("configs\dir","r")
	directorio.set(dirn.read())
	dirn.close()
except:
	directorio.set(os.getcwd())
try:
	use=io.open('configs\.User',"r")
	use2=use.read()
	use.close
	user.set(use2)
except:
	user.set("admin")
	admin()
try:
	pass8=io.open("configs\pss","r")
	pass2.set(pass8.read())
	pass8.close()
except:
	pass2.set("admin")
	adminpass()


test.set("off")
show()
ipauth.set("off")
test3.set("off")
port.set(port2)
ip.set(ip2)
root.mainloop()
