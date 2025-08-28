import streamlit as st
import pandas as pd

# Заголовок приложения
st.title("Планировщик питания на неделю для семьи")
st.write("Каждый член семьи может выбрать блюда на каждый день.")

# Список дней недели
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# Список доступных блюд
available_dishes = {
    "Супы": ["Не выбрано", "Борщ", "Куриный суп", "Грибной суп"],
    "Вторые блюда": ["Не выбрано", "Котлеты с пюре", "Плов", "Макароны с сыром"],
    "Салаты": ["Не выбрано", "Оливье", "Винегрет", "Салат Цезарь"]
}

# Список членов семьи
family_members = ["Иван", "Мария", "Петр", "Елена", "Дмитрий"]

# Словарь для хранения всех заказов
all_orders = {member: {} for member in family_members}

# Создаем секцию для каждого члена семьи
for member in family_members:
    # Используем контейнер, чтобы отделить секции
    with st.container():
        st.markdown("---")
        st.header(f"🧑 Заказ для {member}")

        # Создаем поля для выбора блюд на каждый день
        for day in days_of_week:
            st.subheader(f"🍽️ {day}")
            
            # Виджеты для выбора блюд по категориям
            soup_choice = st.selectbox(
                f"Выберите суп для {member.lower()} на {day.lower()}:",
                available_dishes["Супы"],
                key=f"{member}_soup_{day}" # Уникальный ключ для каждого виджета
            )
            main_course_choice = st.selectbox(
                f"Выберите второе блюдо для {member.lower()} на {day.lower()}:",
                available_dishes["Вторые блюда"],
                key=f"{member}_main_course_{day}"
            )
            salad_choice = st.selectbox(
                f"Выберите салат для {member.lower()} на {day.lower()}:",
                available_dishes["Салаты"],
                key=f"{member}_salad_{day}"
            )
            
            # Сохраняем выбор в словарь
            all_orders[member][day] = {
                "Суп": soup_choice,
                "Второе блюдо": main_course_choice,
                "Салат": salad_choice
            }

# Кнопка для отображения общей сводки заказов
st.markdown("---")
st.header("📄 Общее меню на неделю")
if st.button("Показать общее меню"):
    for member in family_members:
        st.subheader(f"Меню для {member}:")
        df = pd.DataFrame(all_orders[member]).transpose()
        df = df.replace("Не выбрано", "—")
        st.dataframe(df)

# Кнопка для подсчета продуктов (здесь будет ваша логика)
st.markdown("---")
if st.button("Подсчитать общий список продуктов"):
    st.warning("Функция подсчета продуктов пока не реализована.")
    # Здесь будет код, который проходит по всем заказам и составляет общий список покупок.



