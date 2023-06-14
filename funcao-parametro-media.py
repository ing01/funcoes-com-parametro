# Algoritmo com função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que 
# verifique se esta média aprova ou reprova o aluno.

def aluno(nota1, nota2):
  media = (nota1 + nota2) / 2
  print('A média do aluno é',media)
  verificar(media)

def verificar(media):
  if media > 4:
    print('O aluno foi aprovado.')
  else:
    print('O aluno foi reprovado.')

def main():
  p1 = int(input('Insira a nota da primeira prova: '))
  p2 = int(input('Insira a nota da segunda prova: '))
  aluno(p1, p2)

main()
