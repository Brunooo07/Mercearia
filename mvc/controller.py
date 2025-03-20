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
                DaoCategoria.salvar(novaCategoria)
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
                   print(f"Categoria: {i.categoria}")
class ControllerEstoque:
     def cadastrarProduto(self, nome, preco, categoria, quantidade):
          x = DaoEstoque.ler()
          y = DaoCategoria.ler()
          h = list(filter(lambda x: x.categoria == categoria, y))
          estoque = list(filter(lambda x: x.produto.nome == nome, x))
          if len(h) > 0:
               if len(estoque) == 0:
                    produto = Produtos(nome, preco, categoria)
                    DaoEstoque.salvar(produto, quantidade)
                    print('Produto cadastrado com sucesso')
               else:
                    print('Produto já existe em estoque')
          else:
               print('Categoria inexistente')
               
     def removerProduto(self, nome):
          x = DaoEstoque.ler()
          estoque = list(filter(lambda x: x.produto.nome == nome, x))
          if len(estoque) > 0:
               for i in range(len(x)):
                    if x[i].produto.nome == nome:
                         del x[i]
                         print('O produto foi removido com sucesso')
                         break
          else:
               print(f'O produto {nome} não existe')
          with open('estoque.txt', 'w') as arq:
               for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines("\n")
     def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
          x = DaoEstoque.ler()
          y = DaoCategoria.ler()
          h = list(filter(lambda x: x.categoria == novaCategoria, y))
          if len(h) > 0:
               estoque = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
               if len(estoque) > 0:
                    estoque = list(filter(lambda x: x.produto.nome == novoNome, x))
                    if len(estoque) == 0:
                         x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if (x.produto.nome == nomeAlterar) else (x), x))
                         print(f'O produto {nomeAlterar} foi alterado com sucesso para {novoNome}, custando {novoPreco}R$, na categoria {novaCategoria} e {novaQuantidade} quantidades')
                    else:
                         print('Produto já cadastrado')
               else:
                    print(f'O produto {nomeAlterar} não existe ')
          with open('estoque.txt', 'w') as arq:
               for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines("\n")
     def mostrarEstoque(self):
          estoque = DaoEstoque.ler()
          if len(estoque) == 0:
               print('Estoque vazio')
          else:
               for i in estoque:
                    print("============Produtos===========")
                    print(f'Nome: {i.produto.nome}\n'
                          f'Preço: {i.produto.preco}\n'
                          f'Categoria: {i.produto.categoria}\n'
                          f'Quantidade: {i.quantidade}'
                          )
class ControllerVenda:
    def cadastrarVenda(self, comprador, vendedor, nomeProduto, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if not existe and i.produto.nome == nomeProduto:
                existe = True
                if i.quantidade >= int(quantidadeVendida):
                    quantidade = True
                    i.quantidade -= int(quantidadeVendida)
                    vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                    valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                    DaoVenda.salvar(vendido)
                    print(f'A venda foi cadastrada com sucesso')
            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        # Aqui agora está certo: reescreve o arquivo só uma vez
        with open('estoque.txt', 'w') as arq:
            for item in temp:
                arq.writelines(item[0].nome + "|" + item[0].preco + "|" + item[0].categoria + "|" + str(item[1]))
                arq.writelines("\n")
        
        if not existe:
            print(f'O produto {nomeProduto} não existe no estoque')
            return None
        elif not quantidade:
            print('Não há essa quantidade em estoque')
            return None
        else:
            return valorCompra

    def relatorioGeralVendas(self):
        vendas = DaoVenda.ler()
        if not vendas:
            print('Nenhuma venda realizada.')
            return
        for venda in vendas:
            print("========== Venda ==========")
            print(f'Produto: {venda.itensVendidos.nome}')
            print(f'Categoria: {venda.itensVendidos.categoria}')
            print(f'Preço Unitário: {venda.itensVendidos.preco}')
            print(f'Vendedor: {venda.vendedor}')
            print(f'Comprador: {venda.comprador}')
            print(f'Quantidade Vendida: {venda.quantidadeVendida}')
            print(f'Data: {venda.data}')
