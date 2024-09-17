#class
#instanciar 
import requests

class GitHub:
    BASE_URL = "https://api.github.com/users"

    def __init__(self, usuario):
        self.usuario = usuario

    def obter_dados(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.github = GitHub(nome)

    def exibir_perfil(self):
        dados = self.github.obter_dados(self.nome)
        if dados:
            print(f"\nPerfil de {self.nome}:\n"
                  f"Login: {dados['login']}\n"
                  f"Nome: {dados['name']}\n"
                  f"Localizacao: {dados['location']}\n"
                  f"Bio: {dados['bio']}\n"
                  f"Repositorios Publicos: {dados['public_repos']}\n"
                  f"Seguidores: {dados['followers']}\n"
                  f"Seguindo: {dados['following']}")
        else:
            print("Usuario nao encontrado ou erro ao acessar API.")

    def exibir_repositorios(self):
        repos = self.github.obter_dados(f"{self.nome}/repos")
        if repos:
            while True:
                print("\nRepositorios Publicos:")
                for i, repo in enumerate(repos, start=1):
                    print(f"{i}. {repo['name']}")
                
                escolha = input("\nDigite o numero do repositorio para acessar ou 'nao' para voltar: ").strip().lower()
                if escolha.isdigit():
                    indice = int(escolha) - 1
                    if 0 <= indice < len(repos):
                        print(f"\nAcessando: {repos[indice]['html_url']}")
                    else:
                        print("Numero invalido.")
                elif escolha == 'nao':
                    break
                else:
                    print("Entrada invalida.")

                if escolha.isdigit() and 0 <= indice < len(repos):
                    if input("Deseja acessar mais algum? (sim/nao): ").strip().lower() != 'sim':
                        break
        else:
            print("Erro ao acessar os repositorios.")

class App:
    def iniciar(self):
        while True:
            nome = input("Qual usuario do GitHub voce quer buscar? ")
            usuario = Usuario(nome)

            escolha = input("Deseja ver 'perfil' ou 'repositorios'? ").strip().lower()
            if escolha == 'perfil':
                usuario.exibir_perfil()
                if input("Ver repositorios? (sim/nao): ").strip().lower() == 'sim':
                    usuario.exibir_repositorios()
            elif escolha == 'repositorios':
                usuario.exibir_repositorios()
                if input("Ver perfil? (sim/nao): ").strip().lower() == 'sim':
                    usuario.exibir_perfil()

            if input("Buscar outro perfil? (sim/nao): ").strip().lower() != 'sim':
                break

if __name__ == "__main__":
    App().iniciar()
