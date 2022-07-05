from tkinter import *
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk
import csv
import os

def verificarCodigoExistente(codigo):
    with open('GuestList/lista.csv', mode='r') as csv_file:
        significado=False
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["codigo"]==codigo:
                significado=True
        return significado

def registro(codigo):
    with open('GuestList/lista.csv', 'r') as file :
        filedata = file.read()

    filedata = filedata.replace(codigo, 'Presente')

    with open('GuestList/lista.csv', 'w') as file:
        file.write(filedata)
  
def verificar():
    if not (os.path.exists("GuestList/lista.csv")):
        messagebox.showwarning(title=None, message="La base de datos nunca existió.") 

    if (os.path.exists("GuestList/lista.csv")):
        if verificarCodigoExistente(codigoVar.get())==True:
            registro(codigoVar.get())
            messagebox.showinfo(title=None, message="Acceso Permitido")
        else:
            messagebox.showwarning(title=None, message="Acesso Denegado! La persona ya ingreso a la fiesta o no está en la lista.")
            
def listado():
    if os.path.exists("ListadoInvitados.txt"):
        if messagebox.askyesno('Verificar', '¿Realmente a terminado el evento, se eliminará la base de datos actual y se le mostrará el listado final?'):
            os.remove("ListadoInvitados.txt")
            results = []
            with open('GuestList/lista.csv') as File:
                reader = csv.DictReader(File)
                for row in reader:
                    results.append(row)

            f = open ('ListadoInvitados.txt','w')
            f.write('Lista de invitados'"\n")
            f.write('')
            cantidad=0
            for i in results:
                f.write("Codigo:"+i['codigo']+" Nombre:"+i['nombre']+" Apellido:"+i['apellido']+" Numero:"+i['telefono']+"\n")
                cantidad+=1
            f.write("\n")
            f.write("Invitados totales: "+str(cantidad)+"\n")
            f.close()
            os.remove("GuestList/lista.csv")
            messagebox.showwarning('Si', 'Base de datos eliminada con exito.')

        else:
            messagebox.showinfo('No', 'Salir fue cancelado')
        
    else:
        messagebox.showwarning(title=None, message="Nunca se generó el listado de invitado.") 

 
def frameMain():
    root=Tk()

    ancho_ventana =500
    alto_ventana=150

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    root.geometry(posicion)
    root.configure(background="white")
    root.title("Party Day Validation")
    root.resizable(width=False,height=False)
    root.configure(background='black')
    root.iconbitmap('GuestList/logo.ico')


    titulo=Label(root,text="Validation",width=25,background="white",fg="black",font=("Bookman Old Style",30)).place(x=120,y=30,anchor=CENTER,height=60)

    global codigoVar
    codigoVar=StringVar()


    idLabel=Label(root,text="Código: ",width=15,background="black",fg="white",font=("Bookman Old Style",10)).place(x=120,y=80,anchor=CENTER,height=20)
    id=Entry(root,width=18,background="white",fg="black",font=("Bookman Old Style",10),relief="groove",textvariable=codigoVar).place(x=250,y=80,anchor=CENTER,height=20)


    im = PIL.Image.open("GuestList/barra.png")
    photo = PIL.ImageTk.PhotoImage(im)
    imagenPerfil=Label(root,image=photo,height=300,width=100).place(x=380,y=0)

    verifica=Button(root,text="Verificar",width=10,background="white",fg="black",font=("Calibri Light",10),relief="groove",command=verificar).place(x=150,y=120,anchor=CENTER,height=20)
    lista=Button(root,text="Final Evento",width=10,background="white",fg="black",font=("Calibri Light",10),relief="groove",command=listado).place(x=250,y=120,anchor=CENTER,height=20)


    root.mainloop()

if __name__ == '__main__':
        frameMain()