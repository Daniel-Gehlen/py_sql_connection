import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import connection

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()


def main():
    # Recuperar o nome de usuário e senha das variáveis de ambiente
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')

    if not user or not password:
        print('Por favor, defina as variáveis de ambiente MYSQL_USER e MYSQL_PASSWORD no arquivo .env.')
        return

    # Configurar os detalhes da conexão
    config = {
        'user': user,
        'password': password,
        'host': 'localhost',  # ou o endereço IP do servidor MariaDB
        'database': 'healthcare',
        'port': '3306'  # geralmente 3306
    }

    try:
        # Estabelecer a conexão com o banco de dados
        conn = mysql.connector.connect(**config)

        if conn.is_connected():
            print('Conexão bem-sucedida ao banco de dados MariaDB!')
            conn.close()
            print('Conexão fechada.')
    except mysql.connector.Error as e:
        print(f'Erro ao conectar ao banco de dados: {e}')


if __name__ == "__main__":
    main()
