# Algoritmo com função/método para calcular a tabuada de um número informado pelo usuário.

def tabuada(x):
  for cont in range(1,11):
     print('{0} x {1} = {2}'.format(x,cont,x*cont))

def main():
  num = int(input('Insira um valor para descobrir a tabuada: '))
  tabuada(num)

main()
