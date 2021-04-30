from bson.objectid import ObjectId
from funcoes.escola import Escola
from conexo_mongo import Mongodb
from flask import Flask, request
from funcoes.aluno import Aluno
import pandas as pd
import json

app = Flask(__name__)


@app.route("/listar_provas/<matricula>", methods=["GET"])
def listar_provas(matricula):
    a = Mongodb().provas
    try:
        if Aluno().conferir_matricula(matricula):
            df = pd.DataFrame(a.find({}, {"_id": 1, "Nome": 1}))
            df = df.astype(str)
            json = df.to_json(orient="records")
            return json
        else:
            return "Matrícula não existe!"

    except Exception as error:
        return str(error.args)


@app.route("/acessar_prova/<matricula>/<id_prova>", methods=["GET"])
def acessar_provas(matricula, id_prova):
    a = Mongodb().provas

    try:
        if Aluno().conferir_matricula(matricula):
            prova = a.find_one({"_id": ObjectId(id_prova)}, {"_id": 0})
            for numero_questao in prova["Questoes"]:
                del prova["Questoes"][numero_questao]["Resposta correta"]
            return prova
        else:
            return "Matrícula não existe!"

    except Exception as error:
        return str(error.args)


@app.route("/realizar_prova/<matricula>/<id_prova>", methods=["POST"])
def realizar_prova(matricula, id_prova):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    try:
        if Aluno().conferir_matricula(matricula):
            # Escola().corrigir_prova(id_prova, dict_values)
            return Escola().corrigir_prova(id_prova, dict_values), 200
        else:
            return "Matrícula não existe!"

    except Exception as error:
        return str(error.args)


if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/acessar_prova/<id_prova>", methods=["GET"])
# def acessar_provas(id_prova):
#     a = Mongodb().provas
#
#     try:
#         prova = a.find_one({"_id": ObjectId(id_prova)}, {"_id": 0})
#         for numero_questao in prova["Questoes"]:
#             del prova["Questoes"][numero_questao]["Resposta correta"]
#         return prova
#
#     except Exception as error:
#         return str(error.args)

#
#
# @app.route("/realizar_prova/<matricula>/<id_prova>", methods=["POST"])
# def realizar_prova(matricula, id_prova):
#     raw_request = request.data.decode("utf-8")
#     dict_values = json.loads(raw_request)
#     dict_values['Matricula'] = matricula
#     dict_values['id_prova'] = id_prova
#
#     try:
#         if Aluno().conferir_matricula(matricula):
#             a = Aluno()
#             a.realizar_prova(dict_values)
#             return "Prova realizada com sucesso!", 200
#         else:
#             return "Matrícula não existe!"
#
#     except Exception as error:
#         return str(error.args)