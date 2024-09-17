def dividir(a, b):

    print(f"Resultado: {a / b}")

def obter_numero(prompt):
    return float(input(prompt))

while True:
    try:
        numero1 = obter_numero("Digite o primeiro número: ")
        numero2 = obter_numero("Digite o segundo número: ")
        dividir(numero1, numero2)

    except ZeroDivisionError:
        print("O divisor nao pode ser zero.")
    except ValueError:
        print("So é permitido numeros")
    except:
        raise Exception("Ocorreu um erro inesperado")
    print("\n")
