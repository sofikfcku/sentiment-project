import streamlit as st

from model import analyze_text


st.set_page_config(
    page_title="Анализ тональности",
    page_icon="💬",
)

st.title("Анализ тональности текста")

st.write(
    "Введите текст на английском языке. "
    "Модель определит, положительный он или отрицательный."
)

st.write("Пример: **I really enjoyed this movie!**")

text = st.text_area(
    "Текст для анализа",
    height=180,
)

if st.button("Анализировать", type="primary"):
    if not text.strip():
        st.warning("Введите текст для анализа.")
    else:
        try:
            with st.spinner("Модель анализирует текст..."):
                result = analyze_text(text)

            label = result["label"]
            score = result["score"]

            st.subheader("Результат")

            if label == "POSITIVE":
                st.success("Текст положительный 😊")
            else:
                st.error("Текст отрицательный 😞")

            st.write(f"Уверенность модели: **{score:.1%}**")
            st.progress(score)

        except Exception as error:
            st.error(f"Произошла ошибка: {error}")

st.divider()

st.caption(
    "Используется предобученная модель DistilBERT с Hugging Face. "
    "Дополнительное обучение модели не проводится."
)