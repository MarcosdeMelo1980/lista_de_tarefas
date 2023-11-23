from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template('form_add.html')

# Rota para adicionar tarefas
@app.route("/add", methods=["GET", "POST"])
def add():
    from models.tarefa import Tarefa
    if request.method == "POST":
        #try:
        # Obtenha os dados do formulário
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        data = request.form.get('data')
        hora = request.form.get('hora')

            # Crie uma nova instância da classe Tarefa
        nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, data=data, hora=hora)

            # Adicione a nova tarefa ao banco de dados
        db.session.add(nova_tarefa)
        db.session.commit()

        return redirect(url_for('listar_tarefas'))  # Redireciona para a lista de tarefas após a adição

        #except Exception as e:
            # Lidar com erros, como exceções de validação de dados
           # return render_template('erro.html', mensagem=str(e))

    return render_template('form_add.html')  # Renderiza o formulário HTML para adicionar tarefas

# Adicione uma rota para listar tarefas (você pode ajustar isso conforme necessário)

@app.route("/listar_tarefas")
def listar_tarefas():
    tarefas = Tarefa.query.all()
    return render_template('lista_tarefas.html', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)


def py():
    return None