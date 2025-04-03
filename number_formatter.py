import tkinter as tk
from tkinter import ttk, filedialog
import math
import time
import threading

# === Logica de Formato ===
def format_numbers():
    numbers = input_text.get("1.0", "end-1c").split()
    format_type = format_type_var.get()

    if format_type == "String":
        formatted_numbers = ', '.join(f"'{num}'" for num in numbers)
    else:
        formatted_numbers = ', '.join(num for num in numbers if num.isdigit())

    output_text.delete("1.0", "end")
    output_text.insert("1.0", formatted_numbers)

    total_numbers_var.set(f"Total formateados: {len(numbers)}")

# === Copiar ===
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", "end-1c"))
    root.update()

# === Guardar en archivo ===
def export_output():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(output_text.get("1.0", "end-1c"))

# === Toggle Modo Claro/Oscuro ===
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg = "#0d1117" if dark_mode else "#ffffff"
    fg = "white" if dark_mode else "black"
    box_bg = "#161b22" if dark_mode else "#e0e0e0"
    text_bg = "#0d1117" if dark_mode else "#ffffff"
    text_fg = "white" if dark_mode else "#000000"
    insert_color = "white" if dark_mode else "black"
    sub_fg = "#c9d1d9" if dark_mode else "#444444"
    info_fg = "#8b949e" if dark_mode else "#666666"

    root.configure(bg=bg)
    main_frame.configure(bg=bg)
    title.configure(bg=bg, fg=fg)
    options_frame.configure(bg=bg)
    label.configure(bg=bg, fg=fg)
    input_label.configure(bg=bg, fg=sub_fg)
    output_label.configure(bg=bg, fg=sub_fg)
    info_label.configure(bg=bg, fg=info_fg)
    button_frame.configure(bg=bg)
    canvas.configure(bg=bg)
    tag_label.configure(bg=bg, fg="#58a6ff" if dark_mode else "#1f6feb")

    input_text.configure(bg=text_bg, fg=text_fg, insertbackground=insert_color)
    input_text.master.configure(bg=box_bg)
    output_text.configure(bg=text_bg, fg=text_fg, insertbackground=insert_color)
    output_text.master.configure(bg=box_bg)

# === Estilo Moderno de Botón ===
def create_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command,
                       bg="#1f6feb", fg="white",
                       font=("Inter", 12, "bold"), bd=0,
                       activebackground="#388bfd",
                       activeforeground="white", padx=20, pady=10,
                       cursor="hand2")
    button.pack(side=tk.LEFT, padx=10)
    return button

# === Estilo Caja ===
def create_text_box(parent):
    frame = tk.Frame(parent, bg="#161b22", bd=2, relief="ridge")
    text = tk.Text(frame, wrap=tk.WORD, font=("Inter", 11), fg="white", bg="#0d1117",
                   insertbackground="white", bd=0, height=6)
    text.pack(expand=True, fill=tk.BOTH, padx=8, pady=8)
    frame.pack(fill=tk.X, pady=10)
    return text

# === Animación Donut (no modificar) ===
def donut_animation():
    A = 0
    B = 0
    while True:
        output = []
        z = [0] * 1760
        b = [' '] * 1760
        for j in range(0, 628, 7):
            for i in range(0, 628, 2):
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(A)
                f = math.sin(j)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e
                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = int(x + 80 * y)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                if 1760 > o > 0 and D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
        output.append('\x1b[H')
        for k in range(1760):
            output.append(b[k] if k % 80 else '\n')
        canvas.delete("all")
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                           text=''.join(output), font=("Consolas", 8), fill="#1f6feb", anchor=tk.CENTER)
        root.update()
        A += 0.04
        B += 0.02
        time.sleep(0.03)

# === Animación Título con Tag ===
def animate_title():
    text = (
        "    ___   __     __  __  ____   __  "
        "\n   / __) /  \  _(  )(  )(  _ \ / _\ "
        "\n  ( (_ \\(  0 )/ \\) \\ )(  )   //    \ "
        "\n   \\___/ \\__/ \\____/(__)(__\\_)\\_/\\_/"
    )
    displayed = ""
    for char in text:
        displayed += char
        tag_label.config(text=displayed)
        root.update()
        time.sleep(0.005)

# === UI Principal ===
root = tk.Tk()
root.title("Formateador de Números")
root.geometry("700x850")
root.configure(bg="#0d1117")
root.resizable(False, False)

# Variables
dark_mode = True
format_type_var = tk.StringVar(value="String")
total_numbers_var = tk.StringVar(value="Total formateados: 0")

# === Layout Principal ===
main_frame = tk.Frame(root, bg="#0d1117")
main_frame.pack(padx=30, pady=30, fill=tk.BOTH, expand=True)

# === Tag animado ===
tag_label = tk.Label(main_frame, font=("Courier", 10, "bold"), bg="#0d1117", fg="#58a6ff", justify="left")
tag_label.pack(pady=(0, 20))
threading.Thread(target=animate_title, daemon=True).start()

# === Opciones ===
options_frame = tk.Frame(main_frame, bg="#0d1117")
options_frame.pack(fill=tk.X)

label = tk.Label(options_frame, text="Tipo de Formato:", font=("Inter", 12), bg="#0d1117", fg="white")
label.pack(side=tk.LEFT)

combo = ttk.Combobox(options_frame, textvariable=format_type_var, state="readonly",
                     values=["String", "Int"], font=("Inter", 11), width=10)
combo.pack(side=tk.LEFT, padx=10)

# === Input ===
input_label = tk.Label(main_frame, text="Ingresar valores separados por espacios:", font=("Inter", 11), bg="#0d1117", fg="#c9d1d9")
input_label.pack(anchor=tk.W)
input_text = create_text_box(main_frame)

# === Output ===
output_label = tk.Label(main_frame, text="Resultado:", font=("Inter", 11), bg="#0d1117", fg="#c9d1d9")
output_label.pack(anchor=tk.W)
output_text = create_text_box(main_frame)

# === Botones ===
button_frame = tk.Frame(main_frame, bg="#0d1117")
button_frame.pack(pady=10)

create_button(button_frame, "Formatear", format_numbers)
create_button(button_frame, "Copiar", copy_to_clipboard)
create_button(button_frame, "Exportar", export_output)
create_button(button_frame, "🌙/☀️ Tema", toggle_theme)

# === Conteo ===
info_label = tk.Label(main_frame, textvariable=total_numbers_var, font=("Inter", 10), bg="#0d1117", fg="#8b949e")
info_label.pack(pady=10)

# === Animación Donut ===
canvas = tk.Canvas(main_frame, bg="#0d1117", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True, pady=20)
threading.Thread(target=donut_animation, daemon=True).start()

# === Run ===
root.mainloop()