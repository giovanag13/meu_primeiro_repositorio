import requests

def obter_dados(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def exibir_perfil(usuario):
    dados = obter_dados(f"https://api.github.com/users/{usuario}")
    if dados:
        print(f"\nPerfil de {usuario}:\nLogin: {dados['login']}\nNome: {dados['name']}\nLocalizacao: {dados['location']}\nBio: {dados['bio']}\nRepositorios Publicos: {dados['public_repos']}\nSeguidores: {dados['followers']}\nSeguindo: {dados['following']}")
    else:
        print("Usuario nao encontrado ou erro ao acessar API.")

def exibir_repositorios(usuario):
    repos = obter_dados(f"https://api.github.com/users/{usuario}/repos")
    if repos:
        print("\nRepositorios Publicos:")
        for repo in repos:
            print(f"- {repo['name']}")
    else:
        print("Erro ao acessar os repositorios.")

def main():
    while True:
        usuario = input("Qual usuario do GitHub voce quer buscar? ")

        escolha = input("Deseja ver 'perfil' ou 'repositorios'? ").strip().lower()
        if escolha == 'perfil':
            exibir_perfil(usuario)
            if input("Deseja ver os repositorios tambem? (sim/nao): ").strip().lower() == 'sim':
                exibir_repositorios(usuario)
        elif escolha == 'repositorios':
            exibir_repositorios(usuario)
            if input("Deseja ver o perfil tambem? (sim/nao): ").strip().lower() == 'sim':
                exibir_perfil(usuario)

        if input("Deseja buscar outro perfil? (sim/nao): ").strip().lower() != 'sim':
            break

if __name__ == "__main__":
    main()