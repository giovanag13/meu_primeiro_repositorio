import requests

class GitHub:
    def __init__(self, usuario, base_url="https://api.github.com/users"):
        self.usuario = usuario
        self.base_url = base_url

    def obter_dados(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

class Usuario:
    def __init__(self, nome, base_url):
        self.nome = nome
        self.github = GitHub(nome, base_url)

    def exibir_perfil(self):
        dados = self.github.obter_dados(self.nome)
        if dados:
            print(f"\nPerfil de {self.nome}:\n"
                  f"Login: {dados.get('login', 'N/A')}\n"
                  f"Nome: {dados.get('name', 'N/A')}\n"
                  f"Localizacao: {dados.get('location', 'N/A')}\n"
                  f"Bio: {dados.get('bio', 'N/A')}\n"
                  f"Repositorios Publicos: {dados.get('public_repos', 0)}\n"
                  f"Seguidores: {dados.get('followers', 0)}\n"
                  f"Seguindo: {dados.get('following', 0)}")
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
        base_url = input("Digite a URL base da API do GitHub (deixe em branco para usar a padrão): ").strip()
        if not base_url:
            base_url = "https://api.github.com/users"

        while True:
            nome = input("Qual usuario do GitHub voce quer buscar? ").strip()
            if not nome:
                print("Nome de usuario não pode estar vazio.")
                continue

            usuario = Usuario(nome, base_url)

            escolha = input("Deseja ver 'perfil' ou 'repositorios'? ").strip().lower()
            if escolha == 'perfil':
                usuario.exibir_perfil()
                if input("Ver repositorios? (sim/nao): ").strip().lower() == 'sim':
                    usuario.exibir_repositorios()
            elif escolha == 'repositorios':
                usuario.exibir_repositorios()
                if input("Ver perfil? (sim/nao): ").strip().lower() == 'sim':
                    usuario.exibir_perfil()
            else:
                print("Escolha inválida. Tente novamente.")

            if input("Buscar outro perfil? (sim/nao): ").strip().lower() != 'sim':
                break

def main():
    app = App()
    app.iniciar()

if __name__ == "__main__":
    main()
