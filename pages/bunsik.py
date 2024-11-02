import streamlit as st

p=0
store = st.sidebar.selectbox("store",['main','수미네 분식집','김밥천국'])

if store == 'main':
    st.title("분식 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

if store == '수미네 분식집':
    st.title("수미네 분식집")

    sumi_tt = st.checkbox("수미떡볶이 : 4000 원")
    if sumi_tt:
        p=p+4000
        sumi_hot=st.radio('맵기 선택',["안매워요"
                                      ,"약간 매워요",
                                      "너무 매워요!"])

        if sumi_hot =="안매워요":
            st.write("선택됨!")

        if sumi_hot =="약간 매워요":
            st.write("선택됨!")

        if sumi_hot =="너무 매워요!":
            st.write("선택됨!")

    sumi_kim = st.checkbox("수미김밥 : 종류별")
    if sumi_kim:
        st.write("기본:3500원 / 참치:4000원 / 돈까스:4100원")
        sumi_kim_menu = st.radio('메뉴 선택',["기본"
                                      ,"참치",
                                      "돈까스"])
        
        if sumi_kim_menu =="기본":
            p=p+3500

        if sumi_kim_menu =="참치":
            p=p+4000

        if sumi_kim_menu =="돈까스":
            p=p+4100

    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')

    
        

if store == '김밥천국':
    st.title("김밥천국")
    st.write("[김밥메뉴]")

    kimori = st.checkbox("원조 김밥 : 3000 원")
    if kimori:
        p=p+3000

    kimcheese = st.checkbox("치즈 김밥 : 4000 원")
    if kimcheese:
        p=p+4000

    kimtuna = st.checkbox("참치 김밥 : 4000 원")
    if kimtuna:
        p=p+4000

    kimbeef = st.checkbox("소고기 김밥 : 4500 원")
    if kimbeef:
        p=p+4500


    st.write("[면 메뉴]")
    kimra = st.checkbox("라면 : 4000 원")
    if kimra:
        p=p+4000

        st.write("추가메뉴 선택 ( 각각 가격 : 500원 )")
        kimra_cheese = st.checkbox("치즈 추가")
        if kimra_cheese:
            p=p+500
        kimra_tt = st.checkbox("떡 추가")
        if kimra_tt:
            p=p+500
        kimra_mandu = st.checkbox("만두 추가")
        if kimra_mandu:
            p=p+500
        st.write("")

    kimud = st.checkbox("우동 : 5000")
    if kimud:
        p=p+5000

    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')

