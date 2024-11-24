import sqlite3
import pandas as pd

# Conectar con la base de datos SQLite (se crea automáticamente si no existe)
def conectar_bd():
    return sqlite3.connect("clinica.db")

# Leer el CSV en un DataFrame y retornarlo
def leer_csv(ruta_csv):
    try:
        return pd.read_csv(ruta_csv)
    except FileNotFoundError:
        print(f"El archivo {ruta_csv} no se encontró.")
        return None

# Crear tabla en SQLite
def crear_tabla():
    db = conectar_bd()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            PatientID INTEGER PRIMARY KEY,
            Age INTEGER,
            Gender TEXT,
            Ethnicity TEXT,
            EducationLevel TEXT,
            Smoking TEXT,
            AlcoholConsumption TEXT,
            PhysicalActivity TEXT,
            DietQuality TEXT,
            SleepQuality TEXT,
            FamilyHistoryAlzheimers TEXT,
            CardiovascularDisease TEXT,
            Diabetes TEXT,
            Depression TEXT,
            HeadInjury TEXT,
            Hypertension TEXT,
            MMSE INTEGER,
            FunctionalAssessment TEXT,
            MemoryComplaints TEXT,
            BehavioralProblems TEXT,
            ADL TEXT,
            Confusion TEXT,
            Disorientation TEXT,
            PersonalityChanges TEXT,
            DifficultyCompletingTasks TEXT,
            Forgetfulness TEXT,
            Diagnosis TEXT,
            DoctorInCharge TEXT
        );
    """)

    db.commit()
    cursor.close()
    db.close()

# Insertar datos desde el CSV a la tabla SQLite
def insertar_datos_csv(ruta_csv):
    df = leer_csv(ruta_csv)
    db = conectar_bd()
    cursor = db.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR REPLACE INTO pacientes (
                PatientID, Age, Gender, Ethnicity, EducationLevel, Smoking, AlcoholConsumption, PhysicalActivity,
                DietQuality, SleepQuality, FamilyHistoryAlzheimers, CardiovascularDisease, Diabetes, Depression, HeadInjury,
                Hypertension, MMSE, FunctionalAssessment, MemoryComplaints, BehavioralProblems, ADL, Confusion, Disorientation,
                PersonalityChanges, DifficultyCompletingTasks, Forgetfulness, Diagnosis, DoctorInCharge
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(row))
    
    db.commit()
    cursor.close()
    db.close()

# Leer datos desde SQLite
def leer_datos():
    db = conectar_bd()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pacientes")
    resultados = cursor.fetchall()
    cursor.close()
    db.close()
    return resultados

# Buscar un paciente por PatientID
def buscar_paciente_por_id(patient_id):
    try:
        db = conectar_bd()
        cursor = db.cursor()

        # Verifica si la consulta SQL se está ejecutando correctamente
        print(f"Buscando paciente con PatientID = {patient_id}...")

        cursor.execute("SELECT * FROM pacientes WHERE PatientID = ?", (patient_id,))
        paciente = cursor.fetchone()

        # Si paciente es None, significa que no se encontró ningún paciente
        if paciente:
            print(f"Paciente encontrado: {paciente}")
        else:
            print("No se encontró ningún paciente con ese ID.")

        cursor.close()
        db.close()

        return paciente
    except Exception as e:
        print(f"Error al buscar paciente: {e}")
        return None

# Actualizar un campo específico de un paciente en SQLite
def actualizar_paciente(PatientID, columna, valor):
    db = conectar_bd()
    cursor = db.cursor() 
    cursor.execute(f"UPDATE pacientes SET {columna} = ? WHERE PatientID = ?", (valor, PatientID))
    db.commit()
    cursor.close()
    db.close()
    
# Insertar un nuevo paciente
def insertar_paciente(nuevo_paciente):
    db = conectar_bd()
    cursor = db.cursor()
    
    cursor.execute("""
        INSERT INTO pacientes (
            PatientID, Age, Gender, Ethnicity, EducationLevel, Smoking, AlcoholConsumption, PhysicalActivity,
            DietQuality, SleepQuality, FamilyHistoryAlzheimers, CardiovascularDisease, Diabetes, Depression, HeadInjury,
            Hypertension, MMSE, FunctionalAssessment, MemoryComplaints, BehavioralProblems, ADL, Confusion, Disorientation,
            PersonalityChanges, DifficultyCompletingTasks, Forgetfulness, Diagnosis, DoctorInCharge
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(nuevo_paciente))
    
    db.commit()
    cursor.close()
    db.close()

