import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.geometry('1000x680')
root.title("Justicia & Asociados - LawFirm Management")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Frames para las 4 pestañas (módulos)
tab1 = ttk.Frame(notebook)   # Clientes
tab2 = ttk.Frame(notebook)   # Abogados
tab3 = ttk.Frame(notebook)   # Casos Legales
tab4 = ttk.Frame(notebook)   # Audiencias y Citas

# Añadir las 4 pestañas al Notebook
notebook.add(tab1, text="Clientes")
notebook.add(tab2, text="Abogados")
notebook.add(tab3, text="Casos Legales")
notebook.add(tab4, text="Audiencias y Citas")

# Empaquetar el Notebook
notebook.pack(expand=True, fill="both")


# ================================================================
#   MÓDULO 1: CLIENTES
# ================================================================

def save_cliente():
    messagebox.showinfo("Guardar", "Cliente guardado correctamente")

def update_cliente():
    messagebox.showinfo("Actualizar", "Cliente actualizado correctamente")

def delete_cliente():
    if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este cliente?"):
        messagebox.showinfo("Eliminar", "Cliente eliminado correctamente")

def clear_cliente_form():
    ClienteID.delete(0, tk.END)
    TipoCliente.set("")
    NombreRazonSocial.delete(0, tk.END)
    DocumentoRUC.delete(0, tk.END)
    Direccion_c.delete(0, tk.END)
    Telefono_c.delete(0, tk.END)
    Correo_c.delete(0, tk.END)
    FechaPrimerContacto.delete(0, tk.END)
    ReferidoPor.delete(0, tk.END)
    ClasificacionInterna.delete(0, tk.END)

# --- Contenido pestaña 1 (CLIENTES) ---
titulo1 = tk.Label(tab1, text="GESTIÓN DE CLIENTES", font=("Arial", 16, "bold"), fg="#1a237e")
titulo1.pack(pady=15)

form_frame_clientes = tk.Frame(tab1)
form_frame_clientes.pack(pady=5, anchor="w", padx=60)

