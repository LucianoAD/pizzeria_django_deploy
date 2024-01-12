<h1 align="center"> TPO Backend Grupo 8 <br>Programa Codo a codo </h1>

![Badge en Desarollo](https://img.shields.io/badge/STATUS-FINALIZADO-green) ![Badge en Desarollo](https://img.shields.io/badge/LICENSE-MIT-green)

## :book:Descripción
Este backend sirve como base para una aplicación de ventas,  fue desarrollada con Django y desplegada en PythonAnywhere. 

## :hammer: Estructura

```plaintext
pizzeria_django_deploy
├── README.md
├── andersonpizza
│   ├── ...
├── app_pizzas
│   ├── ...
├── db.sqlite3
├── manage.py
├── quit
├── quit.pub
├── requirements.txt
├── static
│   ├── ...
└── templates
    ├── base.html
    └── landing_page.html
```
## 🧱 Componentes
1. andersonpizza

    Este directorio contiene las configuraciones y ajustes del proyecto Django.

2. app_pizzas

    Este directorio encapsula la aplicación de ventas del producto, manejando modelos, vistas, serializadores y puntos finales de la API.
    La carpeta templates incluye plantillas HTML para vistas relacionadas con los productos.

3. db.sqlite3

    Archivo de base de datos SQLite donde se almacenan los datos de la aplicación.

4. manage.py

    Script de gestión de Django para varios comandos, migraciones y tareas administrativas.

5. static

    Archivos estáticos, incluyendo CSS, JavaScript, imágenes y otros recursos.

6. templates

    Plantillas HTML para la representación de vistas en el frontend.

## :rocket:Funcionalidades

- Modelos y vistas para crear, actualizar y eliminar productos.
- Puntos finales de la API para interactuar con los datos de los productos.
- Implementación del protocolo HTTP y los métodos GET, POST, PUT y DELETE.
- Utilización del formato JSON para enviar y recibir datos desde la base de datos.
   
## :wrench: Configuración y despliegue

- Clonar el repositorio.
- Instalar dependencias con pip install -r requirements.txt.
- Migrar la base de datos con python manage.py migrate.
- Ejecutar el servidor de desarrollo con python manage.py runserver.

## ✔ Puntos finales de la API

- API de Pizzas: http://luad.pythonanywhere.com/
- CRUD: http://luad.pythonanywhere.com/pizzas/


## 🧑‍🤝‍🧑🧑‍🤝‍🧑 Integrantes:

- Luciano Anselmino
- Yanina Tiribelli
- Miguel Angel Estrada Rivera 
- Franco Bernedo
