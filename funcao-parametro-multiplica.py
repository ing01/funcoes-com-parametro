# Algoritmo contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado.

def multiplicar(numero):
  r = numero * 2
  print('O valor multiplicado por 2 é',r)

def main():
  n = int(input('Insira um valor: '))
  multiplicar(n)

main()
