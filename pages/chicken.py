import streamlit as st

p=0
store = st.sidebar.selectbox("store",['main','네네치킨','굽네치킨'])

if store == 'main':
    st.title("치킨 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

if store == '네네치킨':
    st.title("네네치킨")

    m1 = st.checkbox("청양마요치킨 : 20000 원")
    if m1:
        p=p+20000

    m2 = st.checkbox("레스노윙MAXX : 21000 원")
    if m2:
        p=p+21000

    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')


if store == '굽네치킨':
    st.title("굽네치킨")
    chrispy = st.radio('바사삭시리즈',["오븐바사삭","고추바사삭","치즈바사삭"])
    st.write("오븐:18900원 / 고추:19900원 / 치즈:19900원")
    if chrispy =="오븐바사삭":
        p=p+18900
        st.write('선택됨!')

    if chrispy =="고추바사삭":
        p=p+19900
        st.write('선택됨!')

    if chrispy =="치즈바사삭":
        p=p+19900
        st.write('선택됨!')
    
    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')

    

    