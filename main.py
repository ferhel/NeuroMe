from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from patientApp import PatientScreen

# Definimos el ScreenManager
class MyScreenManager(ScreenManager):
    pass

# Definimos las pantallas
class MainScreen(Screen):
    pass

class EstadisticaScreen(Screen):
    pass



class Main(App):
    def build(self):
        Window.tittle = "NeuroMe"  # Establecer el título de la ventana
        sm = MyScreenManager()
        sm.add_widget(MainScreen(name="main"))  # Pantalla principal
        sm.add_widget(PatientScreen(name="patient"))# Pantalla de historial
        sm.add_widget(EstadisticaScreen(name="estadistica_screen"))
        return sm


if __name__ == "__main__":
    Main().run()