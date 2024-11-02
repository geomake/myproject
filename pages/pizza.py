import streamlit as st

p=0
store = st.sidebar.selectbox("store",['main','피자헛','도미노피자'])

if store == 'main':
    st.title("피자 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

if store == '피자헛':
    st.title("피자헛")
    supershirmp = st.checkbox("슈퍼슈프림")
    if supershirmp:
        st.write("M:28500원 / L:33900원 ")
        shrimpsize = st.radio('선택',["새우 M"
                                      ,"새우 L",])
        if shrimpsize =="새우 M":
            p=p+28500

        if shrimpsize =="새우 L":
            p=p+33900

    peperoni = st.checkbox("페페로니 러버")
    if peperoni:
        st.write("M:19900원 / L:25900원 ")
        peperonisize = st.radio('선택',["페페로니 M"
                                      ,"페페로니 L",])
        if peperonisize == "페페로니 M":
            p=p+19900

        if peperonisize == "페페로니 L":
            p=p+25900
        
    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')


if store == '도미노피자':
    st.title("도미노피자")
    cheese = st.checkbox("치즈")
    if cheese:
        st.write("M:16500원 / L:23900원 ")
        cheesesize = st.radio('선택',["치즈 M"
                                      ,"치즈 L",])
        if cheesesize =="치즈 M":
            p=p+16500

        if cheesesize =="치즈 L":
            p=p+23900

    bul = st.checkbox("리얼불고기")
    if bul:
        st.write("M:22500원 / L:29900원 ")
        bulsize = st.radio('선택',["불고기 M"
                                      ,"불고기 L",])
        if bulsize == "불고기 M":
            p=p+22500

        if bulsize == "불고기 L":
            p=p+29900

    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')
