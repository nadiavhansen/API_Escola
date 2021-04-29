from flask import Flask, request
from escola import *
import json
from conexo_mongo import *
import pandas as pd
from random import randint

app = Flask(__name__)


def gerar_matricula():
    matricula = "".join([str(randint(0, 9)) for i in range(12)])
    return matricula


@app.route("/cadastrar_prova/", methods=["POST"])
def cadastrar_prova():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    chaves = list(dict_values['Questoes'].keys())
    soma_pesos = sum([dict_values['Questoes'][key]["Peso"] for key in chaves if key != "Nome"])
    quantidade_questoes = len([dict_values['Questoes'][key] for key in chaves if key != "Nome"])
    try:
        if quantidade_questoes < 1 or quantidade_questoes > 20:
            return "Quantidade de questões inválidas! Cadastre no mínimo 1 questão e no máximo 20 questões."
        elif soma_pesos != 10:
            return "Nota final da prova diferente de 10! Preste atenção nos pesos!"

        else:
            a = Escola()
            a.cadastrar_prova(dict_values)
            return "Prova cadastrada com sucesso!", 200

    except Exception as error:
        return str(error.args)


@app.route("/listar_provas/", methods=["GET"])
def listar_provas():
    a = Mongodb().provas
    try:
        df = pd.DataFrame(a.find({}, {"_id": 1, "Nome": 1}))
        df = df.astype(str)
        json = df.to_json(orient="records")
        return json

    except Exception as error:
        return str(error.args)


@app.route("/cadastrar_aluno/", methods=["POST"])
def cadastrar_aluno():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    escola = Escola()
    db = Mongodb()

    try:
        while True:
            matricula = gerar_matricula()
            response = list(db.alunos_matricula.find({"Matricula": matricula}))
            if response == []:
                dict_values["Matricula"] = matricula
                break

        escola.cadastrar_alunos(dict_values)
        return "Aluno cadastrado com sucesso!", 200

    except Exception as error:
        return str(error.args)


@app.route("/listar_alunos/", methods=["GET"])
def listar_alunos():
    a = Mongodb().alunos_matricula
    df = pd.DataFrame(a.find({}, {"_id":0}))
    df = df.astype(str)
    json = df.to_json(orient="records")
    return json


if __name__ == "__main__":
    app.run(debug=True)

# pesos = [dict_values[key]["Peso"] for key in chaves if key != "Nome"]
# for i in pesos:
#     round(i, 3)
#     print(round(i, 3))

# soma_pesos = []
# for key in chaves:
#     if key != "Nome":
#         soma_pesos.append(dict_values[key]["Peso"])
# soma_pesos = sum(soma_pesos)