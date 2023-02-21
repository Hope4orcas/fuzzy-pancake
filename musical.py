import streamlit as st
import random
st.title("Elija su tipo de música")

opciones=("Alt","Pop", "Reggaeton","Vocaloid","Kpop")

respuesta=st.radio("¿Género de música favorito?", opciones)

choice_alt=["https://www.youtube.com/watch?v=dn5rSbHGsHY",
            "https://www.youtube.com/watch?v=qolmz4FlnZ0",
            "https://www.youtube.com/watch?v=iggmiF7DNoM"
            ]
choice_pop=["https://www.youtube.com/watch?v=wV1FrqwZyKw",
            "https://www.youtube.com/watch?v=QYh6mYIJG2Y",
            "https://www.youtube.com/watch?v=e-ORhEE9VVg"
            ]
choice_kpop=["https://www.youtube.com/watch?v=pyf8cbqyfPs",
            "https://www.youtube.com/watch?v=KhTeiaCezwM",
            "https://www.youtube.com/watch?v=Jh4QFaPmdss"
            ]
choice_voc=["https://www.youtube.com/watch?v=ScSW9C3DF18",
            "https://www.youtube.com/watch?v=Av04XfLtAcU",
            "https://www.youtube.com/watch?v=TNf3GPizM58"
            ]
if respuesta=="Alt":
  st.write("maravilloso")
  st.video(random.choice(choice_alt))
if respuesta=="Pop":
  st.write("gg")
  st.video(random.choice(choice_pop))
if respuesta=="Kpop":
  st.write("OMG")
  st.video(random.choice(choice_kpop))
if respuesta=="Vocaloid":
  st.write("Yasssss")
  st.video(random.choice(choice_voc))
