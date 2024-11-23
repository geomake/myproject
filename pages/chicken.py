import streamlit as st

p=0
store = st.sidebar.selectbox("store",['main','네네치킨','굽네치킨'])

if store == 'main':
    st.title("치킨 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

    st.image('./img/1213.png')
    st.write("치킨(chicken)은 토막난 닭고기에 밀가루나 전분 등을 묻혀서 끓는 기름으로 튀긴 닭 요리이다. 또는 이 요리가 대한민국으로 전해진 뒤 현지화된 한국식 닭튀김의 일종을 일컫는다.")
    st.write("")
    st.write("오늘날에는 조각내지 않고 튀기거나 기름에 튀기지 않는 방식의 요리들까지 광범위하게 치킨이라 불리고 있으며, 다양한 변형들이 만들어지고 있다. 즉, 프라이드 치킨의 줄임말로 시작했지만 튀김 방식이 아닌 새로운 닭요리를 통칭하는 용어로 사용되고 있다. 때문에 치킨과 통닭을 같은 뜻으로 사용하는 사람도 많아졌다. 강냉이와 옥수수를 같은 뜻으로 이해하는 것과 비슷하다.")
    st.write("")
    st.write("")
    st.write("------------------------------")

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

    if chrispy =="고추바사삭":
        p=p+19900

    if chrispy =="치즈바사삭":
        p=p+19900
    
    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')

    

    