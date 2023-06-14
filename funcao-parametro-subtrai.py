# Algoritmo contendo uma função/método para subtrair dois números e apresentar o resultado.

def subtrair(numero, numero2):
  s = numero - numero2
  print('O valor da subtração é',s)

def main():
  n1 = int(input('Insira o primeiro número: '))
  n2 = int(input('Insira o segundo número: '))
  subtrair(n1, n2)

main()
