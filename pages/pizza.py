import streamlit as st

store = st.sidebar.selectbox("store",['main','피자헛','도미노피자'])

if store == 'main':
    st.title("피자 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

if store == '피자헛':
    st.title("피자헛")
    pizza = st.checkbox("a")

if store == '도미노피자':
    st.title("도미노피자")
    b = st.checkbox("b")
    if b:
        st.write("선택됨!")