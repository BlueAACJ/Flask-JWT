from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json
import os
from flask_cors import CORS

app = Flask(__name__)

# Configuración del JWT sin expiración
app.config["JWT_SECRET_KEY"] = "clave_secreta_para_api"  # Cambiar por algo seguro
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False  # Desactiva la expiración

jwt = JWTManager(app)  # Inicializar JWTManager

CORS(app)  # Esto habilita CORS para todas las rutas

load_dotenv()

app.secret_key = os.getenv("contrasena")

# Ruta del archivo JSON
ruta_conParametros = "conParametros.json"

ruta_sinParametros= "sinParametros.json"

# Leer el archivo JSON
with open(ruta_conParametros, "r", encoding="utf-8") as archivo:
    datos_conParametros = json.load(archivo)

# Leer el archivo JSON
with open(ruta_sinParametros, "r", encoding="utf-8") as archivo:
    datos_sinParametros = json.load(archivo)   

@app.route('/', methods=['GET','POST'])
def funcion():
    username = "Hola mundo"
    # Generar un token de acceso sin expiración
    token = create_access_token(identity=username)
    return jsonify(access_token=token), 200

# Ruta sin Parametros
@app.route('/sinParametros', methods=['GET'])
# @jwt_required()
def sinParametros():
    return render_template("sinParametros.html")

# Ruta con Parametros
@app.route('/conParametros', methods=['GET'])
# @jwt_required()
def conParametros():
    return render_template("conParametros.html")

############ API´s con parametros y sin parametros ############

# Ruta para obtener todos los registros
@app.route('/api/Aldeas/', methods=['GET'])
@jwt_required()
def obtener_todos_los_registros():
    get_jwt_identity()  # Obtener el usuario del token
    return jsonify(datos_sinParametros)

# Ruta para obtener un registro específico por ID
@app.route('/api/Aldeas/<int:id_register>', methods=['GET'])
@jwt_required()
def obtener_registro_por_id(id_register):
  if id_register:
    get_jwt_identity()  # Obtener el usuario del token
    print(id_register)
    return jsonify(datos_conParametros)

# Manejo de errores por tokens inválidos
@app.errorhandler(401)
def handle_unauthorized(e):
    return jsonify({"msg": "Token inválido o ausente"}), 401

# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)
