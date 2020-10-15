#Ftp help 3
import tkinter

root=tkinter.Tk()

root.title("FTP-HELP PERMISOS")
root.config(bg="#bde0e9")
root.resizable(0,0)

root.geometry("520x550")
tkinter.Label(text="Ftp Config Help N°4\nPERMISOS",justify="center",bd=5,relief="sunken",font=("Arial",20),bg="#bee2b3").place(x=120,y=0)
tkinter.Label(text="Los permisos son el tipo de acceso que tendra el usuario",justify="center",font="Arial",bg="#bee2b3").place(x=50,y=90)
tkinter.Label(text="""Permisos de lectura:

    "E" • cambiar directorio (CWD, comandos CDUP)
    "L" • archivos de lista (comandos LIST, NLST, STAT, MLSD, MLST, SIZE)
    "R" • Recuperar archivo del servidor (mandato RETR)

Permisos de escritura:

    "A" • anexar datos a un archivo existente (comando APPE)
    "D" • Eliminar archivo o directorio (deLE, comandos RMD)
    "F" • cambiar el nombre del archivo o directorio (RNFR, comandos RNTO)
    "M" • crear directorio (comando MKD)
    "W" • almacenar un archivo en el servidor (comandos STOR, STOU)
    "M" • Cambiar el modo de archivo / permiso (comando SITE CHMOD)
    "T" • cambiar el tiempo de modificación del archivo""",bg="#bde0e9").place(x=45,y=120)



root.mainloop()
