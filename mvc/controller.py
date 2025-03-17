from dao import *
from model import *
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
                categoria = Categoria(novaCategoria)
                DaoCategoria.salvar(categoria)
                print('Categoria cadastrada com sucesso')
                x = DaoCategoria.ler()
                print([cat.categoria for cat in x])
        else:
            print('A categoria já existe')
    def removerCategoria(self, categoriaRemover):
         x = DaoCategoria.ler()
         cat = filter()

