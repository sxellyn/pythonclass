
#classe

class Boletim():
  def __init__(self, estudante):
    self.estudante = estudante

  #calculo com mensagem de aprovado e reprovado

  def calculo(self):
    bimestre1 = float(input("Insira a nota do primeiro bimestre:"))
    bimestre2 = float(input("Insira a nota do segundo bimestre:"))
    bimestre3 = float(input("Insira a nota do terceiro bimestre:"))
    bimestre4 = float(input("Insira a nota do quarto bimestre:"))
    self.media = (bimestre1 + bimestre2 + bimestre3 + bimestre4)/4
    if self.media >=6:
      print('A média é ', self.media, 'e o estudante está aprovado :)')
    else:
      print('A média é ', self.media, 'e o estudante foi reprovado.\ninfelizmente o estudante terá que passar por reavaliação :(')

    #recuperação

  def recuperacao(self):
    if self.media >=6.0:
     print("Bem vindo a recuperação!")
    nota = float(input("Insira a nota de recuperação:"))
    print("Sua nota foi de recuperação foi:", nota)
    if nota >=6:
        print("Você aprovado!:)")
    else:
        print("Infelizmente você foi reprovado!")

  def automatizacao(self):
    self.calculo()
    self.recuperacao()

aluno = Boletim("Suellyn")
aluno.automatizacao()