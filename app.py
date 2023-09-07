from flask import Flask, render_template, request, session, flash, redirect, url_for
app = Flask(__name__)


posts = [
    {
        "titulo": "minha primeira postagem",
        "texto": "teste"
    },
    {
        "titulo": "segunda",
        "texto": "teste 2"
    }
]



@app.route('/')
def exibir_entradas():
    entradas = posts
    return render_template('exibir_entradas.html', entradas=entradas)

@app.route('/login.html', methods= ['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return 'ok'
            session['logado'] = True
            flash('Login efetuado com sucesso')
            return redirect(url_for('exibir_entradas'))
        erro = 'Usuário ou senha incorretos'
    return render_template('login.html', erro=erro)