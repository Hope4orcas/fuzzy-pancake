import streamlit as st
import random
st.title("Elija su tipo de música")

opciones=("Alt","Pop","Rock", "Reggaeton","Vocaloid","Kpop")

respuesta=st.radio("¿Género de música favorito?", opciones)

choice_alt=["https://www.youtube.com/watch?v=dn5rSbHGsHY",
            "https://www.youtube.com/watch?v=qolmz4FlnZ0",
            "https://www.youtube.com/watch?v=iggmiF7DNoM"
            ]
choice_pop=["https://www.youtube.com/watch?v=wV1FrqwZyKw",
            "https://www.youtube.com/watch?v=QYh6mYIJG2Y",
            "https://www.youtube.com/watch?v=e-ORhEE9VVg"
            ]

if respuesta=="Alt":
  st.write("maravilloso")
  st.video(random.choice(choice_alt))
if respuesta=="Pop":
  st.write("gg")
  st.video(random.choice(choice_pop))
