"""
Docstring for sistema_de_noticias.news_api_client
"""

import json
from urllib import error, parse, request
from .exception_api import ApiKyeError

NEWS_API_URL_BASE: str = "https://newsdata.io/api/1/latest"

def news_api_client(
    api_key: str, query: str, timeout: int = 30, retries: int = 3
) -> dict:
    # Construir una URL
    params: dict = {
        "q": query,
        "apiKey": api_key,
        "size": 2,
    }
    query_string: str = parse.urlencode(
        params
    )  # Convierte los parámetros como parte de la URL
    url: str = f"{NEWS_API_URL_BASE}?{query_string}"  # Unificamos la URL base con los parámetros

    try:
        # Enviar el request con administrador de contexto.
        with request.urlopen(url, timeout=timeout) as resp:
            if resp.status != 200:
                raise error.HTTPError(
                    url, resp.status, "Error en la respuesta", resp.headers, None
                )
            data_bytes: str = resp.read()  # Respuesta cruda en bytes.
            # Decodificar y parsear json.
            data_text: str = data_bytes.decode("utf-8")
            data: dict = json.loads(data_text)
            return data
    except error.HTTPError as e:
        raise ApiKyeError("Ocurrio un error: ", e)


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    print(f"Guardian: section={section}")
    print(f"From_date={from_date}")
    print(f"Timeout={timeout}")
    # retries sin usar


def fetch_news(api_name: str, *args, **keywords):
    # configuración base común a múltiples APIs
    base_config = {
        "timeout": 30,  # por defecto
        "retries": 3,  # por defecto
    }

    # fusión de configuración: base + parámetros nombrados entrantes
    config = {**base_config, **keywords}

    # selección de cliente por nombre
    api_clients = {
        "newsAPI": news_api_client,  # referencia a cliente de News API
        "Guardian": guardian_client,  # referencia a cliente de Guardian
    }

    client = api_clients[api_name]
    return client(*args, **config)
