import tkinter as tk
from tkinter import messagebox

# Función para predecir la nota a partir del ID de usuario
def predecir_nota():
    user_id = entry_id.get()
    # Aquí se colocaría la lógica para predecir la nota
    predicted_score = 0.85  # Suponiendo una nota predicha de ejemplo
    messagebox.showinfo("Predicción de Nota", f"La nota predicha para el usuario {user_id} es: {predicted_score * 10:.1f}")

# Función para verificar si va bien para una nota deseada
def verificar_nota():
    user_id = entry_id.get()
    desired_score = float(entry_nota.get())
    # Aquí se colocaría la lógica para verificar si va bien o no
    outcome = "bien" if desired_score <= 0.8 else "necesita mejorar"  # Suponiendo una lógica de ejemplo
    messagebox.showinfo("Verificación de Nota", f"El usuario {user_id} va {outcome} para alcanzar la nota {desired_score * 10:.1f}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Sistema de Predicción de Notas")

# Creación de entradas para ID y Nota deseada
tk.Label(root, text="ID de Usuario:").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="ID de Aula:").grid(row=1, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Nota Deseada:").grid(row=2, column=0, padx=10, pady=5)
entry_nota = tk.Entry(root)
entry_nota.grid(row=2, column=1, padx=10, pady=5)

# Creación de los botones
btn_pred_nota = tk.Button(root, text="Predecir Nota", command=predecir_nota)
btn_pred_nota.grid(row=3, column=0, padx=10, pady=10)

btn_verif_nota = tk.Button(root, text="Verificar Nota Deseada", command=verificar_nota)
btn_verif_nota.grid(row=3, column=1, padx=10, pady=10)

btn_salir = tk.Button(root, text="Salir", command=root.quit)
btn_salir.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
