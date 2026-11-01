from functools import lru_cache

from transformers import pipeline


# Название готовой модели на Hugging Face.
MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"


@lru_cache
def get_model():
    """
    Загружает модель.
    Благодаря lru_cache загрузка выполняется только один раз.
    """
    return pipeline(
        task="sentiment-analysis",
        model=MODEL_NAME,
    )


def analyze_text(text: str) -> dict:
    """
    Получает текст и возвращает результат анализа.
    """
    cleaned_text = text.strip()

    if not cleaned_text:
        raise ValueError("Введите текст для анализа.")

    model = get_model()
    result = model(cleaned_text)[0]

    return {
        "label": result["label"],
        "score": round(float(result["score"]), 4),
    }