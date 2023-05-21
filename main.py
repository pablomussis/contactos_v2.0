# -*- coding: utf-8 -*-
                            # Importamos la función Flask del módulo flask, g, render_template
from flask import Flask, g, render_template, request, redirect, url_for, flash
import sqlite3              # Importamos el módulos completo SQLite3

app = Flask(__name__)

'''
# Función que carga y pone activa la base de datos (contacto.db) con su tabla (contactos):
#def cargar_base(self):
	# Crea, si no existe, y conecta con la base de datos en la dirección indicada:
conexion = sqlite3.connect("contacto.db") #Añadir ruta del archivo "contacto.db" para que funcione correctamente
	# Con cursor manejaremos la base de datos conectada:
cursor = conexion.cursor()
	# Con cursor.execute ejecutaremos sentencias de SQLite3 y SQL
cursor.execute("CREATE TABLE IF NOT EXISTS contactos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, contacto TEXT NOT NULL)")
'''

def get_db():
    db = getattr(g, '_database', None)		# g, es un Objeto Global en Flask
    if db is None:
        db = g._database = sqlite3.connect('contacto.db')	# Función .connect para conectar con la BBDD
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()							# Función .close para cerrar la conexión a la BBDD

app.secret_key = 'mysecretkey'


@app.route('/')             				# Ruta localhost:5000/
def index():
	cursor = get_db().cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS contactos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, contacto TEXT NOT NULL)")
	cursor = get_db().cursor()					# Con cursor manejaremos la base de datos conectada
	cursor.execute("SELECT * FROM contactos")	# Consulta de registros de la tabla contactos
	registros = cursor.fetchall()				# Obtiene todos los datos
	return render_template("index.html", registros = registros) # Pasar los datos a index.html


@app.route('/editar/<id>') # Ruta localhost:5000/modficación
def editar_contacto(id):
	cursor = get_db().cursor()					 # Con cursor manejaremos la base de datos conectada
	print(id)
	# Inserta y actualiza (función commit()) los nuevos registros de la base:
												 # Con cursor.execute ejecutaremos sentencias de SQLite3 y SQL
	cursor.execute("SELECT * FROM contactos WHERE id = (?)", id) # Consulta el registro de la tabla contactos
	registro = cursor.fetchall()				 # Obtiene todos los datos
	return render_template("editar_contacto.html", registro = registro[0]) # Pasar los datos a editar_contacto.html

@app.route('/editar_ok/<id>', methods=["POST"]) # Ruta localhost:5000/modficación
def editar_contacto_ok(id):
	if (request.method == "POST"):			# Si los datos fueron enviados por el método POST
		reg = (request.form['nombre'], request.form['contacto'], id)
		print(reg, id)
		cursor = get_db().cursor()					 # Con cursor manejaremos la base de datos conectada
													 # Con cursor.execute ejecutaremos sentencias de SQLite3 y SQL
		cursor.execute("UPDATE contactos SET nombre = (?), contacto = (?) WHERE id = (?)", reg) # Modificar el registro de la tabla contactos	
		get_db().commit()							 # Edita (función .commit()) el registro seleccionado
		flash("Registro EDITADO con exito !!")
		return redirect(url_for('index'))


@app.route('/alta', methods=["POST"])		# Ruta localhost:5000/alta
def alta_contacto():
	if (request.method == "POST"):			# Si los datos fueron enviados por el método POST
		nombre = request.form["nombre"]
		contacto = request.form["contacto"]
		alta = (nombre, contacto)			# Creación de la tupla alta con los datos del formulario
		cursor = get_db().cursor()			# Con cursor manejaremos la base de datos conectada
		# Inserta y actualiza (función commit()) los nuevos registros de la base:
											# Con cursor.execute ejecutaremos sentencias de SQLite3 y SQL
		cursor.execute("INSERT INTO contactos (nombre, contacto) VALUES (?, ?)", alta)
		get_db().commit()					# Agrega (función .commit()) un registro nuevo
		flash("Registro GUARDADO con exito !!")
		return redirect(url_for('index'))


@app.route('/eliminar/<id>')         		# Ruta localhost:5000/baja
def eliminar_contacto(id):
	print(id)
	cursor = get_db().cursor()				# Con cursor manejaremos la base de datos conectada
	# Inserta y actualiza (función commit()) los nuevos registros de la base:
											# Con cursor.execute ejecutaremos sentencias de SQLite3 y SQL
	cursor.execute("DELETE FROM contactos WHERE id = (?)", id)
	get_db().commit()						# Elimina (función .commit()) el registro seleccionado
	flash("Registro ELIMINADO con exito !!")
	return redirect(url_for('index'))


@app.route('/acercade')     				# Ruta localhost:5000/acercade
def acercade():
	mensaje = """
			Se libera el siguiente código para ser estudiado, reutilizado y redistribuido con sus modificaciones. <br>
			- APP WEB CRUD - Flask 2.2.3 - Python 3.7.3 - SQlite 3.27.2 <br>
			- Sobre el sistema de base GNU/Debian 10. <br>
			- Desarrollado en el laboratorio de la E.E.S.T.N°2 de Fcio Varela <br>
			- Abril de 2023 Versión 0.1 <br>
			- Con el propósito práctico profesional. <br>
			- Prof. Pablo Mussis <br>
			Nota: <br>
			Para su próxima versión se requiere: <br>
			- Modularizar tareas. <br>
			- Configurar un servidor WSGI. <br>
			"""
	#return('<br>' '<h1 style="text-align:center">' 'Acerca del proyecto' '</h1>')
	return('<br>' + '<div>' + mensaje + '</div>')


if (__name__ == '__main__'):
	#cargar_base()
	app.run(port = 5000, debug = True)
