#Ftp help 1
import tkinter

root=tkinter.Tk()

root.title("FTP-HELP IP")

ip_port=tkinter.PhotoImage(file="help\Ftp_ip-port.png")
ip_port_yes=tkinter.PhotoImage(file="help\Ftp_ip-port-yes.png")

root.geometry("520x270")
tkinter.Label(text="Ftp Config Help N°1\nIP",justify="center",bd=5,relief="sunken",font=("Arial",20)).place(x=120,y=0)
tkinter.Label(text="Primero se configura el IP y el Puerto de su servidor").place(x=110,y=80)
tkinter.Label(image=ip_port).place(x=60,y=110)

tkinter.Label(text="Si quiere puede dejar que el programa lo configure\n automaticamente presionando la casilla 'automatico'").place(x=100,y=165)
tkinter.Label(image=ip_port_yes).place(x=60,y=210)


root.mainloop()
