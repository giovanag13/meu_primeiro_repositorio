def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def obter_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erro: por favor, insira um número válido.")

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("\nSelecione uma opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Calculadora encerrada.")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = obter_numero("Digite o primeiro número: ")
                num2 = obter_numero("Digite o segundo número: ")

                if escolha == '1':
                    print(f"\nResultado: {num1} + {num2} = {adicionar(num1, num2)}")

                elif escolha == '2':
                    print(f"\nResultado: {num1} - {num2} = {subtrair(num1, num2)}")

                elif escolha == '3':
                    print(f"\nResultado: {num1} * {num2} = {multiplicar(num1, num2)}")

                elif escolha == '4':
                    print(f"\nResultado: {num1} / {num2} = {dividir(num1, num2)}")

            except ZeroDivisionError:
                print("O divisor não pode ser zero.")
            except ValueError:
                print("Só é permitido números.")
            except:
                raise Exception("Ocorreu um erro inesperado.")

        else:
            print("Opção inválida, tente novamente.")

        print("\n")

calculadora()

