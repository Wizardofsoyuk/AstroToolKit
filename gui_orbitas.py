import tkinter as tk
from tkinter.ttk import LabelFrame

from matplotlib import image
import modulos as md
from PIL import ImageTk, Image
import os

def GUI():
    imagen_status =False
    memoria = []
    counter_planet=1
    def acumular_planetas():
        dato = [float(ent_excentricidad.get()),float(ent_semiejemayor.get()),ent_Name.get()]
        memoria.append(dato)
        caja_de_texto.configure(state="normal")
        caja_de_texto.insert(f"{counter_planet}.0",f"\nCuerpo: {ent_Name.get()} | Excentricidad: {ent_excentricidad.get()} | Semieje Mayor: {ent_semiejemayor.get()} UA")
        caja_de_texto.configure(state="disabled")

    def limpiar():
        nonlocal imagen_status
        ent_excentricidad.delete(0, tk.END)
        ent_semiejemayor.delete(0, tk.END)
        ent_Name.delete(0, tk.END)
        memoria.clear()
        if imagen_status == True:
            panel.pack_forget()
            frame_imagen.pack_forget()
            imagen_status =False
        caja_de_texto.configure(state="normal")
        caja_de_texto.delete("1.0", tk.END)
        caja_de_texto.configure(state="disabled")
    
    def colocar_orbita():
        nonlocal imagen_status
        if len(memoria) == 0:
            e=float(ent_excentricidad.get())
            a=float(ent_semiejemayor.get())
            database=md.calcular_posiciones_orbit(e,a,ent_Name.get())
            database = [database]
        else:
            database=[]
            for dato in memoria:
                database_mini = md.calcular_posiciones_orbit(dato[0],dato[1],dato[2])
                database.append(database_mini)
        if imagen_status == True:
            limpiar()
        global frame_imagen 
        frame_imagen= tk.Frame()
        frame_imagen.pack(fill=tk.X, ipadx=5, ipady=5)
        md.dibujar_orbita(database)
        img = ImageTk.PhotoImage(Image.open("orbita.gif"))
        global panel 
        panel = tk.Label(frame_imagen,image=img)
        panel.image=img
        panel.pack()
        imagen_status=True

    ventana = tk.Tk()
    ventana.title("Graficador de Órbitas")

    frame_entradas=tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frame_entradas.pack()

    lbl_excentricidad = tk.Label(master= frame_entradas, text="Coloque su valor de excentricidad: ", font="Helvetica 12")
    lbl_excentricidad.grid(row=0,column= 0,sticky = "e")
    ent_excentricidad = tk.Entry(master=frame_entradas,width= 50)
    ent_excentricidad.grid(row=0,column=1)

    lbl_semiejemayor = tk.Label(master= frame_entradas, text="Coloque su valor del semieje mayor (UA): ", font="Helvetica 12")
    lbl_semiejemayor.grid(row=1,column= 0,sticky = "e")
    ent_semiejemayor = tk.Entry(master=frame_entradas,width= 50)
    ent_semiejemayor.grid(row=1,column=1)

    lbl_Name = tk.Label(master= frame_entradas, text="Inserte el Nombre del Cuerpo", font="Helvetica 12")
    lbl_Name.grid(row=2,column= 0,sticky = "e")
    ent_Name = tk.Entry(master=frame_entradas,width= 50)
    ent_Name.grid(row=2,column=1)

    frame_buttons = tk.Frame()
    frame_buttons.pack( ipadx=5, ipady=5)

    btn_crear_orbita=tk.Button(master = frame_buttons,text="Crear Orbita",command=colocar_orbita)
    btn_crear_orbita.pack(side = tk.RIGHT,padx=10,ipadx=10)
    btn_limpiar=tk.Button(master = frame_buttons,text="Limpiar", command= limpiar)
    btn_limpiar.pack(side = tk.RIGHT,ipadx=10)
    btn_añadir_mas_cuerpos=tk.Button(master = frame_buttons,text="Añadir Cuerpo", command= acumular_planetas)
    btn_añadir_mas_cuerpos.pack(side = tk.RIGHT,ipadx=10,padx=10)

    frame_texto = tk.Frame()
    frame_texto.pack(fill=tk.X,ipadx=5,ipady=5)
    caja_de_texto = tk.Text(master=frame_texto,height=5,state='disabled',font="Helvetica 12")
    caja_de_texto.pack()
    ventana.resizable(False, False) 
    ventana.mainloop()

GUI()


