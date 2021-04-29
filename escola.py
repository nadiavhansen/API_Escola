# Exercício 2
# Escola:
# A escola deve ser capaz de criar uma prova, onde cada questão dela tenha um peso exato.
# A nota da prova deverá ser 10.
# A soma de todos os pesos não poderá ser diferente de 10). Caso seja diferente de 10, a prova não deverá ser salva e
# o usuário deverá ser avisado que há um erro nos pesos.
# Nenhuma questão poderá ter peso 0.
# Os pesos poderão ser números decimais, porém com no máximo 3 casas decimais.
# Essa prova poderá ter de 1 a 20 questões e todas são de múltipla escolha.
# Cada prova deverá ser salva com um id (que pode ser gerado pelo banco).
# Não será possível alterar uma prova depois de salva.
# Deve-se ter em banco todos os alunos que estão matriculados na escola.
# Apenas alunos que estão matriculados poderão fazer as provas.
#
# Rotas Escola:
# Para acessar cada uma das rotas, a escola deve usar uma chave de acesso.
# Ter um rota para conseguir listar todos os alunos matriculados.
# Terá uma rota onde será possível criar a prova. O usuário deverá entrar com um json contendo Nome da prova, número
# da questão, resposta correta da questão, peso da questão e alternativas da questão.
# Ex: {
# 	"Nome":"Ciências - Reprodução humana",
# 	"1":{
# 		"Alternativas":["A", "B", "C"]
# 		"Resposta correta":"A",
# 		"Peso":5},
# 	"2":{
# 		"Alternativas":["A", "B", "C"]
# 		"Resposta correta":"C",
# 		"Peso":5}
# 	}
# Ter uma rota onde é possível listar todas as provas (Somente mostrar o id e o nome da prova na listagem)
# Ter uma rota para cadastrar o aluno na escola com seu Nome, data de nascimento (deverá gerar um número de matricula,
# e esse número deve ser retornado ao aluno após concluir a matricula).
#
#
#
# Aluno:
# O aluno precisa selecionar uma prova para fazer
# Ao fazer a prova, o aluno poderá "assinalar" somente uma alternativa por questão da prova.
#
# Rotas Aluno:
# Para acessar qualquer uma das rotas, o aluno deverá usar seu número de matricula.
# Ter uma rota onde é possível listar todas as provas (Somente mostrar o id e o nome da prova na listagem)
# Ter uma rota onde o aluno coloque o id da prova e liste todas as questões e alternativas da prova.
# Ex de retorno:
# 1 - A, B, C
# 2 - 1, 2, 3, 4, 5
# Não será necessário mostrar um enunciado para as questões.
#
# Terá uma rota onde o aluno fará a prova. Ele precisa mandar o id da prova desejada, o número da questão e a resposta.
# Ex: {
# 	"id":"1234",
# 	"1":"C",
# 	"2":"B"
# 	}
# Obs: O aluno é obrigado a mandar todas as questões da prova com resposta, mesmo que ela seja nula (string vazia).
# Caso o aluno não responda alguma das questões, deve retornar um erro.
# Caso a alternativa de resposta escolhida esteja fora das existentes, deve se considerar que ele errou a resposta.
# Caso não haja erro no json, a nota do aluno deve ser retornada.

import pymongo
from flask import Flask, request
import json
from conexo_mongo import *

app = Flask(__name__)


class Escola:

    def cadastrar_prova(self, dict_values):
        a = Mongodb()
        a.provas.insert_one(dict_values)


@app.route("/cadastrar_prova/", methods=["POST"])
def cadastrar_prova():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    try:
        chaves = list(dict_values.keys())
        soma_pesos = sum([dict_values[key]["Peso"] for key in chaves if key != "Nome"])
        quantidade_questoes = len([dict_values[key] for key in chaves if key != "Nome"])
        # pesos = [dict_values[key]["Peso"] for key in chaves if key != "Nome"]
        # for i in pesos:
        #     round(i, 3)
        #     print(round(i, 3))

        # soma_pesos = []
        # for key in chaves:
        #     if key != "Nome":
        #         soma_pesos.append(dict_values[key]["Peso"])
        # soma_pesos = sum(soma_pesos)

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

# @app.rote("")

if __name__ == "__main__":
    app.run(debug=True)
