from Server import app
from flask import jsonify
from flask import request
from Services.AtualizarAluno import atualizarAluno
from Services.CadastrarAluno import cadastrarAluno
from Services.DeletarAluno import deletarAluno
from Services.ListarAluno import listarAlunos
from Services.ConsultarAluno import consultarAluno
from Models.Aluno import Aluno
from Models.Resposta import Resposta

@app.route("/alunos", methods=["GET"])
def listarAluno():
    alunos = listarAlunos()
    if len(alunos) == 0: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = []
        Resposta["Mensagem"] = "Nao ha alunos"

        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = alunos
    Resposta["Mensagem"] = "Lista Alunos"

    return jsonify(Resposta)

@app.route("/alunos/<ra>", methods=["GET"])
def consultaAluno(ra):
    aluno = consultarAluno(ra)

    if aluno:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = aluno
        Resposta["Mensagem"] = "Consulta de Alunos"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Aluno nao encontrado"
    return jsonify(Resposta)

@app.route("/alunos", methods=["POST"])
def cadastroAluno():
    dados = request.get_json()

    aluno = cadastrarAluno({"ra":dados["ra"], "nome":dados["nome"]})

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = aluno
    Resposta["Mensagem"] = "Aluno Cadastrado"

    return jsonify(Resposta)

@app.route("/alunos/<ra>", methods=["PUT"])
def atualizaAluno(ra):
    dados = request.get_json()

    aluno = atualizarAluno({"ra":dados["ra"], "nome":dados["nome"]},ra)

    if aluno:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = aluno
        Resposta["Mensagem"] = "Aluno atualizado"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Aluno nao encontrado"
    return jsonify(Resposta)

@app.route("/alunos/<ra>", methods=["DELETE"])
def removerAluno(ra):

    removido = deletarAluno(ra)

    if removido:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = {}
        Resposta["Mensagem"] = "Aluno Removido"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Aluno nao encontrado"
    return jsonify(Resposta)


@app.route("/forums", methods=["POST"])
def criarForum():
    dados = request.get_json()

    forum = criarForum(
        {
        "ForumId":dados["ForumId"], 
        "OwnerId":dados["OwnerId"], 
        "Title": dados["Title"], 
        "Description":dados["Description"], 
        "CreateDate":dados["CreateDate"], 
        "LastPostDate":dados["LastPostDate"], 
        "Active":dados["Active"]
        }
    )

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = forum
    Resposta["Mensagem"] = "Forum Criado"

    return jsonify(Resposta)

