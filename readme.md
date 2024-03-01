# Projeto Avançado - Conexão com Banco de Dados MariaDB

## Descrição
Este projeto demonstra como estabelecer uma conexão com um banco de dados MariaDB a partir de um projeto Python usando o PyCharm. Ele também aborda a criação de um arquivo .env para armazenar variáveis de ambiente de forma segura e a geração de scripts DAO baseados na modelagem do banco de dados.

## Requisitos
- PyCharm instalado no seu sistema.
- Ambiente virtual configurado para o projeto.
- Acesso a um banco de dados MariaDB.

## Instalação e Configuração
1. Clone o repositório para o seu sistema.
2. No diretório raiz do projeto, crie um ambiente virtual:
   ```
   python -m venv .venv
   ```
3. Ative o ambiente virtual:
   - No Windows:
     ```
     .venv\Scripts\activate
     ```
   - No Linux/macOS:
     ```
     source .venv/bin/activate
     ```
4. Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
   ```
   MYSQL_USER=seu_usuario
   MYSQL_PASSWORD=sua_senha
   ```
   Substitua `seu_usuario` e `sua_senha` pelos dados de acesso ao banco de dados MariaDB.
5. Configure a conexão com o banco de dados no arquivo main.py.

## Como Usar
1. Execute o arquivo main.py para estabelecer a conexão com o banco de dados e gerar os scripts DAO.
2. Os scripts DAO serão gerados com base na modelagem do banco de dados MariaDB e poderão ser usados para interagir com o banco de dados.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs ou novos recursos.

## Licença
Este projeto é licenciado sob a [Licença MIT](LICENSE).
