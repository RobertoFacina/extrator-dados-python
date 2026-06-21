import requests

def buscar_usuario(id_usuario):
    url = f"https://dummyjson.com/user/{id_usuario}"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 
        
        
        dados = resposta.json()
        
        print(f"--- Perfil do Usuário {id_usuario} ---")
        
        
        nome_completo = f"{dados.get('firstName')} {dados.get('lastName')}"
        idade = dados.get('age')
        email = dados.get('email')
        
        print(f"Nome: {nome_completo}")
        print(f"Idade: {idade} anos")
        print(f"Email: {email}")
    
        cidade = dados.get('address', {}).get('city', 'Cidade não informada')
        estado = dados.get('address', {}).get('state', 'Estado não informado')
        
        print(f"Localização: {cidade} - {estado}")
   
        empresa = dados.get('company', {}).get('name', 'Empresa não informada')
        cargo = dados.get('company', {}).get('title', 'Cargo não informado')
        
        print(f"Trabalho: {cargo} na {empresa}")
        print("-" * 30 + "\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")

if __name__ == "__main__":
    
    buscar_usuario(4)