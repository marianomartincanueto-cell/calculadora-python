import tkinter as tk
from tkinter import font

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora Simple")
        self.ventana.geometry("400x500")
        self.ventana.resizable(False, False)
        
        # Variable para almacenar la expresión
        self.expresion = ""
        
        # Crear la interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Panel para la pantalla
        pantalla_frame = tk.Frame(self.ventana, bg="#2c3e50")
        pantalla_frame.pack(pady=10, padx=10, fill="both", expand=False)
        
        # Pantalla de la calculadora
        self.pantalla = tk.Entry(
            pantalla_frame,
            font=("Arial", 24, "bold"),
            borderwidth=2,
            relief="solid",
            justify="right",
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        self.pantalla.pack(fill="both", ipady=20)
        
        # Panel de botones
        botones_frame = tk.Frame(self.ventana, bg="#34495e")
        botones_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Definir los botones
        botones = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "⌫"]
        ]
        
        # Colores
        color_numero = "#3498db"
        color_operador = "#e74c3c"
        color_igual = "#27ae60"
        color_limpiar = "#95a5a6"
        
        # Crear botones
        for fila in botones:
            fila_frame = tk.Frame(botones_frame, bg="#34495e")
            fila_frame.pack(fill="both", expand=True, pady=5)
            
            for boton_text in fila:
                # Determinar color según tipo de botón
                if boton_text == "=":
                    color = color_igual
                elif boton_text in ["C", "⌫"]:
                    color = color_limpiar
                elif boton_text in ["+", "-", "*", "/"]:
                    color = color_operador
                else:
                    color = color_numero
                
                boton = tk.Button(
                    fila_frame,
                    text=boton_text,
                    font=("Arial", 18, "bold"),
                    bg=color,
                    fg="white",
                    activebackground="#2c3e50",
                    activeforeground="white",
                    border=0,
                    cursor="hand2"
                )
                boton.pack(side="left", fill="both", expand=True, padx=5)
                
                # Asociar eventos
                if boton_text == "=":
                    boton.config(command=self.calcular)
                elif boton_text == "C":
                    boton.config(command=self.limpiar)
                elif boton_text == "⌫":
                    boton.config(command=self.borrar_ultimo)
                else:
                    boton.config(command=lambda x=boton_text: self.agregar(x))
    
    def agregar(self, valor):
        """Agrega un valor a la expresión"""
        self.expresion += str(valor)
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, self.expresion)
    
    def limpiar(self):
        """Limpia toda la expresión"""
        self.expresion = ""
        self.pantalla.delete(0, tk.END)
    
    def borrar_ultimo(self):
        """Borra el último carácter"""
        self.expresion = self.expresion[:-1]
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, self.expresion)
    
    def calcular(self):
        """Calcula el resultado de la expresión"""
        try:
            resultado = eval(self.expresion)
            self.expresion = str(resultado)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, self.expresion)
        except ZeroDivisionError:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error: División por 0")
            self.expresion = ""
        except:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")
            self.expresion = ""

def main():
    ventana = tk.Tk()
    app = Calculadora(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
