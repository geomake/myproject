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

    sumi_tt = st.checkbox("수미떡볶이")
    if sumi_tt:
        p=p+4000
        sumi_hot=st.radio('맵기 선택',["안매워요"
                                      ,"약간 매워요",
                                      "너무 매워요!"])

        if sumi_hot =="안매워요":
            st.write('선택됨!')

        if sumi_hot =="약간 매워요":
            st.write('선택됨!')

        if sumi_hot =="너무 매워요!":
            st.write('선택됨!')

    sumi_kim = st.checkbox("수미김밥")
    if sumi_kim:
        sumi_kim_menu = st.radio('메뉴 선택',["기본"
                                      ,"참치",
                                      "돈까스"])
        
        if sumi_kim_menu =="기본":
            p=p+3500
            st.write('선택됨!')

        if sumi_kim_menu =="참치":
            p=p+4000
            st.write('선택됨!')

        if sumi_kim_menu =="돈까스":
            p=p+4100
            st.write('선택됨!')

    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')

    
        

if store == '김밥천국':
    st.title("김밥천국")
    b = st.checkbox("b")
    if b:
        st.write("선택됨!")