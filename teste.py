def num_primo(numero):
    """
        Verifica se um número é primo.

        Um número é considerado primo se ele for maior que 1 e não tiver divisores além de 1 e ele mesmo.

        Parâmetros:
        numero (int): O número a ser verificado.

        Retorna:
        bool: True se o número for primo, False caso contrário.
    """
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True
    
def imprimir_primos_varias_vezes(numero):
    """
        A função pede números ao usuário e mostra todos os primos até o número fornecido. Ela continua fazendo isso até você parar o programa.
    """

    print(f"Números primos até {numero}:")

    for i in range(2, numero + 1):
        if num_primo(i):
            print(i)

while True:
    numero_digitado_usuario = int(input("Digite um número: "))
    
    if numero_digitado_usuario <= 0:
        print("Por favor, digite um número maior que zero.")
    else:
        imprimir_primos_varias_vezes(numero_digitado_usuario)
