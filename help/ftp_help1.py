#Ftp help 2
import tkinter

root=tkinter.Tk()

root.title("FTP-HELP Dir")

dire=tkinter.PhotoImage(file="help\dir.png")

root.geometry("520x230")
tkinter.Label(text="Ftp Config Help N°2\nDirectorio",justify="center",bd=5,relief="sunken",font=("Arial",20)).place(x=120,y=0)
tkinter.Label(text="El directorio es simplemente el lugar a donde el\nservidor va a guardar o mostrar los archivos").place(x=110,y=80)
tkinter.Label(image=dire).place(x=60,y=120)

tkinter.Label(text="Para configurarlo solo debe escribir el directorio o\ntocar en 'seleccionar'y buscar el directorio deseado").place(x=100,y=175)



root.mainloop()
