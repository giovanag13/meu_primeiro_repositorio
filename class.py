class Calculadora:
    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("O divisor não pode ser zero.")
            return None

    def obter_numero(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Erro: por favor, insira um número válido.")

    def executar(self):
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
                num1 = self.obter_numero("Digite o primeiro número: ")
                num2 = self.obter_numero("Digite o segundo número: ")

                if escolha == '1':
                    print(f"\nResultado: {num1} + {num2} = {self.adicionar(num1, num2)}")

                elif escolha == '2':
                    print(f"\nResultado: {num1} - {num2} = {self.subtrair(num1, num2)}")

                elif escolha == '3':
                    print(f"\nResultado: {num1} * {num2} = {self.multiplicar(num1, num2)}")

                elif escolha == '4':
                    resultado = self.dividir(num1, num2)
                    if resultado is not None:
                        print(f"\nResultado: {num1} / {num2} = {resultado}")

            else:
                print("Opção inválida, tente novamente.")
            print("\n")

calc = Calculadora()
calc.executar()
