
# 🎨 Formateador Estético de Números

Un elegante formateador de números desarrollado con **Tkinter** que permite transformar listas de valores rápidamente en formatos `String` o `Int`, con funcionalidades adicionales como:

- Copiar al portapapeles
- Exportar a archivo `.txt` o `.csv`
- Modo **oscuro / claro**
- Animación de fondo con un **donut ASCII 3D en movimiento**
- Tag personalizado animado en la interfaz

---

## 🧠 Funcionalidad

El objetivo de esta app es facilitar el formateo de números pegados desde archivos, sistemas o listas copiados, dándoles un formato limpio y reutilizable en código.

Ejemplo de entrada:
```
1 2 3 4
```

Salida en formato **String**:
```python
'1', '2', '3', '4'
```

Salida en formato **Int**:
```python
1, 2, 3, 4
```

---

## 🖥 Interfaz

- Basado en `Tkinter`, con una estética moderna y minimalista.
- Modo claro y oscuro dinámico mediante botón 🌙/☀️
- Componentes redondeados, botones estilizados e inputs centrados.
- Canvas con animación de fondo tipo **retro terminal**.

---

## 📦 Instalación

1. Clona el repositorio o descarga el código.
2. Ejecuta el script directamente con Python:

```bash
python number_formatter.py
```

3. Si deseas compilarlo a `.exe`:

```bash
# Instala pyinstaller si no lo tienes
pip install pyinstaller

# Compila con icono personalizado
pyinstaller --noconfirm --onefile --windowed --icon=icono.ico --name=FormateadorNumeros number_formatter.py
```

---

## 🧩 Requisitos

- Python 3.10 o superior
- Tkinter (incluido en instalaciones estándar de Python)

---

## 🧬 Autor y Firma

Este proyecto fue creado con atención al detalle y pasión por la estética de interfaces en Python.

```
     ___   __     __  __  ____   __  
   / __) /  \  _(  )(  )(  _ \ / _\ 
  ( (_ \(  0 )/ \) \ )(  )   //    \ 
   \___/ \__/ \____/(__)(__\_)\_/\_/
```

**🛠 Creado por:** [Tu nombre o alias aquí]

---

## 📜 Licencia

Este proyecto puede utilizarse, modificarse y distribuirse libremente con fines educativos y personales. ¡Agradecimientos son bienvenidos!
