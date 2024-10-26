import streamlit as st

p=0
store = st.sidebar.selectbox("store",['main','롯데리아','맘스터치'])

if store == 'main':
    st.title("햄버거 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

if store == '롯데리아':
    st.title("롯데리아")
    lott_bul = st.checkbox("불고기버거")
    lott_shi = st.checkbox("새우버거")
    lott_han = st.checkbox("한우버거")


#롯데리아 불고기
    if lott_bul:
        lott_bulm = st.radio('선택',["불고기 버거만"
                                      ,"불고기 세트",])
        if lott_bulm =="불고기 버거만":
            p=p+4700
            st.write('선택됨!')

        if lott_bulm =="불고기 세트":
            p=p+6900
            st.write('선택됨!')


#롯데리아 새우
    if lott_shi:
        lott_shim = st.radio('선택',["새우 버거만"
                                      ,"새우 세트",])
        if lott_shim =="새우 버거만":
            p=p+4700
            st.write('선택됨!')

        if lott_shim =="새우 세트":
            p=p+6900
            st.write('선택됨!')


#롯데리아 한우
    if lott_han:
        lott_hanm = st.radio('선택',["한우 버거만"
                                      ,"한우 세트",])
        if lott_hanm =="한우 버거만":
            p=p+8400
            st.write('선택됨!')

        if lott_hanm =="한우 세트":
            p=p+10200
            st.write('선택됨!')

    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')
        
    
        

if store == '맘스터치':
    st.title("맘스터치")
    b = st.checkbox("b")
    if b:
        st.write("선택됨!")

# btn = st.button("D 페이지로 이동")

# if btn:
#     st.switch_page("./page/d.py")