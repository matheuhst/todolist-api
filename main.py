from flask import Flask
from tarefa import buscar_tarefas

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

if __name__ == '__main__':
    app.run(debug=True)