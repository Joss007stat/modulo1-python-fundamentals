import streamlit as st

# MENU LATERAL
st.sidebar.title("Menú")

opcion = st.sidebar.selectbox(
    "Selecciona una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# HOME
if opcion == "Home":
    st.title("Aplicación en Streamlit")

# EJERCICIO 1
elif opcion == "Ejercicio 1":
    
    st.title("Ejercicio 1 – Verificador de Presupuesto")

    # 1️⃣ Solicitar datos
    presupuesto = st.number_input("Ingrese su presupuesto:", min_value=0.0, step=1.0)
    gasto = st.number_input("Ingrese su gasto:", min_value=0.0, step=1.0)

    # 2️⃣ Botón para evaluar
    if st.button("Evaluar presupuesto"):

        # 3️⃣ Evaluar condición
        diferencia = presupuesto - gasto

        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto ✅")
        else:
            st.warning("El presupuesto ha sido excedido ⚠️")

        # 4️⃣ Mostrar diferencia
        st.write(f"Diferencia: {diferencia}")


#EJERCICIO 2
elif opcion == "Ejercicio 2":

    st.title("Ejercicio 2 – Registro de Actividades Financieras")

    # 1️⃣ Crear lista en memoria si no existe
    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    # 2️⃣ Inputs
    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo de actividad", ["Operativa", "Marketing", "Inversión", "Otro"])
    presupuesto = st.number_input("Presupuesto asignado", min_value=0.0, step=1.0)
    gasto_real = st.number_input("Gasto real", min_value=0.0, step=1.0)

    # 3️⃣ Botón para agregar
    if st.button("Agregar actividad"):

        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }

        st.session_state.actividades.append(actividad)
        st.success("Actividad agregada correctamente")

    # 4️⃣ Mostrar lista
    if st.session_state.actividades:
        st.subheader("Lista de actividades registradas")
        st.dataframe(st.session_state.actividades)

        # 5️⃣ Evaluar cada actividad
        st.subheader("Estado de cada actividad")

        for act in st.session_state.actividades:

            diferencia = act["presupuesto"] - act["gasto_real"]

            if act["gasto_real"] <= act["presupuesto"]:
                estado = "Dentro del presupuesto ✅"
            else:
                estado = "Presupuesto excedido ⚠️"

            st.write(
                f"Actividad: {act['nombre']} | Estado: {estado} | Diferencia: {diferencia}"
            )


#EJERCICIO 3
elif opcion == "Ejercicio 3":

    st.title("Ejercicio 3 – Cálculo de Retorno Esperado")

    # Verificar que existan actividades
    if "actividades" not in st.session_state or not st.session_state.actividades:
        st.warning("Primero debe registrar actividades en el Ejercicio 2.")
    
    else:

        # 1️⃣ Definir función
        def calcular_retorno(actividad, tasa, meses):
            return actividad["presupuesto"] * tasa * meses

        # 2️⃣ Inputs
        tasa = st.slider("Seleccione la tasa de retorno (%)", 0.0, 1.0, 0.1)
        meses = st.number_input("Ingrese la cantidad de meses", min_value=1, step=1)

        # 3️⃣ Botón
        if st.button("Calcular retorno esperado"):

            # 4️⃣ Aplicar programación funcional
            retornos = list(
                map(
                    lambda act: {
                        "nombre": act["nombre"],
                        "retorno_esperado": calcular_retorno(act, tasa, meses)
                    },
                    st.session_state.actividades
                )
            )

            # 5️⃣ Mostrar resultados
            st.subheader("Resultados de Retorno Esperado")

            for r in retornos:
                st.write(
                    f"Actividad: {r['nombre']} | Retorno esperado: {r['retorno_esperado']}"
                )


#EJERCICIO 4
elif opcion == "Ejercicio 4":

    st.title("Ejercicio 4 – Programación Orientada a Objetos")

    # 1️⃣ Definir la clase
    class Actividad:

        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self):
            diferencia = self.presupuesto - self.gasto_real
            return (
                f"Actividad: {self.nombre} | "
                f"Tipo: {self.tipo} | "
                f"Presupuesto: {self.presupuesto} | "
                f"Gasto real: {self.gasto_real} | "
                f"Diferencia: {diferencia}"
            )

    # 2️⃣ Verificar que existan actividades
    if "actividades" not in st.session_state or not st.session_state.actividades:
        st.warning("Primero debe registrar actividades en el Ejercicio 2.")
    else:

        st.subheader("Evaluación de Actividades como Objetos")

        # 3️⃣ Convertir diccionarios en objetos
        objetos_actividades = [
            Actividad(
                act["nombre"],
                act["tipo"],
                act["presupuesto"],
                act["gasto_real"]
            )
            for act in st.session_state.actividades
        ]

        # 4️⃣ Mostrar información de cada objeto
        for obj in objetos_actividades:

            st.write(obj.mostrar_info())

            if obj.esta_en_presupuesto():
                st.success("Cumple el presupuesto ✅")
            else:
                st.warning("Presupuesto excedido ⚠️")