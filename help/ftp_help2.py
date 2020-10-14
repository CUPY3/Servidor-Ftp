#Ftp help 3
import tkinter

root=tkinter.Tk()

root.title("FTP-HELP USR-PSS")


usr=tkinter.PhotoImage(file="help\_user-password.png")

root.geometry("520x250")
tkinter.Label(text="Ftp Config Help N°3\nUser and Password",justify="center",bd=5,relief="sunken",font=("Arial",20)).place(x=120,y=0)
tkinter.Label(text="El usuario y la contraseña son muy importantes\npara la proteccion del servidor").place(x=110,y=80)
tkinter.Label(image=usr).place(x=60,y=120)

tkinter.Label(text="Sin estas este podria ser hackeado").place(x=150,y=220)



root.mainloop()
