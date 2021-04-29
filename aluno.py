from flask import Flask, request
from escola import *
import json
from conexo_mongo import *
import pandas as pd
from random import randint

class Aluno:

    def __init__(self):
        pass

    def realizar_prova(self, dict_values):
        a = Mongodb()
        a.alunos_prova.insert_one(dict_values)

