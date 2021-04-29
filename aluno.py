from flask import Flask, request
from escola import *
import json
from conexo_mongo import *
import pandas as pd
from random import randint
from bson.objectid import ObjectId

class Aluno:

    def __init__(self):
        pass

    def realizar_prova(self, dict_values):
        a = Mongodb()
        a.alunos_prova.insert_one(dict_values)

    def conferir_matricula(self, codigo_matricula):
        a = Mongodb()
        alunos = a.alunos_matricula.find({"Matricula": codigo_matricula}, {'_id': 0, 'Matricula': 1}).count()
        if alunos > 0:
            return True
        return False

    def chamar_gabarito(self, id_prova):
        a = Mongodb()

        respostas = a.provas.find_one({"_id": ObjectId(id_prova)}, {"_id": 0})
        for numero_questao in respostas["Questoes"]:
            del respostas["Questoes"][numero_questao]["Alternativas"]
            del respostas["Questoes"][numero_questao]["Peso"]
        return respostas


a = Aluno()
b = a.chamar_gabarito("608ae511a4478812bd4e0561")
print(b)
questoes = b['Questoes']
print(questoes)
print(questoes)




