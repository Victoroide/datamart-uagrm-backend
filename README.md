# Backend - DataMart Académico UAGRM

Este proyecto proporciona una API que permite la consulta de diferentes métricas académicas (inscritos, rendimiento, promedios, nuevos inscritos, egresados, deserción y PPAC) basadas en los datos del DataMart Académico de la UAGRM. El backend está construido usando Flask y expone diversos endpoints para consumir los datos filtrados por facultad, carrera y periodo académico.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)
- Flask
- Pandas
- Flask-CORS

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Victoroide/datamart-uagrm-backend.git
   cd datamart-uagrm-backend
   ```

2. **Crear un entorno virtual (recomendado):**

   Si prefieres aislar los paquetes del proyecto, crea un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias:**

   Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

4. **Colocar el archivo de datos:**

   Debes asegurarte de tener el archivo de datos `DataMartAcademicoUAGRM.xlsx` en la carpeta `data/` en la raíz del proyecto. El archivo de Excel debe contener las columnas adecuadas mencionadas en el código (como `LOCALIDAD`, `%APRO`, `PPS`, etc.).

5. **Iniciar la aplicación Flask:**

   Para ejecutar el servidor en modo desarrollo, puedes usar el siguiente comando:

   ```bash
   flask run
   ```

   Esto iniciará el servidor en `http://localhost:5000`.

## Endpoints Disponibles

A continuación, una lista de los endpoints disponibles y su uso:

### 1. **/facultades**

   - **Método:** `GET`
   - **Descripción:** Obtiene la lista de todas las facultades disponibles.

### 2. **/carreras**

   - **Método:** `GET`
   - **Descripción:** Obtiene la lista de todas las carreras disponibles.

### 3. **/periodos**

   - **Método:** `GET`
   - **Descripción:** Obtiene la lista de todos los periodos académicos disponibles.

### 4. **/inscritos**

   - **Método:** `GET`
   - **Parámetros:** `facultad`, `carrera`, `periodo`
   - **Descripción:** Obtiene el número de inscritos por localidad.

### 5. **/rendimiento**

   - **Método:** `GET`
   - **Parámetros:** `facultad`, `carrera`, `periodo`
   - **Descripción:** Obtiene el porcentaje de aprobados por localidad.

### 6. **/promedios**

   - **Método:** `GET`
   - **Parámetros:** `facultad`, `carrera`, `periodo`
   - **Descripción:** Obtiene el promedio ponderado por semestre (PPS) por localidad.

### 7. **/nuevos_inscritos**

   - **Método:** `GET`
   - **Parámetros:** `facultad`, `carrera`, `periodo`
   - **Descripción:** Obtiene el número de nuevos inscritos por localidad.

### 8. **/egresados**

   - **Método:** `GET`
   - **Parámetros:** `facultad`, `carrera`, `periodo`
   - **Descripción:** Obtiene el número de egresados por localidad.

### 9. **/desercion**

   - **Método:** `GET`
   - **Parámetros:** `facultad`, `carrera`, `periodo`
   - **Descripción:** Obtiene el porcentaje de deserción por localidad.

### 10. **/ppac**

   - **Método:** `GET`
   - **Parámetros:** `facultad`, `carrera`, `periodo`
   - **Descripción:** Obtiene el promedio ponderado acumulado (PPAC) por localidad.

## Notas adicionales

- El backend utiliza CORS para permitir la interacción con el frontend.
- Asegúrate de que el archivo de datos `DataMartAcademicoUAGRM.xlsx` esté correctamente formateado para evitar errores.