# Eliminar un paciente por PatientID
def eliminar_paciente(PatientID):
    db = conectar_bd()
    cursor = db.cursor()
    cursor.execute("DELETE FROM pacientes WHERE PatientID = ?", (PatientID,))
    db.commit()
    cursor.close()
    db.close()

# Opciones para editar o añadir el género en el menú interactivo.
def seleccionar_genero():
    print("Selecciona el género:")
    print("0. Masculino")
    print("1. Femenino")
    
    while True:
        try:
            genero = int(input("Escribe el número correspondiente (0 o 1): "))
            if genero in [0, 1]:
                return genero
            else:
                print("Opción no válida. Por favor, ingresa 0 para Masculino o 1 para Femenino.")
        except ValueError:
            print("Por favor, ingresa un número entero válido (0 o 1).")

# Opciones para editar o añadir la etnicidad en el menú interactivo.
def seleccionar_etnicidad():
    print("\nSelecciona la etnicidad:")
    print("0. Caucásico")
    print("1. Afroamericano")
    print("2. Asiático")
    print("3. Otro")
    
    while True:
        try:
            etnicidad = int(input("Escribe el número correspondiente (0-3): "))
            if etnicidad in [0, 1, 2, 3]:
                return etnicidad
            else:
                print("Opción no válida. Por favor, ingresa un número entre 0 y 3.")
        except ValueError:
            print("Por favor, ingresa un número entero válido entre 0 y 3.")

# Opciones para editar o añadir el nivel educativo en el menú interactivo.
def seleccionar_nivel_educativo():
    print("\nSelecciona el nivel educativo:")
    print("0. Ninguno")
    print("1. Secundaria")
    print("2. Licenciatura")
    print("3. Posgrado")
    
    while True:
        try:
            educacion = int(input("Escribe el número correspondiente (0-3): "))
            if educacion in [0, 1, 2, 3]:
                return educacion
            else:
                print("Opción no válida. Por favor, ingresa un número entre 0 y 3.")
        except ValueError:
            print("Por favor, ingresa un número entero válido entre 0 y 3.")
#Actualizar datos unitarios para menú interactivo.
def actualizar_paciente_opcion4(patient_id):
    # Mostrar las columnas disponibles para actualizar
    columnas = [
        "Age", "Gender", "Ethnicity", "EducationLevel", "Smoking", "AlcoholConsumption", "PhysicalActivity",
        "DietQuality", "SleepQuality", "FamilyHistoryAlzheimers", "CardiovascularDisease", "Diabetes", "Depression", 
        "HeadInjury", "Hypertension", "MMSE", "FunctionalAssessment", "MemoryComplaints", "BehavioralProblems", 
        "ADL", "Confusion", "Disorientation", "PersonalityChanges", "DifficultyCompletingTasks", "Forgetfulness", 
        "Diagnosis", "DoctorInCharge"
    ]
    
    # Imprimir las columnas disponibles para actualizar con su número
    print("\nSelecciona la columna que deseas actualizar:")
    for index, columna in enumerate(columnas, 1):  # Enumerar las columnas
        print(f"{index}. {columna}")

    while True:
        try:
            # Solicitar al usuario que seleccione un número correspondiente a la columna
            opcion_columna = int(input("Introduce el número de la columna a actualizar (1-26): "))
            if 1 <= opcion_columna <= len(columnas):  # Validar que la opción esté dentro del rango
                columna_seleccionada = columnas[opcion_columna - 1]  # Ajuste para índices de lista
                break
            else:
                print("Opción no válida. Elige un número entre 1 y 26.")
        except ValueError:
            print("Por favor, ingresa un número entero válido entre 1 y 26.")

    # Solicitar el nuevo valor para la columna seleccionada
    nuevo_valor = input(f"Introduce el nuevo valor para la columna '{columna_seleccionada}': ")

    # Actualizar el paciente en la base de datos
    actualizar_paciente(patient_id, columna_seleccionada, nuevo_valor)
    print(f"Paciente actualizado correctamente. La columna '{columna_seleccionada}' fue modificada.")



        

