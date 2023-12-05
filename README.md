# Juice
# Proyecto Django

Este es un proyecto desarrollado con Django, un framework de Python.

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto localmente:

### Requisitos previos

- Python 3.x
- Pip (administrador de paquetes de Python)

### Pasos de instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/JJRoca/Juice.git
    ```

2. Ve al directorio del proyecto:

    ```bash
    cd tu_proyecto
    ```

3. Crea y activa un entorno virtual (opcional pero recomendado):

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

5. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Crea un superusuario (opcional):

    ```bash
    python manage.py createsuperuser
    ```

7. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

8. Visita `http://localhost:8000` en tu navegador para ver la aplicación.


