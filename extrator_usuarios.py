import requests
import csv # Biblioteca nativa do Python para lidar com planilhas CSV

def gerar_relatorio_usuarios():
    # A URL agora busca a lista completa de usuários, não apenas 1
    url = "https://dummyjson.com/users"
    
    print("Iniciando a extração de dados da API...")
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        
        # A API retorna um dicionário onde a chave 'users' contém a lista de pessoas
        dados = resposta.json()
        lista_usuarios = dados.get('users', [])
        
        if not lista_usuarios:
            print("Nenhum usuário encontrado na API.")
            return

        print(f"Sucesso! {len(lista_usuarios)} usuários encontrados. Gerando arquivo...")

        # Abre (ou cria) um arquivo chamado relatorio_usuarios.csv no modo de escrita ('w')
        # encoding='utf-8' garante que acentos (como em 'São Paulo') funcionem perfeitamente
        with open('relatorio_usuarios.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
            
            # Cria o "escritor" do arquivo
            escritor = csv.writer(arquivo_csv, delimiter=';') # Ponto e vírgula é melhor pro Excel em PT-BR
            
            # Escreve a primeira linha (O cabeçalho da planilha)
            escritor.writerow(['Nome Completo', 'Idade', 'Email', 'Cidade', 'Empresa', 'Cargo'])
            
            # Loop que percorre cada usuário da lista e extrai os dados
            for usuario in lista_usuarios:
                nome = f"{usuario.get('firstName')} {usuario.get('lastName')}"
                idade = usuario.get('age')
                email = usuario.get('email')
                
                # Acessando dados aninhados com segurança (como aprendemos antes!)
                cidade = usuario.get('address', {}).get('city', 'N/A')
                empresa = usuario.get('company', {}).get('name', 'N/A')
                cargo = usuario.get('company', {}).get('title', 'N/A')
                
                # Escreve a linha do usuário atual na planilha
                escritor.writerow([nome, idade, email, cidade, empresa, cargo])
                
        print("Finalizado! Arquivo 'relatorio_usuarios.csv' criado com sucesso na sua pasta.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
    except Exception as e:
        # Captura qualquer outro erro (como falta de permissão para salvar o arquivo)
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    gerar_relatorio_usuarios()