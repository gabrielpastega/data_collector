import os
import pandas as pd
from contrato import Vendas
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

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        errors = []
        # verificar se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no Excel : {', '.join(extra_cols)}"

        # validar cada linhas com o schema escolhido
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                errors.append(f"Erro na linha {index + 2}: {e}")

        # retorna tanto o resultado da validação, os erros, quanto o DataFrame
        return df, True, errors
    
    except Exception as e:
        # se houver exceção, retorna o erro e um DataFrame vazio
        return pd.DataFrame(), f"Erro inesperado: {str(e)}"
    
def excel_to_sql(df):
    df.to_sql('vendas', con=DATABASE_URL, if_exists='replace', index=False)