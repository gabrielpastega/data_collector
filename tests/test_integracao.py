import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(".env")

# verificar as variáveis de ambiente
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# criar url de conexão com o banco de dados
DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# função teste para ler os dados e checar o schema
def test_read_data_and_check_schema():
    df = pd.read_sql('SELECT * FROM vendas', con=DATABASE_URL)

    # verificar se o dataframe não está vazio
    assert not df.empty, "O DataFrame está vazio."

    # verificar o schema (colunas e tipos de dados)
    expected_dtype = {
        'id': 'int64',
        'email': 'object',
        'data': 'datetime64[ns]',
        'valor': 'float64',
        'produto': 'object',
        'quantidade': 'int64',
        'categoria': 'object',
    }