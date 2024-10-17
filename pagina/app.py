from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuração do diretório para salvar as imagens
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16MB

def connect_db():
    conn = sqlite3.connect('dbProdutos.db')
    return conn

def get_data_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nome_produto, descricao FROM produtos")
    data = cursor.fetchall()
    
    conn.close()
    return data

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/joinUs')
def trabalhe_conosco():
    return render_template('book.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        img_file = request.files['upload-img']

        if img_file and img_file.filename != '':
            filename = secure_filename(img_file.filename)  # Nome seguro para o arquivo
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img_file.save(img_path)

            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO produtos (nome_produto, descricao, caminho_img) VALUES (?, ?, ?)", (name, description, img_path))
            conn.commit()
            conn.close()

            return redirect(url_for('tabela_dados'))
        else:
            return "Erro: Nenhuma imagem foi enviada.", 400

@app.route('/addItem')
def adicionar_item():
    return render_template('addItem.html')

@app.route('/dataTable')
def tabela_dados():
    
    dados = get_data_from_db()
    return render_template('dataTable.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)