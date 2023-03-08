from os import system
from math import pow, ldexp, trunc

def limpaTela():
  system('cls') or None

if __name__ == '__main__':

  while True:

    limpaTela()

    print(("-----"*4).center(50))
    print(("MEIA-VIDA").center(50))
    print(("-----"*4).center(50))
    print("1 - Quant. Inicial para Quant. Final")
    print("2 - Quant. Final para Quant. Inicial")

    opcao = input("Escolha uma das opções: ")


    limpaTela()

    if not(opcao.isnumeric()):
      input("Opção não aceita texto. Por favor, aperte \'Enter\' para digitar novamente! ")
    else:
      match int(opcao):
        case 1:
          while True:

            limpaTela()

            qtd_inicial = input("Digite a quantidade inicial da amostra: ")

            limpaTela()

            tempo_meia_vida = input("Digite o tempo de meia-vida da amostra, em anos: ")

            limpaTela()

            tempo = input("Digite o intervalo de tempo do processo de decaimento, em anos: ")

            limpaTela()

            if qtd_inicial.isnumeric() and tempo_meia_vida.isnumeric() and tempo.isnumeric():
              qtd_atual = int(qtd_inicial) * (pow((1/2), (int(tempo)/int(tempo_meia_vida))))

              print(f"Quantidade atual de organismos: {qtd_atual}")
              break
            else:
              input("Valor inválido! Aperte \'Enter\' para digitar novamente!")
              continue
        case 2:
          while True:
              
            limpaTela()

            qtd_atual = input("Digite a quantidade final da amostra: ")

            limpaTela()

            tempo_meia_vida = input("Digite o tempo de meia-vida da amostra, em anos: ")

            limpaTela()

            tempo = input("Digite o intervalo de tempo do processo de decaimento, em anos: ")

            limpaTela()

            if qtd_atual.isnumeric() and tempo_meia_vida.isnumeric() and tempo.isnumeric():
              qtd_inicial = ldexp(int(qtd_atual), trunc(int(tempo)/int(tempo_meia_vida)))

              print(f"Quantidade inicial de organismos: {qtd_inicial}")

              break
            else:
              input("Valor inválido! Aperte \'Enter\' para digitar novamente!")
        case _:
          input("Valor inválido! Aperte \'Enter\' para digitar alguma das opções mostradas!")
          continue
      break

