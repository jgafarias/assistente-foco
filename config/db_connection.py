import sqlite3
import os
import dotenv

def connection():
    
    # Carregar variáveis de ambiente do arquivo .env
    dotenv.load_dotenv()

    # Obter o caminho do banco de dados a partir das variáveis de ambiente
    db_name = os.getenv('DB_NAME', 'apps.db')
    db_path = os.getenv('DB_PATH', './db')

    # Verificar se o diretório do banco de dados existe, se não, criar
    if not os.path.exists(db_path):
        os.makedirs(db_path)

    # Construir o caminho completo do banco de dados
    db_file = os.path.join(db_path, db_name)

    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(db_file)
    
    return conn