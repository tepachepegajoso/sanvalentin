import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random


st.title("Feliz San Valentín Elizalde ❤️")

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

def dibujar_corazon(mensaje, size):

    fig, ax = plt.subplots()
    t = np.linspace(0, 2 * np.pi, 1000)
    x = size * 16 * np.sin(t)**3
    y = size * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))
    ax.plot(x, y, color="red", linewidth=2)
    ax.fill(x, y, color="pink", alpha=0.6)  
    ax.text(0, 0, mensaje, fontsize=12, color="black", ha="center", va="center")
    ax.set_aspect("equal")
    ax.axis("off") 

    return fig


if "corazon_actual" not in st.session_state:
    st.session_state.corazon_actual = None

if st.button("Puchale aquí"):
    mensaje = random.choice(mensajes)
    
    size = random.uniform(0.5, 1.5)  
    fig = dibujar_corazon(mensaje, size)
    st.session_state.corazon_actual = fig

if st.session_state.corazon_actual is not None:
    st.pyplot(st.session_state.corazon_actual)
