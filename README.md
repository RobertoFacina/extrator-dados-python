📊 Gerador de Relatórios Automatizado em Python (Mini-ETL)

Este projeto é um script em Python desenvolvido para demonstrar a automação na extração de dados de uma API REST externa, realizando o tratamento estrutural das informações (JSON) e exportando o resultado final para um formato tabular (CSV).

O projeto simula um processo de ETL (Extract, Transform, Load) em pequena escala, uma rotina muito comum no dia a dia de desenvolvedores e analistas de dados para fornecer relatórios a equipes de negócios.

🚀 Funcionalidades

Consumo de API REST: Conexão com a API pública DummyJSON para listagem de dados.

Tratamento de Dicionários Aninhados: Navegação segura em estruturas JSON complexas utilizando métodos nativos do Python para evitar falhas caso a API retorne dados incompletos.

Exportação Tabular: Geração automática de um arquivo .csv padronizado com separador por ponto e vírgula (;), ideal para importação direta no Microsoft Excel em português.

Tratamento de Exceções: Implementação de blocos try/except para garantir a resiliência do script contra quedas de rede ou erros de servidor (HTTPError).

🛠️ Tecnologias Utilizadas

Python 3.x

Biblioteca requests: Para requisições HTTP.

Biblioteca csv (Nativa): Para manipulação e escrita de arquivos de planilha.

Biblioteca json (Nativa): Para decodificação da resposta da API.

⚙️ Como executar o projeto

Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. Você também precisará instalar a biblioteca requests.

Clone o repositório:

git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO


Instale as dependências:

pip install requests


Execute o script:

python extrator_usuarios.py


Após a execução bem-sucedida, um arquivo chamado relatorio_usuarios.csv será gerado automaticamente no diretório raiz do projeto.

💡 Aprendizados e Estrutura

Este projeto foi construído focando em boas práticas de programação em Python, especificamente:

O uso de f-strings para formatação limpa de texto.

A utilização do método .get() encadeado para acesso seguro a chaves de dicionários, prevenindo KeyErrors.

Manipulação de contexto de arquivos usando o bloco with open(), garantindo que o arquivo na memória seja fechado corretamente após a gravação, evitando vazamento de memória.
