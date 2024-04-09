import os
import pandas as pd
from contrato import Channels, Deliveries, Drivers, Hubs, Orders, Payments, Stores
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

def excel_filename(uploaded_file):
    # verificar o nome do arquivo
    filename = uploaded_file.name

    # retornar a classe do contrato com base no nome do arquivo
    if filename == "channels.csv":
        return Channels
    elif filename == "deliveries.csv":
        return Deliveries
    elif filename == "drivers.csv":
        return Drivers
    elif filename == "hubs.csv":
        return Hubs
    elif filename == "orders.csv":
        return Orders
    elif filename == "payments.csv":
        return Payments
    elif filename == "stores.csv":
        return Stores
    else:
        return f"O arquivo {filename} não é válido, verifique se enviou o arquivo correto"

def process_excel(uploaded_file):

    classe = excel_filename(uploaded_file)

    try:
        df = pd.read_csv(uploaded_file)
        errors = []
        # verificar se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(classe.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no arquivo : {', '.join(extra_cols)}"

        # validar cada linhas com o schema escolhido
        for index, row in df.iterrows():
            try:
                _ = classe(**row.to_dict())
            except Exception as e:
                errors.append(f"Erro na linha {index + 2}: {e}")

        # retorna tanto o resultado da validação, os erros, quanto o DataFrame
        return df, True, errors

    except Exception as e:
        # se houver exceção, retorna o erro e um DataFrame vazio
        return pd.DataFrame(), f"Erro inesperado: {str(e)}"
    
def excel_to_sql(df):
    df.to_sql('channels', con=DATABASE_URL, if_exists='replace', index=False)

