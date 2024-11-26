import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from crud_1 import menu



class PatientScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal con FloatLayout
        main_layout = FloatLayout()

        # Botón para abrir el menú en la terminal (en la parte superior)
        btn_menu = Button(text='Abrir Menú en Terminal', size_hint=(1, 0.1),
                          pos_hint={'x': 0, 'y': 0.9}, background_color=(0.3, 0.3, 0.3, 1)) # Posicionar en la parte superior
        btn_menu.bind(on_press=self.abrir_menu_terminal)
        main_layout.add_widget(btn_menu)

        # Botón para volver a la página principal
        btn_back = Button(text='Volver a la Página Principal', size_hint=(1, 0.1),
                          pos_hint={'x': 0, 'y': 0.8},
                          background_color=(0.3, 0.3, 0.3, 1))
        btn_back.bind(on_press=self.volver_a_pagina_principal)
        main_layout.add_widget(btn_back)

        # Crear un ScrollView
        scroll_view = ScrollView(size_hint=(1, 0.8), pos_hint={'x': 0, 'y': 0})  # Ocupa el 80% de la altura
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

        connection.close()
        return pacientes

    def mostrar_info(self, pacientes_data):
        # Imprimir toda la información del paciente en la terminal
        print("Datos Completos del Paciente:")
        for column in pacientes_data.keys():  # Usar keys() para obtener los nombres de las columnas
            print(f"{column}: {pacientes_data[column]}")  # Acceder a los valores de las columnas

    def abrir_menu_terminal(self, instance):
        menu()

    def volver_a_pagina_principal(self, instance):
        self.manager.current = 'main'