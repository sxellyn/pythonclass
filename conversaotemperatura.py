#Exercicio 02
class Metereologia:
  nome = input("Qual seu nome")

  def get_weather(self):
    fahrenheit = float(input("Insira a temperatura em F°:"))
    celsius = (fahrenheit - 32)/1.8
    if fahrenheit >= 65:
      print("Clima é ideal para sair sem casaco.")
    else:
      print("Fique em casa, está frio lá fora.")
    print(f"Este valor em celsius equivale a {celsius:.2f}")



metereologia = Metereologia()
metereologia.get_weather()