# Fila 1: Código Cliente
tk.Label(form_frame_clientes, text="Código Cliente:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=8)
ClienteID = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
ClienteID.grid(row=1, column=1, sticky="w", pady=8)

# Fila 2: Tipo de Cliente (Combobox)
tk.Label(form_frame_clientes, text="Tipo Cliente:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=8)
TipoCliente = tk.StringVar()
combo_tipo = ttk.Combobox(form_frame_clientes, textvariable=TipoCliente,
                           values=["Persona Natural", "Empresa"],
                           width=23, font=("Arial", 12), state="readonly")
combo_tipo.grid(row=2, column=1, sticky="w", pady=8)

# Fila 3: Nombre / Razón Social
tk.Label(form_frame_clientes, text="Nombre / Razón Social:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=8)
NombreRazonSocial = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
NombreRazonSocial.grid(row=3, column=1, sticky="w", pady=8)

# Fila 4: Documento / RUC
tk.Label(form_frame_clientes, text="Documento / RUC:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=8)
DocumentoRUC = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
DocumentoRUC.grid(row=4, column=1, sticky="w", pady=8)

# Fila 5: Dirección
tk.Label(form_frame_clientes, text="Dirección:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=8)
Direccion_c = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
Direccion_c.grid(row=5, column=1, sticky="w", pady=8)

# Fila 6: Teléfono
tk.Label(form_frame_clientes, text="Teléfono:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=8)
Telefono_c = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
Telefono_c.grid(row=6, column=1, sticky="w", pady=8)

# Fila 7: Correo electrónico
tk.Label(form_frame_clientes, text="Correo Electrónico:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=8)
Correo_c = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
Correo_c.grid(row=7, column=1, sticky="w", pady=8)

# Fila 8: Fecha primer contacto
tk.Label(form_frame_clientes, text="Fecha Primer Contacto:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=8)
FechaPrimerContacto = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaPrimerContacto.grid(row=8, column=1, sticky="w", pady=8)

# Fila 9: Referido por
tk.Label(form_frame_clientes, text="Referido Por:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=8)
ReferidoPor = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
ReferidoPor.grid(row=9, column=1, sticky="w", pady=8)

# Fila 10: Clasificación interna
tk.Label(form_frame_clientes, text="Clasificación Interna:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=8)
ClasificacionInterna = tk.Entry(form_frame_clientes, width=25, font=("Arial", 12), relief="solid", bd=1)
ClasificacionInterna.grid(row=10, column=1, sticky="w", pady=8)

# Botones clientes
button_frame_clientes = tk.Frame(tab1)
button_frame_clientes.pack(pady=15)

btn_save_cliente = tk.Button(button_frame_clientes, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_cliente)
btn_save_cliente.pack(side=tk.LEFT, padx=5)

btn_update_cliente = tk.Button(button_frame_clientes, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_cliente)
btn_update_cliente.pack(side=tk.LEFT, padx=5)

btn_delete_cliente = tk.Button(button_frame_clientes, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_cliente)
btn_delete_cliente.pack(side=tk.LEFT, padx=5)

btn_clear_cliente = tk.Button(button_frame_clientes, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_cliente_form)
btn_clear_cliente.pack(side=tk.LEFT, padx=5)


# ================================================================
#   MÓDULO 2: ABOGADOS
# ================================================================

def save_abogado():
    messagebox.showinfo("Guardar", "Abogado guardado correctamente")

def update_abogado():
    messagebox.showinfo("Actualizar", "Abogado actualizado correctamente")

def delete_abogado():
    if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este abogado?"):
        messagebox.showinfo("Eliminar", "Abogado eliminado correctamente")

def clear_abogado_form():
    NumColegiatura.delete(0, tk.END)
    NombresAbogado.delete(0, tk.END)
    ApellidosAbogado.delete(0, tk.END)
    Especialidad.set("")
    AniosExperiencia.delete(0, tk.END)
    FormacionAcademica.delete(0, tk.END)
    Idiomas.delete(0, tk.END)
    TarifaHora.delete(0, tk.END)
    Disponibilidad.set("")

# --- Contenido pestaña 2 (ABOGADOS) ---
titulo2 = tk.Label(tab2, text="GESTIÓN DE ABOGADOS", font=("Arial", 16, "bold"), fg="#1a237e")
titulo2.pack(pady=15)

form_frame_abogados = tk.Frame(tab2)
form_frame_abogados.pack(pady=5, anchor="w", padx=60)

# Fila 1: Número de colegiatura
tk.Label(form_frame_abogados, text="N° Colegiatura:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=8)
NumColegiatura = tk.Entry(form_frame_abogados, width=25, font=("Arial", 12), relief="solid", bd=1)
NumColegiatura.grid(row=1, column=1, sticky="w", pady=8)

# Fila 2: Nombres
tk.Label(form_frame_abogados, text="Nombres:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=8)
NombresAbogado = tk.Entry(form_frame_abogados, width=25, font=("Arial", 12), relief="solid", bd=1)
NombresAbogado.grid(row=2, column=1, sticky="w", pady=8)

# Fila 3: Apellidos
tk.Label(form_frame_abogados, text="Apellidos:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=8)
ApellidosAbogado = tk.Entry(form_frame_abogados, width=25, font=("Arial", 12), relief="solid", bd=1)
ApellidosAbogado.grid(row=3, column=1, sticky="w", pady=8)

# Fila 4: Especialidad (Combobox)
tk.Label(form_frame_abogados, text="Especialidad:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=8)
Especialidad = tk.StringVar()
combo_esp = ttk.Combobox(form_frame_abogados, textvariable=Especialidad,
                          values=["Civil", "Penal", "Laboral", "Tributario", "Mercantil"],
                          width=23, font=("Arial", 12), state="readonly")
combo_esp.grid(row=4, column=1, sticky="w", pady=8)

# Fila 5: Años de experiencia
tk.Label(form_frame_abogados, text="Años de Experiencia:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=8)
AniosExperiencia = tk.Entry(form_frame_abogados, width=25, font=("Arial", 12), relief="solid", bd=1)
AniosExperiencia.grid(row=5, column=1, sticky="w", pady=8)

# Fila 6: Formación académica
tk.Label(form_frame_abogados, text="Formación Académica:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=8)
FormacionAcademica = tk.Entry(form_frame_abogados, width=25, font=("Arial", 12), relief="solid", bd=1)
FormacionAcademica.grid(row=6, column=1, sticky="w", pady=8)

# Fila 7: Idiomas
tk.Label(form_frame_abogados, text="Idiomas:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=8)
Idiomas = tk.Entry(form_frame_abogados, width=25, font=("Arial", 12), relief="solid", bd=1)
Idiomas.grid(row=7, column=1, sticky="w", pady=8)

# Fila 8: Tarifa por hora
tk.Label(form_frame_abogados, text="Tarifa por Hora ($):", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=8)
TarifaHora = tk.Entry(form_frame_abogados, width=25, font=("Arial", 12), relief="solid", bd=1)
TarifaHora.grid(row=8, column=1, sticky="w", pady=8)

# Fila 9: Disponibilidad (Combobox)
tk.Label(form_frame_abogados, text="Disponibilidad:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=8)
Disponibilidad = tk.StringVar()
combo_disp = ttk.Combobox(form_frame_abogados, textvariable=Disponibilidad,
                           values=["Disponible", "Ocupado", "De vacaciones"],
                           width=23, font=("Arial", 12), state="readonly")
combo_disp.grid(row=9, column=1, sticky="w", pady=8)

# Botones abogados
button_frame_abogados = tk.Frame(tab2)
button_frame_abogados.pack(pady=15)

btn_save_abogado = tk.Button(button_frame_abogados, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_abogado)
btn_save_abogado.pack(side=tk.LEFT, padx=5)

btn_update_abogado = tk.Button(button_frame_abogados, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_abogado)
btn_update_abogado.pack(side=tk.LEFT, padx=5)

btn_delete_abogado = tk.Button(button_frame_abogados, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_abogado)
btn_delete_abogado.pack(side=tk.LEFT, padx=5)

btn_clear_abogado = tk.Button(button_frame_abogados, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_abogado_form)
btn_clear_abogado.pack(side=tk.LEFT, padx=5)


# ================================================================
#   MÓDULO 3: CASOS LEGALES
# ================================================================

def save_caso():
    messagebox.showinfo("Guardar", "Caso legal guardado correctamente")

def update_caso():
    messagebox.showinfo("Actualizar", "Caso legal actualizado correctamente")

def delete_caso():
    if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este caso?"):
        messagebox.showinfo("Eliminar", "Caso legal eliminado correctamente")

def clear_caso_form():
    NumeroCaso.delete(0, tk.END)
    TituloDescriptivo.delete(0, tk.END)
    TipoCaso.delete(0, tk.END)
    RamaDelDerecho.set("")
    FechaApertura.delete(0, tk.END)
    ClienteCaso.delete(0, tk.END)
    Contraparte.delete(0, tk.END)
    JuzgadoEntidad.delete(0, tk.END)
    NumExpedienteExterno.delete(0, tk.END)
    AbogadoPrincipal.delete(0, tk.END)
    EstadoActual.set("")
    FechaEstimadaConclusion.delete(0, tk.END)

# --- Contenido pestaña 3 (CASOS LEGALES) con scroll ---
titulo3 = tk.Label(tab3, text="GESTIÓN DE CASOS LEGALES", font=("Arial", 16, "bold"), fg="#1a237e")
titulo3.pack(pady=15)

canvas3 = tk.Canvas(tab3)
scrollbar3 = ttk.Scrollbar(tab3, orient="vertical", command=canvas3.yview)
scroll_frame3 = tk.Frame(canvas3)

scroll_frame3.bind("<Configure>", lambda e: canvas3.configure(scrollregion=canvas3.bbox("all")))
canvas3.create_window((0, 0), window=scroll_frame3, anchor="nw")
canvas3.configure(yscrollcommand=scrollbar3.set)
canvas3.pack(side="left", fill="both", expand=True)
scrollbar3.pack(side="right", fill="y")

form_frame_casos = tk.Frame(scroll_frame3)
form_frame_casos.pack(pady=5, anchor="w", padx=60)

# Fila 1: Número único de caso
tk.Label(form_frame_casos, text="Número de Caso:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=8)
NumeroCaso = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
NumeroCaso.grid(row=1, column=1, sticky="w", pady=8)

# Fila 2: Título descriptivo
tk.Label(form_frame_casos, text="Título Descriptivo:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=8)
TituloDescriptivo = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
TituloDescriptivo.grid(row=2, column=1, sticky="w", pady=8)

# Fila 3: Tipo de caso
tk.Label(form_frame_casos, text="Tipo de Caso:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=8)
TipoCaso = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
TipoCaso.grid(row=3, column=1, sticky="w", pady=8)

# Fila 4: Rama del derecho (Combobox)
tk.Label(form_frame_casos, text="Rama del Derecho:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=8)
RamaDelDerecho = tk.StringVar()
combo_rama = ttk.Combobox(form_frame_casos, textvariable=RamaDelDerecho,
                           values=["Civil", "Penal", "Laboral", "Tributario", "Mercantil", "Administrativo"],
                           width=23, font=("Arial", 12), state="readonly")
combo_rama.grid(row=4, column=1, sticky="w", pady=8)

# Fila 5: Fecha de apertura
tk.Label(form_frame_casos, text="Fecha de Apertura:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=8)
FechaApertura = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaApertura.grid(row=5, column=1, sticky="w", pady=8)

# Fila 6: Cliente
tk.Label(form_frame_casos, text="Cliente:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=8)
ClienteCaso = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
ClienteCaso.grid(row=6, column=1, sticky="w", pady=8)

# Fila 7: Contraparte
tk.Label(form_frame_casos, text="Contraparte:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=8)
Contraparte = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
Contraparte.grid(row=7, column=1, sticky="w", pady=8)

# Fila 8: Juzgado o Entidad
tk.Label(form_frame_casos, text="Juzgado / Entidad:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=8)
JuzgadoEntidad = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
JuzgadoEntidad.grid(row=8, column=1, sticky="w", pady=8)

# Fila 9: N° Expediente externo
tk.Label(form_frame_casos, text="N° Expediente Externo:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=8)
NumExpedienteExterno = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
NumExpedienteExterno.grid(row=9, column=1, sticky="w", pady=8)

# Fila 10: Abogado principal
tk.Label(form_frame_casos, text="Abogado Principal:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=8)
AbogadoPrincipal = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
AbogadoPrincipal.grid(row=10, column=1, sticky="w", pady=8)

# Fila 11: Estado actual (Combobox)
tk.Label(form_frame_casos, text="Estado Actual:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=8)
EstadoActual = tk.StringVar()
combo_estado = ttk.Combobox(form_frame_casos, textvariable=EstadoActual,
                             values=["Abierto", "En proceso", "Suspendido", "Cerrado", "Ganado", "Perdido"],
                             width=23, font=("Arial", 12), state="readonly")
combo_estado.grid(row=11, column=1, sticky="w", pady=8)

# Fila 12: Fecha estimada de conclusión
tk.Label(form_frame_casos, text="Fecha Est. Conclusión:", font=("Arial", 12)).grid(row=12, column=0, sticky="w", padx=(0, 10), pady=8)
FechaEstimadaConclusion = tk.Entry(form_frame_casos, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaEstimadaConclusion.grid(row=12, column=1, sticky="w", pady=8)

# Botones casos
button_frame_casos = tk.Frame(scroll_frame3)
button_frame_casos.pack(pady=15)

btn_save_caso = tk.Button(button_frame_casos, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_caso)
btn_save_caso.pack(side=tk.LEFT, padx=5)

btn_update_caso = tk.Button(button_frame_casos, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_caso)
btn_update_caso.pack(side=tk.LEFT, padx=5)

btn_delete_caso = tk.Button(button_frame_casos, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_caso)
btn_delete_caso.pack(side=tk.LEFT, padx=5)

btn_clear_caso = tk.Button(button_frame_casos, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_caso_form)
btn_clear_caso.pack(side=tk.LEFT, padx=5)


# ================================================================
#   MÓDULO 4: AUDIENCIAS Y CITAS
# ================================================================

def save_audiencia():
    messagebox.showinfo("Guardar", "Audiencia/Cita guardada correctamente")

def update_audiencia():
    messagebox.showinfo("Actualizar", "Audiencia/Cita actualizada correctamente")

def delete_audiencia():
    if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar esta audiencia/cita?"):
        messagebox.showinfo("Eliminar", "Audiencia/Cita eliminada correctamente")

def clear_audiencia_form():
    CodigoAudiencia.delete(0, tk.END)
    TipoAudiencia.set("")
    CasoRelacionado.delete(0, tk.END)
    FechaHoraAudiencia.delete(0, tk.END)
    DuracionEstimada.delete(0, tk.END)
    LugarAudiencia.delete(0, tk.END)
    ParticipantesInternos.delete(0, tk.END)
    ParticipantesExternos.delete(0, tk.END)
    PropositoAudiencia.delete('1.0', tk.END)
    ResultadoEsperado.delete(0, tk.END)
    ResultadoReal.delete(0, tk.END)

# --- Contenido pestaña 4 (AUDIENCIAS Y CITAS) con scroll ---
titulo4 = tk.Label(tab4, text="GESTIÓN DE AUDIENCIAS Y CITAS", font=("Arial", 16, "bold"), fg="#1a237e")
titulo4.pack(pady=15)

canvas4 = tk.Canvas(tab4)
scrollbar4 = ttk.Scrollbar(tab4, orient="vertical", command=canvas4.yview)
scroll_frame4 = tk.Frame(canvas4)

scroll_frame4.bind("<Configure>", lambda e: canvas4.configure(scrollregion=canvas4.bbox("all")))
canvas4.create_window((0, 0), window=scroll_frame4, anchor="nw")
canvas4.configure(yscrollcommand=scrollbar4.set)
canvas4.pack(side="left", fill="both", expand=True)
scrollbar4.pack(side="right", fill="y")

form_frame_audiencias = tk.Frame(scroll_frame4)
form_frame_audiencias.pack(pady=5, anchor="w", padx=60)

# Fila 1: Código
tk.Label(form_frame_audiencias, text="Código:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=8)
CodigoAudiencia = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
CodigoAudiencia.grid(row=1, column=1, sticky="w", pady=8)

# Fila 2: Tipo (Combobox)
tk.Label(form_frame_audiencias, text="Tipo:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=8)
TipoAudiencia = tk.StringVar()
combo_tipo_aud = ttk.Combobox(form_frame_audiencias, textvariable=TipoAudiencia,
                               values=["Audiencia Oral", "Audiencia Preliminar", "Cita con Cliente",
                                       "Reunión Interna", "Conciliación"],
                               width=23, font=("Arial", 12), state="readonly")
combo_tipo_aud.grid(row=2, column=1, sticky="w", pady=8)

# Fila 3: Caso relacionado
tk.Label(form_frame_audiencias, text="Caso Relacionado:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=8)
CasoRelacionado = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
CasoRelacionado.grid(row=3, column=1, sticky="w", pady=8)

# Fila 4: Fecha y hora
tk.Label(form_frame_audiencias, text="Fecha y Hora:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=8)
FechaHoraAudiencia = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaHoraAudiencia.grid(row=4, column=1, sticky="w", pady=8)

# Fila 5: Duración estimada
tk.Label(form_frame_audiencias, text="Duración Estimada:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=8)
DuracionEstimada = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
DuracionEstimada.grid(row=5, column=1, sticky="w", pady=8)

# Fila 6: Lugar
tk.Label(form_frame_audiencias, text="Lugar:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=8)
LugarAudiencia = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
LugarAudiencia.grid(row=6, column=1, sticky="w", pady=8)

# Fila 7: Participantes internos
tk.Label(form_frame_audiencias, text="Participantes Internos:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=8)
ParticipantesInternos = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
ParticipantesInternos.grid(row=7, column=1, sticky="w", pady=8)

# Fila 8: Participantes externos
tk.Label(form_frame_audiencias, text="Participantes Externos:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=8)
ParticipantesExternos = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
ParticipantesExternos.grid(row=8, column=1, sticky="w", pady=8)

# Fila 9: Propósito (Text widget para texto largo)
tk.Label(form_frame_audiencias, text="Propósito:", font=("Arial", 12)).grid(row=9, column=0, sticky="nw", padx=(0, 10), pady=8)
PropositoAudiencia = tk.Text(form_frame_audiencias, width=25, height=4, font=("Arial", 12), relief="solid", bd=1)
PropositoAudiencia.grid(row=9, column=1, sticky="w", pady=8)

# Fila 10: Resultado esperado
tk.Label(form_frame_audiencias, text="Resultado Esperado:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=8)
ResultadoEsperado = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
ResultadoEsperado.grid(row=10, column=1, sticky="w", pady=8)

# Fila 11: Resultado real
tk.Label(form_frame_audiencias, text="Resultado Real:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=8)
ResultadoReal = tk.Entry(form_frame_audiencias, width=25, font=("Arial", 12), relief="solid", bd=1)
ResultadoReal.grid(row=11, column=1, sticky="w", pady=8)

# Botones audiencias
button_frame_audiencias = tk.Frame(scroll_frame4)
button_frame_audiencias.pack(pady=15)

btn_save_audiencia = tk.Button(button_frame_audiencias, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_audiencia)
btn_save_audiencia.pack(side=tk.LEFT, padx=5)

btn_update_audiencia = tk.Button(button_frame_audiencias, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_audiencia)
btn_update_audiencia.pack(side=tk.LEFT, padx=5)

btn_delete_audiencia = tk.Button(button_frame_audiencias, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_audiencia)
btn_delete_audiencia.pack(side=tk.LEFT, padx=5)

btn_clear_audiencia = tk.Button(button_frame_audiencias, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_audiencia_form)
btn_clear_audiencia.pack(side=tk.LEFT, padx=5)


# ================================================================
#   EJECUTAR LA APLICACIÓN
# ================================================================
root.mainloop()