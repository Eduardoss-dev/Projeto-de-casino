import requests
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from io import BytesIO

frames = []

def animar(indice):
    if frames:
        frame = frames[indice]
        label_imagem.config(image=frame)
        indice = (indice + 1) % len(frames)
        janela.after(100, animar, indice)

def buscar_pokemon():
    global frames

    nome = entrada.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        nome_label.config(text=dados["name"].capitalize())

        tipos = [t["type"]["name"] for t in dados["types"]]
        tipo_label.config(text="Tipo: " + ", ".join(tipos))

        info_label.config(
            text=f"Altura: {dados['height']}   Peso: {dados['weight']}"
        )

        # GIF animado
        gif_url = dados["sprites"]["versions"]["generation-v"]["black-white"]["animated"]["front_default"]

        if not gif_url:
            gif_url = dados["sprites"]["front_default"]

        img_resposta = requests.get(gif_url)
        gif = Image.open(BytesIO(img_resposta.content))

        frames = []
        for frame in ImageSequence.Iterator(gif):
            frame = frame.resize((180, 180))
            frames.append(ImageTk.PhotoImage(frame))

        animar(0)

    else:
        nome_label.config(text="Não encontrado")
        tipo_label.config(text="")
        info_label.config(text="")
        label_imagem.config(image="")

# 🎨 Interface estilo Pokédex
janela = tk.Tk()
janela.title("Pokédex")
janela.geometry("350x500")
janela.configure(bg="#cc0000")  # vermelho pokedex

# Tela (parte branca)
tela = tk.Frame(janela, bg="black", bd=5)
tela.place(x=30, y=80, width=290, height=250)

label_imagem = tk.Label(tela, bg="black")
label_imagem.pack(expand=True)

# Nome
nome_label = tk.Label(janela, text="", font=("Arial", 16, "bold"), bg="#cc0000", fg="white")
nome_label.place(x=30, y=340)

# Tipo
tipo_label = tk.Label(janela, text="", font=("Arial", 10), bg="#cc0000", fg="white")
tipo_label.place(x=30, y=370)

# Info
info_label = tk.Label(janela, text="", font=("Arial", 10), bg="#cc0000", fg="white")
info_label.place(x=30, y=400)

# Entrada
entrada = tk.Entry(janela, font=("Arial", 12))
entrada.place(x=30, y=30, width=200)

# Botão
botao = tk.Button(
    janela,
    text="Buscar",
    command=buscar_pokemon,
    bg="white",
    fg="black"
)
botao.place(x=240, y=28)

# Botões decorativos estilo pokedex
tk.Canvas(janela, width=20, height=20, bg="blue", highlightthickness=0).place(x=30, y=450)
tk.Canvas(janela, width=20, height=20, bg="yellow", highlightthickness=0).place(x=60, y=450)
tk.Canvas(janela, width=20, height=20, bg="green", highlightthickness=0).place(x=90, y=450)

janela.mainloop()