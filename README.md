# IW-G7
IW - G7 -  Gestión de Eventos Musicales

## Descripción

MusicArchive es un proyecto de Django para gestionar información sobre canciones, artistas, álbumes y géneros musicales.

## Comenzando

### Prerrequisitos

- Python instalado.
- Django instalado: `pip install django`.

### Instalación

1. Clona el repositorio: `git clone https://github.com/tuusuario/MusicArchive.git`.
2. Navega al directorio del proyecto: `cd MusicArchive`.
3. Ejecuta las migraciones: `python manage.py migrate`.
4. Crea un superusuario: `python manage.py createsuperuser`.
5. Inicia el servidor: `python manage.py runserver`.

## Uso

- Accede al [panel de administración](http://localhost:8000/admin/).
- Explora la lista de canciones, detalles de artistas, álbumes y géneros.

## Estructura del Proyecto

- `manage.py`: Script de Django.
- `views.py`: Funciones de vista.
- `urls.py`: Configuración de URL.
