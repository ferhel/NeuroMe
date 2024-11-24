import csv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class PatientScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal
        main_layout = BoxLayout(orientation='vertical')

        # Crear un ScrollView
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 600))
        grid_layout = GridLayout(cols=1, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))  # Ajustar altura automáticamente

        # Ejemplo de datos de pacientes
        pacientes_data = self.cargar_pacientes_csv('data/data_limpia.csv')


        # Crear botones para cada paciente
        for paciente in pacientes_data:
            button = Button(text=f"ID: {paciente['PatientID']} - {paciente['Age']}, {paciente['Gender']}", size_hint_y=None,
                            height=40)
            button.bind(on_press=lambda x, p=paciente: self.mostrar_info(p))
            grid_layout.add_widget(button)

        scroll_view.add_widget(grid_layout)
        main_layout.add_widget(scroll_view)

        self.add_widget(main_layout)

    def cargar_pacientes_csv(self, file_path):
        pacientes = []
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pacientes.append(row)
        return pacientes

    def mostrar_info(self, paciente_data):

        print("Datos Completos:", paciente_data)


