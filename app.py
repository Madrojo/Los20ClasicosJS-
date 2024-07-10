#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify, render_template
from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------



app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

#--------------------------------------------------------------------
class Usuarios:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS hincha (
            dni VARCHAR(8) NOT NULL PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            apellido VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            genero CHAR(10),
            hinchade VARCHAR(50),
            mensaje TEXT)''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    #----------------------------------------------------------------
    def agregar_hincha(self, dni, nombre, apellido, email, genero, hinchade, mensaje):
               
        sql = "INSERT INTO hincha (dni, nombre, apellido, email, genero, hinchade, mensaje) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (dni, nombre, apellido, email, genero, hinchade, mensaje)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return self.cursor.lastrowid

    #----------------------------------------------------------------
    def consultar_hincha(self, dni):
        # Consultamos un hincha a partir de su dni
        self.cursor.execute(f"SELECT * FROM hincha WHERE dni = {dni}")
        return self.cursor.fetchone()

    #----------------------------------------------------------------
    def modificar_hincha(self, dni, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_genero, nuevo_hinchade, nuevo_mensaje):
        sql = "UPDATE hincha SET nombre = %s, apellido = %s, email = %s, genero = %s, hinchade = %s, mensaje = %s WHERE dni = %s"
        valores = (nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_genero, nuevo_hinchade, nuevo_mensaje, dni)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def listar_hincha(self):
        self.cursor.execute("SELECT * FROM hincha")
        hincha = self.cursor.fetchall()
        return hincha

    #----------------------------------------------------------------
    def eliminar_hincha(self, dni):
        # Eliminamos un hincha de la tabla a partir de su dni
        self.cursor.execute(f"DELETE FROM hincha WHERE dni = {dni}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_hincha(self, dni):
        # Mostramos los datos de un hincha a partir de su dni
        hincha = self.consultar_hincha(dni)
        if hincha:
            print("-" * 40)
            print(f"dni.....: {hincha['dni']}")
            print(f"nombre: {hincha['nombre']}")
            print(f"apellido...: {hincha['apellido']}")
            print(f"email.....: {hincha['email']}")
            print(f"genero.....: {hincha['genero']}")
            print(f"hinchade.....: {hincha['hinchade']}")
            print(f"mensaje..: {hincha['mensaje']}")
            print("-" * 40)
        else:
            print("Hincha no encontrado.")


#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
usuarios = Usuarios(host='localhost', user='root', password='1234', database='myapp')
#catalogo = Catalogo(host='USUARIO.mysql.pythonanywhere-services.com', user='USUARIO', password='CLAVE', database='USUARIO$miapp')


# Carpeta para guardar las imagenes.
# RUTA_DESTINO = './imagenes/'

#Al subir al servidor, deberá utilizarse la siguiente ruta. USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
#RUTA_DESTINO = '/home/USUARIO/mysite/static/imagenes'


#--------------------------------------------------------------------
# Listar todos los productos
#--------------------------------------------------------------------
#La ruta Flask /productos con el método HTTP GET está diseñada para proporcionar los detalles de todos los productos almacenados en la base de datos.
#El método devuelve una lista con todos los productos en formato JSON.
@app.route("/hincha", methods=["GET"])
def listar_hincha():
    hincha = usuarios.listar_hincha()
    return jsonify(hincha)


#--------------------------------------------------------------------
# Mostrar un sólo producto según su código
#--------------------------------------------------------------------
#La ruta Flask /productos/<int:codigo> con el método HTTP GET está diseñada para proporcionar los detalles de un producto específico basado en su código.
#El método busca en la base de datos el producto con el código especificado y devuelve un JSON con los detalles del producto si lo encuentra, o None si no lo encuentra.
@app.route("/hincha/<int:dni>", methods=["GET"])
def mostrar_hincha(dni):
    hincha = usuarios.consultar_hincha(dni)
    if hincha:
        return jsonify(hincha), 201
    else:
        return "Hincha no encontrado", 404


#--------------------------------------------------------------------
# Agregar un producto
#--------------------------------------------------------------------
@app.route("/hincha", methods=["POST"])
#La ruta Flask `/productos` con el método HTTP POST está diseñada para permitir la adición de un nuevo producto a la base de datos.
#La función agregar_producto se asocia con esta URL y es llamada cuando se hace una solicitud POST a /productos.
def agregar_hincha():
    #Recojo los datos del form
    dni = request.form['dni']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    genero = request.form['genero']
    hinchade = request.form['hinchade']
    mensaje = request.form['mensaje']    
    

    
    # Genero el nombre de la imagen
    # nombre_imagen = secure_filename(imagen.filename) #Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema de archivos
    # nombre_base, extension = os.path.splitext(nombre_imagen) #Separa el nombre del archivo de su extensión.
    # nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" #Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.

    nuevo_dni = usuarios.agregar_hincha(dni, nombre, apellido, email, genero, hinchade, mensaje)
    
    if not nuevo_dni:    
        # imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))

        #Si el producto se agrega con éxito, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 201 (Creado).
        return jsonify({"mensaje": "Hincha agregado correctamente.", "codigo": nuevo_dni}), 201
    else:
        #Si el producto no se puede agregar, se devuelve una respuesta JSON con un mensaje de error y un código de estado HTTP 500 (Internal Server Error).
        return jsonify({"mensaje": "Error al agregar el producto."}), 500
    

#--------------------------------------------------------------------
# Modificar un producto según su código
#--------------------------------------------------------------------
@app.route("/hincha/<int:dni>", methods=["PUT"])
#La ruta Flask /productos/<int:codigo> con el método HTTP PUT está diseñada para actualizar la información de un producto existente en la base de datos, identificado por su código.
#La función modificar_producto se asocia con esta URL y es invocada cuando se realiza una solicitud PUT a /productos/ seguido de un número (el código del producto).
def modificar_hincha(dni):
    #Se recuperan los nuevos datos del formulario
    nuevo_nombre = request.form.get("nombre")
    nuevo_apellido = request.form.get("apellido")
    nuevo_email = request.form.get("email")
    nuevo_genero = request.form.get("genero")
    nuevo_hinchade = request.form.get("hinchade")
    nuevo_mensaje = request.form.get("mensaje")
        
    
    # Verifica si se proporcionó una nueva imagen
    # if 'imagen' in request.files:
      #   imagen = request.files['imagen']
        # Procesamiento de la imagen
        # nombre_imagen = secure_filename(imagen.filename) #Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema de archivos
        # nombre_base, extension = os.path.splitext(nombre_imagen) #Separa el nombre del archivo de su extensión.
        # nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" #Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.

        # Guardar la imagen en el servidor
        # imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
        
        # Busco el producto guardado
        # producto = catalogo.consultar_producto(codigo)
        # if producto: # Si existe el producto...
          #   imagen_vieja = producto["imagen_url"]
            # Armo la ruta a la imagen
            # ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

            # Y si existe la borro.
            # if os.path.exists(ruta_imagen):
              #   os.remove(ruta_imagen)
    
    # else:
        # Si no se proporciona una nueva imagen, simplemente usa la imagen existente del producto
      #   producto = catalogo.consultar_producto(codigo)
         #if producto:
           #  nombre_imagen = producto["imagen_url"]


    # Se llama al método modificar_producto pasando el codigo del producto y los nuevos datos.
    hinchaModificado=usuarios.modificar_hincha(dni, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_genero, nuevo_hinchade, nuevo_mensaje)
    print(hinchaModificado)
    if hinchaModificado:
        
        #Si la actualización es exitosa, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
        return jsonify({"mensaje": "Hincha modificado"}), 200
    else:
        #Si el producto no se encuentra (por ejemplo, si no hay ningún producto con el código dado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado).
        return jsonify({"mensaje": "Hincha no encontrado"}), 404



#--------------------------------------------------------------------
# Eliminar un producto según su código
#--------------------------------------------------------------------
@app.route("/hincha/<int:dni>", methods=["DELETE"])
#La ruta Flask /productos/<int:codigo> con el método HTTP DELETE está diseñada para eliminar un producto específico de la base de datos, utilizando su código como identificador.
#La función eliminar_producto se asocia con esta URL y es llamada cuando se realiza una solicitud DELETE a /productos/ seguido de un número (el código del producto).
def eliminar_hincha(dni):
    # Busco el producto en la base de datos
    hincha = usuarios.consultar_hincha(dni)
    if hincha: # Si el producto existe, verifica si hay una imagen asociada en el servidor.
      #   imagen_vieja = producto["imagen_url"]
        # Armo la ruta a la imagen
        # ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

        # Y si existe, la elimina del sistema de archivos.
        # if os.path.exists(ruta_imagen):
         #    os.remove(ruta_imagen)

        # Luego, elimina el producto del catálogo
        if usuarios.eliminar_hincha(dni):
            #Si el producto se elimina correctamente, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
            return jsonify({"mensaje": "Hincha eliminado"}), 200
        else:
            #Si ocurre un error durante la eliminación (por ejemplo, si el producto no se puede eliminar de la base de datos por alguna razón), se devuelve un mensaje de error con un código de estado HTTP 500 (Error Interno del Servidor).
            return jsonify({"mensaje": "Error al eliminar el hincha"}), 500
    else:
        #Si el producto no se encuentra (por ejemplo, si no existe un producto con el codigo proporcionado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado). 
        return jsonify({"mensaje": "Hincha no encontrado"}), 404

#--------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)