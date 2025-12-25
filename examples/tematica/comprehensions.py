"""
Funciones para entender los for tradicionales y el paso a comprehesions
"""
from ..datos.samples import sample_articles

##Comprehesion para bucle tradicional
def extract_titles_traditional(articles):
    "Extrae títulos usando bucles tradicionales con for."
    titles = []
    for article in articles:
        titles.append(article["title"])
    return titles


def extract_titles(articles):
    "Extrae títulos usando comprehension."
    return [article["title"] for article in articles]


##Comprehesion para bucle tradicional con condicional if
def extract_titles_traditional_at_least(articles):
    "Extrae títulos con al menos 20 caracteres usando bucles tradicionales con for."
    titles = []
    for article in articles:
        if len(article["title"]) >= 20:
            titles.append(article["title"])
    return titles


def extract_titles_at_least(articles):
    "Extrae títulos con al menos 20 caracteres usando comprehension."
    return [article["title"] for article in articles if len(article["title"]) >= 20]


##Comprehesion para bucle tradicional con diccionarios(objetos)
def extract_titles_traditional_dic(articles):
    "Crea un diccionario nuevo únicamente con el título y la descripción usando bucle tradicional."
    summarie = {}
    for article in articles:
        key = article["title"]
        value = article["description"]
        summarie[key] = value
    return summarie


def extract_titles_dic(articles):
    "Crea un diccionario nuevo únicamente con el título y la descripción usando comprehension."
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 10
    }


##Comprehesion para bucle tradicional con conjuntos(sets)
def extract_sources_traditional_set(articles):
    "Crea un conjunto de fuentes únicas usando bucle con comprensión."
    return {article["source"]["name"] for article in articles}


def categorize_news_by_source(articles):
    "Categoriza las noticias según su fuente"
    return {
        category["category"]: 
        [article["title"] for article in articles if category["category"] == article["category"]]
        for category in articles 
    }


print("categorizar", categorize_news_by_source(sample_articles))

""" print("traditional", extract_titles_traditional_dic(sample_articles))
print("==================")
print("comprehesion", extract_titles_dic(sample_articles))
print("==================")
print("comprehesion sets", extract_sources_traditional_set(sample_articles)) """
