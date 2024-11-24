import sqlite3
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
        pacientes_data = self.cargar_pacientes_sqlite3()


        # Crear botones para cada paciente
        for paciente in pacientes_data[:50]:  #Se determina un máximo de 50 pacientes visualizados
            button = Button(text=f"ID: {paciente[0]} - {paciente[1]} - {paciente[2]}", size_hint_y=None,
                            height=40)
            button.bind(on_press=lambda x, p=paciente: self.mostrar_info(p))
            grid_layout.add_widget(button)

        scroll_view.add_widget(grid_layout)
        main_layout.add_widget(scroll_view)

        self.add_widget(main_layout)

    def cargar_pacientes_sqlite3(self):
        pacientes = []
        # Conectar a la base de datos SQLite3
        connection = sqlite3.connect("clinica.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        # Ejecutar la consulta para obtener todos los datos de los pacientes
        cursor.execute("SELECT * FROM pacientes")
        rows = cursor.fetchall()

        # Agregar los datos a la lista de pacientes
        for row in rows:
            pacientes.append(row)
        # Cerrar la conexión
        connection.close()
        return pacientes

    def mostrar_info(self, pacientes_data):

        # Imprimir toda la información del paciente en la terminal
        print("Datos Completos del Paciente:")
        for column in pacientes_data.keys():  # Usar keys() para obtener los nombres de las columnas
            print(f"{column}: {pacientes_data[column]}")  # Acceder a los valores de las columnas

