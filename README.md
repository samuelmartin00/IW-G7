# IW-G7 - Gestión de Eventos Musicales

## Descripción

IW-G7 es un proyecto de Django desarrollado para la gestión de eventos musicales. Permite organizar y explorar información relacionada con canciones, artistas, álbumes y géneros musicales.

## Comenzando

### Prerrequisitos

Asegúrate de tener instalados los siguientes elementos antes de comenzar:

- Python
- Django: Puedes instalarlo con el comando `pip install django`.

### Instalación

1. Clona el repositorio: `git clone https://github.com/{tu_usuario}/MusicArchive.git`.
2. Navega al directorio del proyecto: `cd MusicArchive`.
3. Ejecuta las migraciones: `python manage.py migrate`.
4. Crea un superusuario para acceder al panel de administración: `python manage.py createsuperuser`.
5. Inicia el servidor de desarrollo: `python manage.py runserver`.

## Uso

- Accede al [panel de administración](http://localhost:8000/admin/) utilizando las credenciales del superusuario.
- Explora la lista de canciones, detalles de artistas, álbumes y géneros.

## Estructura del Proyecto

- `manage.py`: Script de Django para tareas administrativas.
- `views.py`: Contiene funciones de vista para renderizar plantillas HTML.
- `urls.py`: Configura los patrones de URL del proyecto.
