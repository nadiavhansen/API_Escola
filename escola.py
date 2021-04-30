from conexo_mongo import Mongodb
from bson.objectid import ObjectId


class Escola:

    def cadastrar_prova(self, dict_values):
        a = Mongodb()
        a.provas.insert_one(dict_values)

    def cadastrar_alunos(self, dict_values):
        a = Mongodb()
        a.alunos_matricula.insert_one(dict_values)

    def listar_alunos(self):
        a = Mongodb()
        alunos = list(a.alunos_matricula.find())
        return alunos

    def chamar_gabarito(self, id_prova):
        a = Mongodb()
        prova = a.provas.find_one({"_id": ObjectId(id_prova)}, {"_id": 0})
        return prova

    def corrigir_prova(self, id_prova, respostas):
        prova = self.chamar_gabarito(id_prova)

        if not respostas.keys() == prova["Questoes"].keys():
            return "Questões inválidas! Verifique se esqueceu de responder alguma ou se passou o número errado!"

        nota_final = 0
        for numero_questao in prova["Questoes"]:
            if prova["Questoes"][numero_questao]["Resposta correta"].lower() == respostas[numero_questao].lower():
                nota_final += float(prova["Questoes"][numero_questao]["Peso"])

        return f"Sua nota final é {nota_final}!"



        # questoes_gabarito, resposta_gabarito = list(gabarito.keys()), list(gabarito.values())
        # peso_questao = list(peso.values())
        # questoes_aluno, resposta_aluno = list(respostas.keys()), list(respostas.values())
        #
        #
        # try:
        #     if len(questoes_gabarito) == len(questoes_aluno):
        #         for i in resposta_gabarito:
        #             if resposta_gabarito[i] == resposta_aluno:
        #                 pass
        #         print(nota_final)
        #
        #         return nota_final
        #     else:
        #         return "Prova não finalizada! Verifique se respondeu todas as questões"

        # except Exception as error:
        #     return str(error.args)


# @app.route("/cadastrar_prova/", methods=["POST"])
# def cadastrar_prova():
#     raw_request = request.data.decode("utf-8")
#     dict_values = json.loads(raw_request)
#
#     try:
#         chaves = list(dict_values.keys())
#         soma_pesos = sum([dict_values[key]["Peso"] for key in chaves if key != "Nome"])
#         quantidade_questoes = len([dict_values[key] for key in chaves if key != "Nome"])
#         # pesos = [dict_values[key]["Peso"] for key in chaves if key != "Nome"]
#         # for i in pesos:
#         #     round(i, 3)
#         #     print(round(i, 3))
#
#         # soma_pesos = []
#         # for key in chaves:
#         #     if key != "Nome":
#         #         soma_pesos.append(dict_values[key]["Peso"])
#         # soma_pesos = sum(soma_pesos)
#
#         if quantidade_questoes < 1 or quantidade_questoes > 20:
#             return "Quantidade de questões inválidas! Cadastre no mínimo 1 questão e no máximo 20 questões."
#         elif soma_pesos != 10:
#             return "Nota final da prova diferente de 10! Preste atenção nos pesos!"
#
#         else:
#             a = Escola()
#             a.cadastrar_prova(dict_values)
#             return "Prova cadastrada com sucesso!", 200
#
#     except Exception as error:
#         return str(error.args)
#
# @app.rote("/listar_provas/")
#
# if __name__ == "__main__":
#     app.run(debug=True)



        # print(questoes_gabarito)
        # print(resposta_gabarito)
        # print(questoes_aluno)
        # print(resposta_aluno)


    # def chamar_gabarito(self, id_prova):
    #     a = Mongodb()
    #
    #     prova = a.provas.find_one({"_id": ObjectId(id_prova)}, {"_id": 0})
    #     # gabarito = {}
    #     # for numero_questao in respostas["Questoes"]:
    #     #     del respostas['Questoes'][numero_questao]['Alternativas']
    #     #     del respostas['Questoes'][numero_questao]['Peso']
    #     #     gabarito[numero_questao] = respostas['Questoes'][numero_questao]['Resposta correta']
    #
    #     # return gabarito
    #     return prova
    #
    # # def chamar_peso(self, id_prova):
    # #     a = Mongodb()
    # #     repostas = a.provas.find_one({"_id": ObjectId(id_prova)}, {"_id": 0})
    # #     peso = {}
    # #     for numero_questao in repostas['Questoes']:
    # #         del repostas['Questoes'][numero_questao]['Alternativas']
    # #         del repostas['Questoes'][numero_questao]['Resposta correta']
    # #         peso[numero_questao] = repostas['Questoes'][numero_questao]['Peso']
    # #
    # #     return peso

    # import pymongo
    # from flask import Flask, request
    # import json
    # from conexo_mongo import *
    # from aluno import *
