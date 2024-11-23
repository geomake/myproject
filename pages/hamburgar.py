import streamlit as st

p=0
store = st.sidebar.selectbox("store",['main','롯데리아','맘스터치'])

if store == 'main':
    st.title("햄버거 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

    st.image('./img/1214.png')
    st.write("패티를 구운 후 다양한 부재료와 함께 빵 사이에 끼워 먹는 음식이다. 전 세계에서 가장 유명한 미국 요리이자 세계화의 바이블급 인지도를 자랑하는 넘버원 패스트푸드로, 세계로 퍼지는 과정에서 각종 문화가 뒤섞이다 보니 이것을 바탕으로 만든 온갖 배리에이션 음식들이 등장했다. 때문에 어원과는 무관하게 햄버거처럼 만든 겹빵 음식이라는 의미인 버거(burger)라는 접미형 신조어도 만들어냈을 정도. 이러한 접미 방식이 처음으로 사용된 음식은 치즈버거라고 한다.")
    st.write("")
    st.write("")
    st.write("------------------------------")

if store == '롯데리아':
    st.title("롯데리아")
    lott_bul = st.checkbox("불고기버거")
    lott_shi = st.checkbox("새우버거")
    lott_han = st.checkbox("한우버거")


#롯데리아 불고기
    if lott_bul:
        lott_bulm = st.radio('선택',["불고기 버거만"
                                      ,"불고기 세트",])
        st.write("단품:4700원 / 세트:6900원")
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
        st.write("단품:4700원 / 세트:6900원")
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
        st.write("단품:8400원 / 세트:10200원")
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

    #버거
    ham1 = st.checkbox("싸이버거")
    if ham1:
        ham11 = st.radio('선택',["싸이 버거만"
                                      ,"싸이버거 세트",])
        st.write("단품:4600원 / 세트:6900원")
        if ham11 =="싸이 버거만":
            p=p+4600
            st.write('선택됨!')

        if ham11 =="싸이버거 세트":
            p=p+6900
            st.write('선택됨!')
    
    ham2 = st.checkbox("딥치즈싸이버거")
    if ham2:
        ham22 = st.radio('선택',["딥치즈 싸이버거만"
                                      ,"딥치즈 싸이버거 세트",])
        st.write("단품:5100원 / 세트:7400원")
        if ham22 =="딥치즈 싸이버거만":
            p=p+5100
            st.write('선택됨!')

        if ham22 =="딥치즈 싸이버거 세트":
            p=p+7400
            st.write('선택됨!')

    ham3 = st.checkbox("언빌리버블버거")
    if ham3:
        ham33 = st.radio('선택',["언빌리버블버거만"
                                      ,"언빌리버블싸이버거 세트",])
        st.write("단품:6200원 / 세트:8500원")
        if ham33 =="언빌리버블버거만":
            p=p+6200
            st.write('선택됨!')

        if ham33 =="언빌리버블싸이버거 세트":
            p=p+8500
            st.write('선택됨!')

    #치킨
    chi1 = st.checkbox("후라이드치킨")
    if chi1:
        chi11 = st.radio('선택',["반마리"
                                      ,"한마리",])
        st.write("반마리:9400원 / 한마리:16900원")
        if chi11 =="반마리":
            p=p+9400
            st.write('선택됨!')

        if chi11 =="한마리":
            p=p+16900
            st.write('선택됨!')

    chi2 = st.checkbox("맘스양념치킨")
    if chi2:
        chi22 = st.radio('선택',["반마리"
                                      ,"한마리",])
        st.write("반마리:10400원 / 한마리:18900원")
        if chi22 =="반마리":
            p=p+10400
            st.write('선택됨!')

        if chi22 =="한마리":
            p=p+18900
            st.write('선택됨!')

    btn = st.button("주문하기")
    if btn:
        st.write(p,'원 입니다.')
        
        

# btn = st.button("D 페이지로 이동")

# if btn:
#     st.switch_page("./page/d.py")