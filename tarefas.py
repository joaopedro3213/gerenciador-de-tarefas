from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    tarefa = request.json.get('tarefa')
    tarefas.append(tarefa)
    return jsonify({"message": "Tarefa adicionada!"}), 201

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    try:
        tarefas.pop(id)
        return jsonify({"message": "Tarefa excluída!"}), 200
    except IndexError:
        return jsonify({"message": "Tarefa não encontrada!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
