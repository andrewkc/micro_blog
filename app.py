
from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = 'Mi_llave_Secreta'
#Creamos una función decorativa

#htpp://localhost:5000/
@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho login {session["username"]}'
    #app.logger.info(f'Mensaje a nivel info {request.path}')
    return 'El usuario no ha hecho login' 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        session['username'] = usuario
        #session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}'

@app.route('/edad/<float:edad>')
def mostrar_edad(edad):
    return f'Tu edad es {edad + 1.3}'

@app.route('/mostrar/<nombre>', methods = ['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', pnombre = nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre',  nombre = 'Juan')) 
    #Entre paréntesis va el nombre de la función a la cual nos vamos a redireccionar con la función redirect

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrado(error):
    return (render_template('error404.html', error = error), 404)

#REST Representation state transfer
@app.route('/api/mostrar/<nombre>', methods = ['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'methods': request.method}
    return jsonify(valores)

#SESIONES PARA CREAR UN LOGIN

