from flask import Flask
from tarefa import buscar_tarefas, buscar_tarefa

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return {
        'message': 'API rodando'
    }

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

@app.route('/api/tarefa', methods=['GET'])
def get_tarefa():
    tarefa = buscar_tarefa()
    return tarefa

if __name__ == '__main__':
    app.run(debug=True)