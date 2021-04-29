import pymongo


class Mongodb:

    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conn["ex_escola"]
        self.provas = self.db["provas"]
        self.alunos_matricula = self.db["alunos_matricula"]
        self.alunos_prova = self.db["alunos_prova"]

