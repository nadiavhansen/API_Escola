from funcoes.escola import Escola
from conexo_mongo import Mongodb
from flask import Flask, request
import pandas as pd
import json


app = Flask(__name__)

chave_acesso = "essa_e_a_chave"


@app.route("/<api_key>/cadastrar_prova/", methods=["POST"])
def cadastrar_prova(api_key):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    chaves = list(dict_values['Questoes'].keys())
    soma_pesos = sum([dict_values['Questoes'][key]["Peso"] for key in chaves if key != "Nome"])
    quantidade_questoes = len([dict_values['Questoes'][key] for key in chaves if key != "Nome"])

    if api_key == chave_acesso:
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
    else:
        return "Chave de acesso inválida!"


@app.route("/<api_key>/listar_provas/", methods=["GET"])
def listar_provas(api_key):
    a = Mongodb().provas
    if api_key == chave_acesso:
        try:
            df = pd.DataFrame(a.find({}, {"_id": 1, "Nome": 1}))
            df = df.astype(str)
            json = df.to_json(orient="records")
            return json

        except Exception as error:
            return str(error.args)
    else:
        return "Chave de acesso inválida!"

@app.route("/api_key/cadastrar_aluno/", methods=["POST"])
def cadastrar_aluno(api_key):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    escola = Escola()
    db = Mongodb()
    if api_key == chave_acesso:
        try:
            while True:
                matricula = Escola().gerar_matricula()
                response = list(db.alunos_matricula.find({"Matricula": matricula}))
                if response == []:
                    dict_values["Matricula"] = matricula
                    break

            escola.cadastrar_alunos(dict_values)
            return "Aluno cadastrado com sucesso!", 200

        except Exception as error:
            return str(error.args)
    else:
        return "Chave de acesso inválida!"


@app.route("/api_key/listar_alunos/", methods=["GET"])
def listar_alunos(api_key):

    if api_key == chave_acesso:
        a = Mongodb().alunos_matricula
        df = pd.DataFrame(a.find({}, {"_id":0}))
        df = df.astype(str)
        json = df.to_json(orient="records")
        return json
    else:
        return "Chave de acesso inválida!"


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