from conexo_mongo import Mongodb


class Aluno:

    def conferir_matricula(self, codigo_matricula):
        a = Mongodb()
        alunos = a.alunos_matricula.find({"Matricula": codigo_matricula}, {'_id': 0, 'Matricula': 1}).count()
        if alunos > 0:
            return True
        return False

    # def chamar_gabarito(self, id_prova):
    #     a = Mongodb()
    #
    #     respostas = a.provas.find_one({"_id": ObjectId(id_prova)}, {"_id": 0})
    #     gabarito = {}
    #     repostas_corretas, questoes = [], []
    #     for numero_questao in respostas["Questoes"]:
    #         del respostas["Questoes"][numero_questao]["Alternativas"]
    #         del respostas["Questoes"][numero_questao]["Peso"]
    #         gabarito[numero_questao] = respostas["Questoes"][numero_questao]["Resposta correta"]
    #
    #     # print(list(gabarito.keys()))
    #     # print(list(gabarito.values()))
    #
    #     return gabarito

        # print(gabarito)
        # return respostas

# a = Aluno()
# b = print(a.chamar_gabarito("608ae111e83b5f6fb733ca19"))

# def realizar_prova(self, dict_values):
#     a = Mongodb()
#     a.alunos_prova.insert_one(dict_values)

#
# for i in gabarito.values():
#     repostas_corretas.append(i)
#
# for i in gabarito:
#     questoes.append(i)

# from flask import Flask, request
# from escola import *
# import json
# from conexo_mongo import *
# import pandas as pd
# from random import randint
# from bson.objectid import ObjectId