##Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%.

def preco(novo):
  reajuste = (9 * novo) / 100 + novo
  print('O novo preço do produto é',reajuste,'reais.')

def main():
  produto = int(input('Insira o valor do produto: '))
  preco(produto)

main()
