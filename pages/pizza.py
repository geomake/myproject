import streamlit as st
import sqlite3 

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
p=0
store = st.sidebar.selectbox("store",['main','피자헛','도미노피자'])

if store == 'main':
    st.title("피자 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

    st.image('./img/1221.png')
    st.write("피자(pizza)는 밀가루로 만든 얇고 납작한 반죽에 토마토 소스와 치즈 등 토핑을 얹어서 구워 내는 이탈리아 요리이다. 세계 각지에서 가장 대중적으로 사랑받는 요리 가운데 하나로, 파스타와 함께 이탈리아의 상징과도 같은 음식이라 할 수 있다.")
    st.write("")
    st.write("본래 이탈리아 피자는 크기가 미국 피자에 비해 좀 작고 토핑이 간소하며 드문드문하게 올리는 경향이 있다.[1] 미국식 피자는 최대한 많은 재료를 올려 여러 명이 함께 나누어 먹는 음식이라는 인식이 강하기 때문에 크기가 상당히 크고 토핑도 비교적 다양한 반면,[2] 이탈리아에서는 간편하게 한 끼를 때우는 음식이라 한 명, 많아봤자 두 사람이 먹을 만큼만 만든다. 먹을 만큼만 만든다. 물론 이탈리아에도 미국과 같은 크게 만드는 피자가 있는데, 둥글넓적하게 만드는 미국식이 아니라 사각형으로 넓적하게 한 판씩 만들어 케이크 조각처럼 잘라 판매한다.[3] 이 방식의 피자는 로마나 시칠리아 등지에서 흔히 볼 수 있다.")
    st.write("")
    st.write("")
    st.write("------------------------------")

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
        st.session_state.money = st.session_state.money - p
        sql=f"""UPDATE user SET money ="{st.session_state.money}" WHERE username = "{st.session_state.id}"
            """
        cursor.execute(sql)
        conn.commit()


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
        st.session_state.money = st.session_state.money - p
        sql=f"""UPDATE user SET money ="{st.session_state.money}" WHERE username = "{st.session_state.id}"
            """
        cursor.execute(sql)
        conn.commit()
