from tkinter import *
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk
import csv
from csv import writer
import os



def verificarCodigoExistente(codigo):
    with open('GuestList/lista.csv', mode='r') as csv_file:
        significado=False
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["codigo"]==codigo:
                significado=True
    return significado

def registrarUsuario(codigo,nombre,apellido,numero):
    list_data=[codigo,nombre,apellido,numero]
    with open('GuestList/lista.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(list_data)  
        f_object.close()
    
def crearBBDD():
    if not (os.path.exists("GuestList/lista.csv")):
        registrarUsuario("codigo","nombre","apellido","telefono")
    else:
        pass

def registro():
    crearBBDD()
    if verificarCodigoExistente(codigoVar.get())==False:
        if codigoVar.get()!="" and nombreVar.get()!="" and apellidoVar.get()!="" and telefonoVar.get()!="":
            if len(codigoVar.get())<=4:
                messagebox.showinfo(title=None, message="Usuario Registrado Correctamente.")
                registrarUsuario(codigoVar.get(),nombreVar.get(),apellidoVar.get(),telefonoVar.get())
                codigoVar.set("")
                nombreVar.set("")
                apellidoVar.set("")
                telefonoVar.set("")
            else:
                messagebox.showwarning(title=None, message="Máximo de carracteres del codigo es de 4")
        else:
            messagebox.showwarning(title=None, message="Completar todos los datos.")

    else:
        messagebox.showwarning(title=None, message="El código escrito ya esta existente.")

def resetear():
    if not (os.path.exists("GuestList/lista.csv")):
        messagebox.showwarning(title=None, message="La base de datos nunca existió.")  

    if (os.path.exists("GuestList/lista.csv")):
        if messagebox.askyesno('Verificar', '¿Realmente quiere eliminar la base de datos actual?'):
            os.remove("GuestList/lista.csv")
            os.remove("ListadoInvitados.txt")
            messagebox.showwarning('Si', 'Base de datos eliminada con exito.')
        else:
            messagebox.showinfo('No', 'Salir fue cancelado')
    
def listado():
    if os.path.exists("ListadoInvitados.txt"):
        os.remove("ListadoInvitados.txt")

    results = []
    with open('GuestList/lista.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)

    f = open ('ListadoInvitados.txt','w')
    f.write('Lista de invitados'"\n")
    f.write('')
    for i in results:
        f.write("Codigo:"+i['codigo']+" Nombre:"+i['nombre']+" Apellido:"+i['apellido']+"\n")
    f.close()


def frameMain():
    root=Tk()

    ancho_ventana =500
    alto_ventana=300

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    root.geometry(posicion)
    root.configure(background="white")
    root.title("Guest List")
    root.resizable(width=False,height=False)
    root.configure(background='black')
    root.iconbitmap('PartyDayValidation/Logo.ico')


    titulo=Label(root,text="Guest List",width=25,background="white",fg="black",font=("Bookman Old Style",30)).place(x=120,y=30,anchor=CENTER,height=60)

    global codigoVar
    global nombreVar
    global apellidoVar
    global telefonoVar

    codigoVar=StringVar()
    nombreVar=StringVar()
    apellidoVar=StringVar()
    telefonoVar=StringVar()

    idLabel=Label(root,text="Código: ",width=15,background="black",fg="white",font=("Bookman Old Style",10)).place(x=120,y=100,anchor=CENTER,height=20)
    idNombre=Label(root,text="Nombre: ",width=15,background="black",fg="white",font=("Bookman Old Style",10)).place(x=120,y=130,anchor=CENTER,height=20)
    idApellido=Label(root,text="Apellido: ",width=15,background="black",fg="white",font=("Bookman Old Style",10)).place(x=120,y=160,anchor=CENTER,height=20)
    idTelefono=Label(root,text="Telefono: ",width=15,background="black",fg="white",font=("Bookman Old Style",10)).place(x=120,y=190,anchor=CENTER,height=20)


    id=Entry(root,width=18,background="white",fg="black",font=("Bookman Old Style",10),relief="groove",textvariable=codigoVar).place(x=250,y=100,anchor=CENTER,height=20)
    nombre=Entry(root,width=18,background="white",fg="black",font=("Bookman Old Style",10),relief="groove",textvariable=nombreVar).place(x=250,y=130,anchor=CENTER,height=20)
    apellido=Entry(root,width=18,background="white",fg="black",font=("Bookman Old Style",10),relief="groove",textvariable=apellidoVar).place(x=250,y=160,anchor=CENTER,height=20)
    telefono=Entry(root,width=18,background="white",fg="black",font=("Bookman Old Style",10),relief="groove",textvariable=telefonoVar).place(x=250,y=190,anchor=CENTER,height=20)

    im = PIL.Image.open("GuestList/barra.png")
    photo = PIL.ImageTk.PhotoImage(im)
    imagenPerfil=Label(root,image=photo,height=300,width=100).place(x=380,y=0)

    buscar=Button(root,text="Registrar",width=10,background="white",fg="black",font=("Calibri Light",10),relief="groove",command=registro).place(x=100,y=250,anchor=CENTER,height=20)
    listar=Button(root,text="Listado",width=10,background="white",fg="black",font=("Calibri Light",10),relief="groove",command=listado).place(x=200,y=250,anchor=CENTER,height=20)
    reset=Button(root,text="Resetear",width=10,background="white",fg="black",font=("Calibri Light",10),relief="groove",command=resetear).place(x=300,y=250,anchor=CENTER,height=20)
    


    root.mainloop()

if __name__ == '__main__':
        frameMain()