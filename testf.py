import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# Título de la aplicación
st.title("Feliz San Valentín Elizalde ❤️")

# Lista de mensajes
mensajes = [
    "Roma", 
    "mundo", 
    "maravilla", 
    "lunas", 
    "gravedad", 
    "sonrisa", 
    "atmósfera", 
    "consentir", 
    "pulmones", 
    "simétricos", 
    "culturas", 
    "místicas", 
    "cerebro", 
    "enigmático", 
    "natural", 
    "sol", 
    "enamorar", 
    "hacerte", 
    "bello", 
    "imperios", 
    "esplendor", 
    "fisonomía", 
    "inicio", 
    "creación", 
    "viajar", 
    "espacio", 
    "frenesí", 
    "revolución", 
    "mil años", 
    "luz", 
    "lado"
]


# Función para dibujar un corazón con un mensaje
def dibujar_corazon(mensaje, size):
    # Crear la figura
    fig, ax = plt.subplots()

    # Parámetros del corazón
    t = np.linspace(0, 2 * np.pi, 1000)
    x = size * 16 * np.sin(t)**3
    y = size * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))

    # Dibujar el corazón
    ax.plot(x, y, color="red", linewidth=2)
    ax.fill(x, y, color="pink", alpha=0.6)  # Rellenar el corazón

    # Agregar el mensaje dentro del corazón
    ax.text(0, 0, mensaje, fontsize=12, color="black", ha="center", va="center")

    # Configurar el aspecto del gráfico
    ax.set_aspect("equal")
    ax.axis("off")  # Ocultar ejes

    return fig

# Inicializar el estado del corazón en la sesión
if "corazon_actual" not in st.session_state:
    st.session_state.corazon_actual = None

# Botón para dibujar corazones
if st.button("Puchale aquí"):
    # Seleccionar un mensaje aleatorio
    mensaje = random.choice(mensajes)
    
    # Generar un tamaño aleatorio para el corazón
    size = random.uniform(0.5, 1.5)  # Tamaño entre 0.5 y 1.5 veces el original
    
    # Dibujar el corazón con el mensaje
    fig = dibujar_corazon(mensaje, size)
    
    # Guardar el corazón actual en el estado de la sesión
    st.session_state.corazon_actual = fig

# Mostrar el corazón actual
if st.session_state.corazon_actual is not None:
    st.pyplot(st.session_state.corazon_actual)