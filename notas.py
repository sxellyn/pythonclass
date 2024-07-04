
class A ():

  def init(self, aluno):
    self.nomeAluno = aluno
    self.atribNota1 = 0
    self.atribNota2 = 0
    self.atribNotaDaFinal = 0
    self.media = 0.00
    self.situacao = False

  def calcularMedia(self, nota1, nota2):
    self.media = (nota1 + nota2)/2
    if (self.media >= 7.00):
      self.situacao = True
    return self.media

  def calcularMediaAposFinal(self, notaFinal):
    self.media = (self.media + notaFinal)/2
    if (self.media >= 5.00):
      self.situacao = True
    return self.media

  def situacaoAluno(self):
    if(self.situacao == True and self.media >= 5.00):
      print("Aluno ",self.nomeAluno, " está em situação Aprovado")
    else:
      print("Aluno ",self.nomeAluno, " está em situação Reprovado")

da = DesempenhoAcademico("Alexandre Cordel")

minhaMedia = da.calcularMedia(10,8)

da.situacaoAluno()