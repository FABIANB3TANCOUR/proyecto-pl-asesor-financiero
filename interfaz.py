from tkinter import messagebox
from motor_inferencia import hechos, cosulta_meses_para_ahorrar, consulta_gastos_requieren_ajuste, consulta_cumple_regla_50_30_20, que_gastos_ajustar
import tkinter as tk

def generar_dict(entrada_gastos, entrada_ingreso, entrada_ahorro):
    try:
        ingresos = float(entrada_ingreso.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un valor valido para los ingresos.")
        return
    ahorro_texto = entrada_ahorro.get().strip()
    ahorro = None
    if ahorro_texto != "":
        try:
            ahorro = float(ahorro_texto)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor válido para la meta de ahorro (o deje el campo vacío).")
            return


    gastos_fijos = []
    gastos_variables = []
    
    for hecho in hechos:
        if hecho[0] == 'gastos' and hecho[2] in entrada_gastos:
            try:
                monto = float(entrada_gastos[hecho[2]].get())
            except ValueError:
                messagebox.showerror("Error", f"Por favor ingrese un valor valido para {hecho[2]}.")
                return
            
            gasto = {hecho[2]: monto}
            if hecho[1] == 'fijos':
                gastos_fijos.append(gasto)
            elif hecho[1] == 'variables':
                gastos_variables.append(gasto)
    
    datos = {
        "ingresos": ingresos,
        "gastos": {
            "fijos": gastos_fijos,
            "variables": gastos_variables
        }
    }
    if ahorro is not None:
        datos["meta_ahorro"] = ahorro

    return datos

def enviar(entrada_gastos, entrada_ingreso, entrada_ahorro):
    datos = generar_dict(entrada_gastos, entrada_ingreso, entrada_ahorro)
    # Ventana 3 - Para realizar consultas
    ventana_consultas = tk.Toplevel(root)
    ventana_consultas.title("Asesor Financiero - Consultas")
    titulo = tk.Label(ventana_consultas, text="Consultas", font=("Helvetica", 16))
    titulo.pack(pady=10)
    btn_requiere_ajuste = tk.Button(ventana_consultas, text="¿Requiere ajuste?", font=("Helvetica", 12), command=lambda: print(consulta_gastos_requieren_ajuste(datos)))
    btn_requiere_ajuste.pack(pady=5)
    btn_cumple_regla = tk.Button(ventana_consultas, text="¿Cumple regla 50-30-20?", font=("Helvetica", 12), command=lambda: print(consulta_cumple_regla_50_30_20(datos)))
    btn_cumple_regla.pack(pady=5)
    btn_recortes = tk.Button(ventana_consultas, text="¿Qué gastos ajustar?", font=("Helvetica", 12), command=lambda: print(que_gastos_ajustar(datos)))
    btn_recortes.pack(pady=5)
    btn_meses_ahorrar = tk.Button(ventana_consultas, text="¿Meses para ahorrar?", font=("Helvetica", 12), command=lambda: print(cosulta_meses_para_ahorrar(datos)))
    btn_meses_ahorrar.pack(pady=5)


def confirmar(checkbox_vars):
    gastos_seleccionados = []
    for nombre, var in checkbox_vars.items():
        if var.get() == 1:
            gastos_seleccionados.append(nombre)
    
    # Ventana 2 - Para ingresar montos
    ventana_gastos = tk.Toplevel(root)
    ventana_gastos.title("Asesor Financiero - Ingreso de Gastos")
    titulo = tk.Label(ventana_gastos, text="Ingreso de Datos", font=("Helvetica", 16))
    titulo.pack(pady=10)
    instruccion = tk.Label(ventana_gastos, text="Ingrese los montos de los gastos seleccionados:", font=("Helvetica", 12))
    instruccion.pack(pady=5)
    entrada_gastos = {}
    for gasto in gastos_seleccionados:
        frame_gasto = tk.Frame(ventana_gastos)
        frame_gasto.pack(pady=5)
        label = tk.Label(frame_gasto, text=f"{gasto.capitalize()}: ", font=("Helvetica", 10))
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame_gasto, font=("Helvetica", 10))
        entry.pack(side=tk.LEFT)
        entrada_gastos[gasto] = entry

    frame_ingreso = tk.Frame(ventana_gastos)
    frame_ingreso.pack(pady=5)
    label_ingreso = tk.Label(frame_ingreso, text="Ingresos mensuales: ", font=("Helvetica", 10))
    label_ingreso.pack(side=tk.LEFT)
    entry_ingreso = tk.Entry(frame_ingreso, font=("Helvetica", 10))
    entry_ingreso.pack(side=tk.LEFT)
    entrada_ingreso = entry_ingreso

    frame_ahorro = tk.Frame(ventana_gastos)
    frame_ahorro.pack(pady=5)
    label_ahorro = tk.Label(frame_ahorro, text="Meta de ahorro mensual (opcional): ", font=("Helvetica", 10))
    label_ahorro.pack(side=tk.LEFT)
    entry_ahorro = tk.Entry(frame_ahorro, font=("Helvetica", 10))
    entry_ahorro.pack(side=tk.LEFT)
    entrada_ahorro = entry_ahorro
    


    btn_enviar = tk.Button(ventana_gastos, text="Enviar", font=("Helvetica", 12), command=lambda: enviar(entrada_gastos, entrada_ingreso, entrada_ahorro))
    btn_enviar.pack(pady=20)


#Ventana principal - para seleccionar gastos
root = tk.Tk()
root.title("Asesor Financiero")
root.geometry("500x600")
titulo = tk.Label(root, text="Asesor Financiero", font=("Helvetica", 16))
titulo.pack(pady=10)

subtitulo = tk.Label(root, text="Seleccione los gastos con los que cuenta:", font=("Helvetica", 12))
subtitulo.pack(pady=5)
frame = tk.Frame(root)
frame.pack(pady=10)

checkbox_vars = {}
# Checkboxes para gastos
for hecho in hechos:
    if hecho[0] == 'gastos':
        var = tk.IntVar()
        cb = tk.Checkbutton(frame, text=f"{hecho[2]}".capitalize(), variable=var, font=("Helvetica", 10))
        cb.pack(anchor='w')
        checkbox_vars[(hecho[2])] = var

btn =  tk.Button(root, text="confirmar", font=("Helvetica", 12), command=lambda: confirmar(checkbox_vars))
btn.pack(pady=20)

root.mainloop()