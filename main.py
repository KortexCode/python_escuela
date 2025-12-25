from news_api.open_ia import analyze_ai_output


def main():
    print("Hello from python-escuela!")
    # main.py - Todo el código en un archivo
    """
    Sistema de análisis de noticias con APIs múltiples.
    """

    # Se importan paquetes
    import os

    from dotenv import load_dotenv

    from news_api.exception_api import ApiKyeError

    load_dotenv()

    # PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
    API_TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    DEFAULT_LANGUAGE: str = "es"  # PEP 8: Comillas dobles para strings
    NEWS_API_KEY: str = os.getenv("API_KEY")

    # PEP 8: Bloque principal
    try:
        data_result: dict | None = None
        """ data_result = fetch_news("newsAPI", NEWS_API_KEY, "video games") """
        analyze_ai_output("tecnología")

    except ApiKyeError as e:
        print(e)
    finally:
        print("Request finalizado.")

    if data_result:
        print("resultado", data_result)
    else:
        print("No se obtuvieron datos.")


if __name__ == "__main__":
    main()
