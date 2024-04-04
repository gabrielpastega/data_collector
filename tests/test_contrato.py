import pytest
from datetime import datetime
from pydantic import ValidationError
from src.contrato import Channels

def teste_vendas_com_dados_validos():
    dados_validos = {
        "channel_id": 83901231,
        "channel_name": "OTHER PLACE",
        "channel_type": "OWN CHANNEL"
    }
    channels = Channels(**dados_validos)
    assert channels.channel_id == dados_validos["channel_id"]
    assert channels.channel_name == dados_validos["channel_name"]
    assert channels.channel_type == dados_validos["channel_type"]

def teste_vendas_com_dados_invalidos():
    dados_invalidos = {
        "channel_id": "83901231",
        "channel_name": 1233331,
        "channel_type": True
    }
    with pytest.raises(ValidationError):
        Channels(**dados_invalidos)
        
# def teste_validacao_categoria():
#     dados_categoria = {
#         "email": "comprador@example.com",
#         "data": datetime.now(),
#         "valor": 100.50,
#         "produto": "Produto Y",
#         "quantidade": 3,
#         "categoria": "categoria inexistente"
#     }
#     with pytest.raises(ValidationError):
#         Vendas(**dados_categoria)

