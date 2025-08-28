import streamlit as st
import pandas as pd

# Заголовок с большим шрифтом и цветом
st.title("🍽️ Меню на неделю")
st.markdown("---") # Разделительная линия

# Добавляем картинку
st.image("https://www.example.com/your_menu_image.jpg") # Замените ссылку на свою картинку!

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-weight: bold;
    color: #4CAF50;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Выберите блюда для своей семьи:</p>', unsafe_allow_html=True)

# Ваш код для выбора меню на каждый день
меню_недели = {
    'Вторник': ['Салат', 'Суп', 'Рыба'],
    'Среда': ['Макароны', 'Курица', 'Овощи'],
    'Четверг': ['Пицца', 'Рис', 'Стейк']
}

for день, блюда in меню_недели.items():
    st.header(f"Меню на {день}:")
    выбор = st.selectbox(f"Ваш выбор на {день}:", блюда)

    st.write(f"Вы выбрали: **{выбор}**")
