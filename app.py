pip install streamlit
import streamlit as st
import pandas as pd

# Заголовок приложения
st.title("Планировщик питания на неделю")
st.write("Выберите блюда на каждый день недели для одного человека.")

# Список дней недели
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# Список доступных блюд
available_dishes = {
    "Супы": ["Борщ", "Куриный суп", "Грибной суп"],
    "Вторые блюда": ["Котлеты с пюре", "Плов", "Макароны с сыром"],
    "Салаты": ["Оливье", "Винегрет", "Салат Цезарь"]
}

# Словарь для хранения заказов
orders = {}

# Создаем секции для каждого дня недели
for day in days_of_week:
    st.header(f"🍽️ {day}")
    
    # Виджеты для выбора блюд по категориям
    soup_choice = st.selectbox(f"Выберите суп на {day.lower()}:", ["Не выбрано"] + available_dishes["Супы"])
    main_course_choice = st.selectbox(f"Выберите второе блюдо на {day.lower()}:", ["Не выбрано"] + available_dishes["Вторые блюда"])
    salad_choice = st.selectbox(f"Выберите салат на {day.lower()}:", ["Не выбрано"] + available_dishes["Салаты"])
    
    # Сохраняем выбор в словарь
    orders[day] = {
        "Суп": soup_choice,
        "Второе блюдо": main_course_choice,
        "Салат": salad_choice
    }

# Кнопка для отображения сводки заказа
st.markdown("---")
st.header("📄 Ваше меню на неделю")
if st.button("Показать мой заказ"):
    # Создаем DataFrame для удобного отображения
    df = pd.DataFrame(orders).transpose()
    df = df.replace("Не выбрано", "—")
    st.dataframe(df)

# Кнопка для подсчета продуктов (здесь будет ваша логика)
st.markdown("---")
if st.button("Подсчитать продукты"):
    st.warning("Функция подсчета продуктов пока не реализована.")
    st.write("Здесь будет логика, которая проходит по вашему заказу и составляет список покупок.")
streamlit run app.py
