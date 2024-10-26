import streamlit as st

p=0
store = st.sidebar.selectbox("store",['main','넹넹치킨','b'])

if store == 'main':
    st.title("치킨 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

if store == '넹넹치킨':
    st.title("넹넹치킨")

    m1 = st.checkbox("청양마요치킨")
    if m1:
        st.write("선택됨!")
        p=p+20000

    m2 = st.checkbox("레스노윙MAXX")
    if m2:
        st.write("선택됨!")
        p=p+21000

    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')

if store == 'b':
    st.title("b")
    b = st.checkbox("b")
    if b:
        st.write("선택됨!")