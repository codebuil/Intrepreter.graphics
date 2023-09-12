from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog

# Função para desenhar uma linha
def draw_line(draw, args):
    draw.line(args, fill="white", width=1)

# Função para desenhar um retângulo vazado
def draw_rect(draw, args):
    draw.rectangle(args, outline="white", width=1)

# Função para desenhar um retângulo preenchido
def draw_box(draw, args):
    draw.rectangle(args, fill="white", outline="white")

# Função para desenhar um círculo vazado
def draw_circle(draw, args):
    draw.ellipse(args, outline="white", width=1)

# Função para desenhar um círculo preenchido
def draw_filled_circle(draw, args):
    draw.ellipse(args, fill="white", outline="white")

# Função principal do interpretador
def interpretador_grafico(commands):
    width, height = 800, 600
    image = Image.new("RGB", (width, height), "blue")
    draw = ImageDraw.Draw(image)

    for command in commands:
        parts = command.split(",")
        keyword = parts[0]

        if keyword == "line":
            draw_line(draw, [int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])])
        elif keyword == "rect":
            draw_rect(draw, [int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])])
        elif keyword == "box":
            draw_box(draw, [int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])])
        elif keyword == "circle":
            draw_circle(draw, [int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])])
        elif keyword == "fcircle":
            draw_filled_circle(draw, [int(parts[1]), int(parts[2]), int(parts[3])])

    image.save("view.png")

# Função para abrir a imagem no visualizador padrão do Windows
def abrir_imagem():
    file_path = "view.png"
    import os
    os.system(f"start {file_path}")

# Interface gráfica para inserir os comandos
root = tk.Tk()
root.title("Interpretador Gráfico")
root.configure(bg="blue")  # Define a cor de fundo da janela como azul
text = tk.Text(root,wrap="none", width=40, height=10, bg="blue", fg="white")
text.pack()
texto_pre_escrito = """line,100,100,200,200
rect,300,300,400,400
circle,500,500,100,100"""
text.insert("1.0", texto_pre_escrito)
button = tk.Button(root, text="Interpretar e Visualizar", command=lambda: interpretador_grafico(text.get("1.0", "end-1c").split("\n")))
button.pack()

open_button = tk.Button(root, text="Abrir Imagem", command=abrir_imagem)
open_button.pack()

root.mainloop()