# Llamada a la opción 4 del menú para actualizar paciente
# Menú interactivo
def menu():
    while True:
        print("\n*** Menú de Opciones ***")
        print("1. Ver todos los pacientes")
        print("2. Buscar paciente por ID")
        print("3. Insertar nuevo paciente")
        print("4. Actualizar paciente")
        print("5. Eliminar paciente")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pacientes = leer_datos()
            if pacientes:
                for paciente in pacientes:
                    print(paciente)
            else:
                print("No hay pacientes en la base de datos.")

        elif opcion == "2":
            patient_id = int(input("Introduce el ID del paciente a buscar: "))
            paciente = buscar_paciente_por_id(patient_id)
            

        elif opcion == "3":
            print("Introduce los datos del nuevo paciente.")
            patient_id = int(input("ID del paciente: "))
            age = int(input("Edad: "))
            gender = seleccionar_genero()
            ethnicity = seleccionar_etnicidad()
            education_level = seleccionar_nivel_educativo()
            smoking = input("Fuma (Sí/No): ")
            alcohol_consumption = input("Consumo de alcohol (Sí/No): ")
            physical_activity = input("Actividad física (Sí/No): ")
            diet_quality = input("Calidad de la dieta: ")
            sleep_quality = input("Calidad del sueño: ")
            family_history_alzheimers = input("Antecedentes familiares de Alzheimer (Sí/No): ")
            cardiovascular_disease = input("Enfermedad cardiovascular (Sí/No): ")
            diabetes = input("Diabetes (Sí/No): ")
            depression = input("Depresión (Sí/No): ")
            head_injury = input("Lesión en la cabeza (Sí/No): ")
            hypertension = input("Hipertensión (Sí/No): ")
            mmse = int(input("MMSE: "))
            functional_assessment = input("Evaluación funcional: ")
            memory_complaints = input("Quejas de memoria: ")
            behavioral_problems = input("Problemas de comportamiento: ")
            adl = input("Actividades de la vida diaria: ")
            confusion = input("Confusión (Sí/No): ")
            disorientation = input("Desorientación (Sí/No): ")
            personality_changes = input("Cambios de personalidad (Sí/No): ")
            difficulty_completing_tasks = input("Dificultad para realizar tareas (Sí/No): ")
            forgetfulness = input("Olvido (Sí/No): ")
            diagnosis = input("Diagnóstico: ")
            doctor_in_charge = input("Médico a cargo: ")

            nuevo_paciente = [patient_id, age, gender, ethnicity, education_level, smoking, alcohol_consumption, physical_activity,
                             diet_quality, sleep_quality, family_history_alzheimers, cardiovascular_disease, diabetes, depression,
                             head_injury, hypertension, mmse, functional_assessment, memory_complaints, behavioral_problems, adl,
                             confusion, disorientation, personality_changes, difficulty_completing_tasks, forgetfulness, diagnosis,
                             doctor_in_charge]
            
            insertar_paciente(nuevo_paciente)
            print("Paciente insertado correctamente.")

        elif opcion == "4":
            patient_id = int(input("Ingrese ID del paciente:"))
            actualizar_paciente_opcion4(patient_id)
            
            

        elif opcion == "5":
            patient_id = int(input("Introduce el ID del paciente a eliminar: "))
            eliminar_paciente(patient_id)
            print("Paciente eliminado correctamente.")

        elif opcion == "6":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 6.")

# Ejecución del menú
if __name__ == "__main__":
    crear_tabla()
    menu()
