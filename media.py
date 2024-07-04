class Boletim():
  def __init__(self, estudante):
    self.nome = estudante
    self.bimestre1 = 0
    self.bimestre2 = 0
    self.bimestre3 = 0
    self.bimestre4 = 0
    self.media = 0.00
    self.recuperacao = 0

  def calculo_de_media(self, bimestre1, bimestre2, bimestre3, bimestre4):
    self.media = (bimestre1 + bimestre2 + bimestre3 + bimestre4)/4
    #comparar notas aqui com input
    if (self.media >= 7.00):
      return print(f'A média é {self.media} e o estudante está aprovado :)')
    else:
      return print(f'A média é {self.media} e estudante está reprovado :(')

aluno1 = Boletim('Suellyn')
aluno1.calculo_de_media(9.5, 9, 8, 10)