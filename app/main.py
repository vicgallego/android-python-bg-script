from kivy.app import App
from kivy.uix.label import Label
import threading
import time

# Función que corre en segundo plano
def mi_script_segundo_plano():
    while True:
        print("Script corriendo en segundo plano...")
        time.sleep(2)  # Espera 2 segundos antes de repetir

class MyApp(App):
    def build(self):
        # Crear un hilo para el script
        hilo = threading.Thread(target=mi_script_segundo_plano, daemon=True)
        hilo.start()

        # Interfaz principal de la app
        return Label(text="App corriendo 🚀")

if __name__ == "__main__":
    MyApp().run()