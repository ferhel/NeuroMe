import sqlite3
import pandas as pd

# Conectar con la base de datos SQLite (se crea automáticamente si no existe)
def conectar_bd():
    return sqlite3.connect("clinica.db")

# Leer el CSV en un DataFrame y retornarlo
def leer_csv(ruta_csv):
    
    try: 
        return pd.read_csv(ruta_csv)
    except: 
        FileNotFoundError
        print(f"El archivo {ruta_archivo} no se encontró.")
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
            SystolicBP INTEGER,
            DiastolicBP INTEGER,
            CholesterolTotal INTEGER,
            CholesterolLDL INTEGER,
            CholesterolHDL INTEGER,
            CholesterolTriglycerides INTEGER,
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
                Hypertension, SystolicBP, DiastolicBP, CholesterolTotal, CholesterolLDL, CholesterolHDL, CholesterolTriglycerides,
                MMSE, FunctionalAssessment, MemoryComplaints, BehavioralProblems, ADL, Confusion, Disorientation,
                PersonalityChanges, DifficultyCompletingTasks, Forgetfulness, Diagnosis, DoctorInCharge
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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

# Actualizar un paciente en SQLite
def actualizar_paciente(PatientID, nuevo_dato):
    db = conectar_bd()
    cursor = db.cursor()

    for columna, valor in nuevo_dato.items():
        cursor.execute(f"UPDATE pacientes SET {columna} = ? WHERE PatientID = ?", (valor, PatientID))
    
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

# Ejemplo de uso
if __name__ == "__main__":
    # Crear la tabla (si no existe)
    crear_tabla()

    # Insertar datos del CSV a la base de datos SQLite
    ruta_archivo = "data_limpia.csv"  # Ruta al archivo CSV
    insertar_datos_csv(ruta_archivo)
    
    # Leer los datos desde la base de datos
    print("Datos de pacientes:")
    pacientes = leer_datos()
    for paciente in pacientes:
        print(paciente)

    # Actualizar un paciente (Ejemplo: cambiar el diagnóstico)
    print("\nActualizando el diagnóstico del paciente con PatientID = 1...")
    actualizar_paciente(1, {"Diagnosis": "Mild Dementia"})

    # Leer los datos después de la actualización
    print("\nDatos después de la actualización:")
    pacientes_actualizados = leer_datos()
    for paciente in pacientes_actualizados:
        print(paciente)

    # Eliminar un paciente
    print("\nEliminando el paciente con PatientID = 2...")
    eliminar_paciente(2)

    # Leer los datos después de la eliminación
    print("\nDatos después de la eliminación:")
    pacientes_final = leer_datos()
    for paciente in pacientes_final:
        print(paciente)
