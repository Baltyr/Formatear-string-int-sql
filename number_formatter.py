import tkinter as tk
from tkinter import ttk
import itertools
import math
import time

def format_numbers():
    numbers = input_text.get("1.0", "end-1c").split()
    format_type = format_type_var.get()

    if format_type == "String":
        formatted_numbers = ', '.join(f"'{num}'" for num in numbers)
    else:
        formatted_numbers = ', '.join(num for num in numbers if num.isdigit())

    output_text.delete("1.0", "end")
    output_text.insert("1.0", formatted_numbers)

    total_numbers_var.set(f"Total numbers formatted: {len(numbers)}")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", "end-1c"))
    root.update()  # Necessary to update the clipboard

def create_rounded_text(parent, **options):
    frame_bg = options.pop('bg', '#0d1117')
    radius = options.pop('radius', 20)
    border_color = options.pop('border_color', '#238636')
    border_width = options.pop('border_width', 2)
    
    frame = tk.Frame(parent, bg=frame_bg)
    canvas = tk.Canvas(frame, bg=frame_bg, highlightthickness=0, width=options['width'] + 2 * radius, height=options['height'] + 2 * radius)
    text = tk.Text(frame, **options, relief=tk.FLAT, bg="#161b22", fg="white", insertbackground="white", highlightthickness=0, wrap=tk.WORD)

    def draw_rounded_rectangle(canvas, x1, y1, x2, y2, r=25, **kwargs):
        points = [x1+r, y1,
                  x1+r, y1,
                  x2-r, y1,
                  x2-r, y1,
                  x2, y1,
                  x2, y1+r,
                  x2, y1+r,
                  x2, y2-r,
                  x2, y2-r,
                  x2, y2,
                  x2-r, y2,
                  x2-r, y2,
                  x1+r, y2,
                  x1+r, y2,
                  x1, y2,
                  x1, y2-r,
                  x1, y2-r,
                  x1, y1+r,
                  x1, y1+r,
                  x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    # Create rounded rectangle
    draw_rounded_rectangle(canvas, radius, radius, options['width'] + radius, options['height'] + radius, radius, outline=border_color, width=border_width)
    canvas.pack(expand=True, fill=tk.BOTH)
    text.place(x=radius, y=radius, width=options['width'], height=options['height'])

    return frame, text

def create_modern_button(parent, text, command, **options):
    button_color = options.pop('button_color', '#238636')
    text_color = options.pop('text_color', 'white')
    hover_color = options.pop('hover_color', '#2ea043')

    button = tk.Button(parent, text=text, command=command, relief=tk.FLAT, bg=button_color, fg=text_color, font=("Helvetica", 12, "bold"),
                       activebackground=button_color, activeforeground=text_color, cursor="hand2", bd=0, padx=10, pady=5)

    def on_enter(e):
        button['background'] = hover_color

    def on_leave(e):
        button['background'] = button_color

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button

# Donut animation adapted for tkinter
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
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text=''.join(output), font=("Consolas", 8), fill="#1f6feb", anchor=tk.CENTER)
        root.update()
        A += 0.04
        B += 0.02
        time.sleep(0.03)

# Configurar la ventana principal
root = tk.Tk()
root.title("Number Formatter")
root.geometry("700x700")
root.resizable(False, False)
root.configure(bg="#0d1117")

# Estilos
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 12), background="#0d1117", foreground="white")
style.configure("TButton", font=("Helvetica", 12), background="#238636", foreground="white", borderwidth=0, padding=10)
style.configure("TEntry", font=("Helvetica", 12), padding=5)
style.configure("TCombobox", font=("Helvetica", 12), padding=5, relief=tk.FLAT, background="#161b22", foreground="white", fieldbackground="#161b22")
style.map("TCombobox", fieldbackground=[('readonly', '#161b22')], background=[('readonly', '#161b22')], foreground=[('readonly', 'white')])
style.configure("TFrame", background="#0d1117")
style.configure("TText", background="#161b22", foreground="white", font=("Helvetica", 12))

# Configuración de variables
format_type_var = tk.StringVar(value="String")
total_numbers_var = tk.StringVar(value="Total numbers formatted: 0")

# Crear y organizar widgets
main_frame = ttk.Frame(root, padding="10", style="TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)

input_frame = ttk.Frame(main_frame, padding="5", style="TFrame")
input_frame.pack(fill=tk.BOTH, expand=True)

output_frame = ttk.Frame(main_frame, padding="5", style="TFrame")
output_frame.pack(fill=tk.BOTH, expand=True)

button_frame = ttk.Frame(main_frame, padding="5", style="TFrame")
button_frame.pack(fill=tk.BOTH, expand=True)

input_label_frame = ttk.Frame(input_frame, style="TFrame")
input_label_frame.pack(fill=tk.X, padx=5, pady=5)

ttk.Label(input_label_frame, text="Ingresar valores (separados por espacio):", style="TLabel").pack(side=tk.LEFT, anchor=tk.W)
format_options = ttk.Combobox(input_label_frame, textvariable=format_type_var, values=["String", "Int"], state="readonly", style="TCombobox")
format_options.pack(side=tk.LEFT, anchor=tk.W, padx=5)

input_frame_inner, input_text = create_rounded_text(input_frame, width=500, height=100, border_color="#238636", border_width=2)
input_frame_inner.pack(fill=tk.BOTH, padx=5, pady=20)  # Aumentar el padding para más espacio

# Fondo de animación
animation_frame = ttk.Frame(main_frame, padding="5", style="TFrame")
animation_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(animation_frame, bg="#0d1117", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

ttk.Label(output_frame, text="Output:", style="TLabel").pack(anchor=tk.W, pady=5)
output_frame_inner, output_text = create_rounded_text(output_frame, width=500, height=100, border_color="#238636", border_width=2)
output_frame_inner.pack(fill=tk.BOTH, padx=5, pady=20)  # Aumentar el padding para más espacio

buttons_container = ttk.Frame(button_frame, style="TFrame")
buttons_container.pack()

formatear_button = create_modern_button(buttons_container, text="Formatear", command=format_numbers, button_color="#238636", hover_color="#2ea043")
formatear_button.grid(row=0, column=0, padx=10)

copiar_button = create_modern_button(buttons_container, text="Copiar", command=copy_to_clipboard, button_color="#238636", hover_color="#2ea043")
copiar_button.grid(row=0, column=1, padx=10)

ttk.Label(button_frame, textvariable=total_numbers_var, style="TLabel").pack(pady=10)

# Iniciar la animación de fondo
import threading
animation_thread = threading.Thread(target=donut_animation, daemon=True)
animation_thread.start()

root.mainloop()
