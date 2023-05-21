
# Project name: Listado de contactos (aplicación web)
***
	- Aplicación web en Flask 2.2.3 (Python 3.7.3) con SQLite 3 sobre GNU/Linux Debian 10.

## General info
***
	- Migración de C.L.I. a Web App.
	- Mayo de 2023 Versión 2.0
	- G.U.I. Aplicación web en Flask 2.2.3 (Python 3.7.3) como A. B. M. con base de datos en SQlite3
	- Sobre el sistema de base GNU/Debian 10.
	- Pablo Mussis

### Author developer
***
Pablo Mussis
	- gitlab @pablomussis
	- github @pablomussis

### Nota:
***
Nota: 
  X - Requiere conexión a Internet por enlace al servidor de BOOTSTRAP 5.
 OK - Ejecución correcta sobre el navegador Mozilla Firefox.

### Estructura de la base de datos
***
Base: 	contacto
Tabla: 	contactos
campos 	id INTEGER PRIMARY KEY AUTOINCREMENT 
		nombre TEXT NOT NULL	(nombre completo)
		contacto TEXT NOT NULL	(email, teléfono movil, etc)

### Ejecución de la aplicación web
***
Terminal (o símbolos de sistema)
# Activar el entorno virtual
$ source venv/bin/activate

# Instalar dependencias
$ pip3 install -r requirements.txt

# Correr el servidor de desarrollo, en http://127.0.0.1:5000
$ python3 main.py
