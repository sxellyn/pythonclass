#virou pokemon
import random

class Partes():
  def __init__(self, nome,nivel_ataque=0, nivel_defesa=0, consumo_mana=0):
    self.nome = nome
    self.nivel_ataque = nivel_ataque
    self.nivel_defesa = nivel_defesa
    self.consumo_mana = consumo_mana
    self.available = True

  def print_status(self):
    print(self.nome)
    print("Nivel de Ataque:", self.nivel_ataque)
    print("Nivel de Defesa:", self.nivel_defesa)
    print("Custo de Mana:", self.consumo_mana)
    print("Está disponivel?:", self.available)

class Pokemon:
    def __init__(self, nome, tipo, nome_jogador):
      self.nome = nome
      self.tipo = tipo
      self.nome_jogador = nome_jogador
      self.mana= 100
      self.vivo = True
      self.parte = {
          "Ataque Básico": Partes("Ataque Básico", nivel_ataque=5, nivel_defesa=5, consumo_mana=0),
          "Habilidade 1": Partes("Habilidade 1",  nivel_ataque=25, nivel_defesa=15, consumo_mana=20),
          "Habilidade 2": Partes("Habilidade 2", nivel_ataque=35, nivel_defesa=25, consumo_mana=30),
      }
    def ataque(self, pokemon_inimigo, escolha_ataque, alvo):
      pokemon_inimigo.print_status[alvo].nivel_defesa  = self.parte[escolha_ataque].nivel_ataque
      self.mana = self.parte[escolha_ataque].consumo_mana

    def skill_especial(self):
      habilidades = {
          Partes("Passiva", nivel_ataque=0, nivel_defesa=30, consumo_mana=0),
          Partes("Habilidade Especial", nivel_ataque=15, nivel_defesa=0, consumo_mana=10),
      }
      super = random.choice(habilidades)
      self.parte["super"] = super
      print("O Pokémon aprendeu algo especial!")
      super.print_status
      print("Preparando Pokémon para batalha.")

    def apresentacao(self):
        print(self.nome)
        print(self.tipo)
        print("Total de Mana:", self.mana)
        print("Nome do Jogador:", self.nome_jogador)
        print(self.nome_jogador+":", self.nome +', Eu escolho você!')

    def status(self):
      if self.mana > 0:
        print('Pokémon pronto para combate, vamos lá!')
      else:
        print('O pokémon precisa descansar, volte em 1 hora.')

squirtle = Pokemon("Squirtle", "Tipo Água", "Suellyn")
squirtle.apresentacao()
chamar = squirtle.status()
print("Squirtle: squirtle! :)")