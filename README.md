# **Examen Practicante - Analítica**
Este proyecto consiste en procesar y analizar datos de un Contact Center que gestiona interacciones en redes sociales, para evaluar el cumplimiento de metas de casos atendidos diariamente. El proyecto incluye varias etapas de transformación de datos utilizando Python y SQL, y la creación de un Dashboard en Power BI para responder preguntas clave de negocio.

## **Estructura del Proyecto**

1. **Python:** Se desarrollaron scripts en Python para transformar los datos de las pestañas "Casos" y "Meta" del archivo de Excel proporcionado. Los scripts realizan las siguientes tareas:
    - Ejercicio 1: Transformación de la pestaña "Casos" en un DataFrame estructurado (df_casos_bd).
    - Ejercicio 2: Unión del DataFrame resultante con la pestaña "Meta" para calcular el porcentaje de cumplimiento (df_casos_union).
2. **SQL:** Se creó un script SQL para agrupar la información de df_casos_union por red social, tipo, año y mes, obteniendo la cantidad total de casos.
3. **Power BI**: Se desarrolló un Dashboard para visualizar el cumplimiento de las metas diarias, el comportamiento de casos por día, y el desglose por red y tipo. Las tablas "Caso" y "Meta" se cargan directamente en Power BI y se relacionan en Power Query.

## Instrucciones para Ejecutar el Proyecto
1. Configurar el Entorno Virtual:
    - Crear un entorno virtual con Python 3.9.12.
    - Ejecutar el siguiente comando en la terminal:
       ```bash
         python -m venv venv
       ```
    - Activar el entorno:
        - En Windows: venv\Scripts\activate
2. Clonar el repositorio:
    - Clona el repositorio actual y accede a la carpeta de este:
        ```bash
           git clone https://github.com/MateoRamirezRubio1/Prueba_tecnica_practicas.git
           cd Prueba_tecnica_practicas
        ```
3. Instalar Dependencias:
    - El archivo de requerimientos, instalar con:
      ```bash
         pip install -r requirements.txt
       ```
4. Ejecutar los Scripts de Python:
    - Navegar a la carpeta correspondiente de cada ejercicio y ejecutar cada script:
        - Para el primer ejercicio:
          ```bash
           python script1.py
          ```
        - Para el segundo ejercicio:
          ```bash
           python script2.py
          ```
    - Los resultados se exportarán a archivos de Excel.

## Ejercicio 4: Comandos Git Utilizados
1. Inicializar el repositorio local:
    ```bash
    git init
    ```
    Inicializa un nuevo repositorio Git en el proyecto local.
2. Agregar archivos al área de preparación:
   ```bash
    git add .
    ```
    Añade todos los archivos al área de preparación para ser commit.
3. Guardar los cambios:
   ```bash
    git commit -m "Solucion prueba tecnica"
    ```
    Crea un commit con el mensaje especificado, guardando los cambios en el repositorio local.
5. Enlazar con el repositorio en GitHub:
   ```bash
    git remote add origin https://github.com/MateoRamirezRubio1/Prueba_tecnica_practicas.git
    ```
    Enlaza el repositorio local con el repositorio en GitHub.
5. Crear la rama principal y subir los archivos:
   ```bash
    git branch -M main
    ```
    Cambia el nombre de la rama actual a "main".
   ```bash
    git push -u origin main
    ```
    Sube los cambios al repositorio en GitHub en la rama "main"
