from flask import Flask, render_template
app = Flask('meu app')


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
    return render_template(exibir_entradas)



    @app.route('/')
def exibir_entradas():
    sql = '''select titulo, texto from entriadas order by id desc'''
    cur = g.db.execute(sql)
    entradas = [dict(titulo=titulo, texto=texto)
                    for titulo, texto in cur.fetchall()]
    return render_template('exibir_entradas.html', entradas=entradas)