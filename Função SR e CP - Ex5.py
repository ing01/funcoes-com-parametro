##Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem lida.

def preco(produto, porcentagem):
  reajuste = produto * (porcentagem / 100 + 1)
  print('O novo valor do produto é',reajuste)

def main():
  valor = int(input('Insira o valor do produto: '))
  percent = int(input('Insira a porcentagem de aumento: '))
  preco(valor, percent)

main()
