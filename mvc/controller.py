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
         cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
         if len(cat) <= 0:
              print('Essa categoria não existe')
         else:
              for i in range(len(x)):
                   if x[i].categoria == categoriaRemover:
                        del x[i]
                        break
              print('Categoria removida com sucesso')

              with open('categoria.txt', 'w') as arq:
                   for i in x:
                        arq.writelines(i.categoria)
                        arq.writelines('\n')
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
         x = DaoCategoria.ler()
         cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
         if len(cat) > 0:
              cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
              if len(cat1) == 0:
               x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else(x), x))
               print(f'A categoria {categoriaAlterar} foi modificada para {categoriaAlterada} ')
              else:
                    print(" A categoria para qual deseja alterar já existe")
         else:
               print("A categoria que deseja alterar não existe")

         with open('categoria.txt', 'w') as arq:
              for i in x:
                   arq.writelines(i.categoria)
                   arq.writelines('\n')
    def mostrarCategoria(self):
         categorias = DaoCategoria.ler()
         if len(categorias) == 0:
              print('Não há categorias')
         else:
              for i in categorias:
                   print(i.categoria)
a = ControllerCategoria()
a.mostrarCategoria()