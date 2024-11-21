from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Definimos el ScreenManager
class MyScreenManager(ScreenManager):
    pass

# Definimos las pantallas
class MainScreen(Screen):
    pass

class ContactosScreen(Screen):
    pass

class HistorialScreen(Screen):
    pass

class BitacoraScreen(Screen):
    pass

class Main(App):
    def build(self):
        Window.title = "NeuroMe"  # Establecer el título de la ventana
        sm = MyScreenManager()
        sm.add_widget(MainScreen(name="main"))  # Pantalla principal
        sm.add_widget(ContactosScreen(name="contactos_screen"))  # Pantalla de contactos
        sm.add_widget(HistorialScreen(name="historial_screen"))  # Pantalla de historial
        sm.add_widget(BitacoraScreen(name="bitacora_screen"))  # Pantalla de bitácora
        return sm

if __name__ == "__main__":
    Main().run()