import os

from openai import OpenAI

from examples.datos.samples import sample_articles


def analyze_ai_output(category: str):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    context: str = "\n".join(
        [
            f"Título:{article['title']} - Descripción:{article['description']} - Categoría:{article['category']}"
            for article in sample_articles
        ]
    )

    print(context)

    promt: str = f"""
        Basandote en estas noticias, responde una pregunta.
        {context}
        ¿Cual es la fuete y el título de las noticias que tienen la siguiente categoría {category}?
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="Actua como un agente ai para responder en español sobre un contexto.",
        input=promt,
        max_output_tokens=50,
    )

    return print(response.output_text)
