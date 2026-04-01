# ⚖️ Justicia & Asociados — LawFirm Management System

Sistema de gestión de escritorio para el bufete de abogados **"Justicia & Asociados"**, desarrollado en Python con interfaz gráfica Tkinter.

---

## 📋 Descripción

Aplicación que centraliza la administración de los procesos clave del bufete: clientes, abogados, casos legales y audiencias. Desarrollado como proyecto universitario aplicando programación orientada a objetos, estructuras de control, funciones y la librería Tkinter.

---

## 🗂️ Módulos del sistema

| # | Módulo | Descripción |
|---|--------|-------------|
| 1 | **Clientes** | Registro de personas naturales y empresas con toda su información de contacto |
| 2 | **Abogados** | Datos profesionales, especialidades, tarifa por hora y disponibilidad |
| 3 | **Casos Legales** | Apertura y seguimiento completo de casos con estado actual |
| 4 | **Audiencias y Citas** | Agenda de audiencias judiciales y reuniones con participantes |

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Librería `tkinter` *(viene incluida con Python por defecto, no requiere instalación adicional)*

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/lawfirm.git
cd lawfirm
```

### 2. Verificar que Python esté instalado

```bash
python --version
```

> Debe mostrar Python 3.8 o superior.

### 3. Ejecutar el sistema

```bash
python lawfirm.py
```

> No se requiere instalar ninguna dependencia adicional.

---

## 🖥️ Uso de la aplicación

1. Al abrir la aplicación verás **4 pestañas** en la parte superior, una por módulo.
2. Navega entre ellas haciendo clic en cada una.
3. Completa los campos del formulario correspondiente.
4. Usa los botones de acción:

| Botón | Color | Función |
|-------|-------|---------|
| **Guardar** | Verde | Registra la información del formulario |
| **Actualizar** | Azul | Modifica un registro existente |
| **Eliminar** | Rojo | Elimina el registro (pide confirmación) |
| **Limpiar** | Naranja | Borra todos los campos del formulario |

> Los módulos **Casos Legales** y **Audiencias y Citas** tienen barra de desplazamiento vertical para ver todos los campos.

---

## 📁 Estructura del proyecto

```
lawfirm/
│
├── lawfirm.py       # Script principal con los 4 módulos
└── README.md        # Instrucciones de instalación y uso
```

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| **Python 3** | Lenguaje de programación principal |
| **Tkinter** | Construcción de la interfaz gráfica (GUI) |
| **ttk** | Widgets mejorados: Notebook, Combobox, Scrollbar |
| **messagebox** | Ventanas de confirmación y alertas |

---

## 👨‍💻 Autor

Proyecto universitario — Programación con Python  
Bufete de abogados: **Justicia & Asociados**
