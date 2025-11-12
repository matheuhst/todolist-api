from flask import jsonify
from conexao import get_conexao
from psycopg2.extras import RealDictCursor

def buscar_tarefas():
    con = get_conexao()
    cursor = con.cursor(cursor_factory = RealDictCursor)
    cursor.execute(
    "SELECT id, name, description FROM todos ORDER BY id;"
)

    todos = cursor.fetchall()
    cursor.close()

    return jsonify(todos)

def buscar_tarefa(id):
    con = get_conexao()
    cursor = con.cursor(cursor_factory = RealDictCursor)
    cursor.execute(
    "SELECT id, name, description FROM todos WHERE id = %s;",(id,)
)

    todos = cursor.fetchone()

    cursor.close()
    con.close()

    return jsonify(todos)

def criar_tarefa(name, description):
    con = get_conexao()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO todos (name, description) VALUES (%s, %s)",
        (name, description)
    )
    con.commit()
    cursor.close()
    con.close()

def apagar_tarefa(tarefa_id):
    con = get_conexao()
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM todos WHERE id = %s",
        (tarefa_id,)
    )
    con.commit()
    cursor.close()
    con.close()

def atualizar_tarefa(tarefa_id, name, description):
    con = get_conexao()
    cursor = con.cursor()
    cursor.execute(
        "UPDATE todos SET name=%s, description=%s WHERE id = %s",
        (name, description, tarefa_id)
    )
    con.commit()
    cursor.close()
    con.close()