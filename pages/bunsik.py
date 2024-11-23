import streamlit as st
import sqlite3 

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
p=0
store = st.sidebar.selectbox("store",['main','수미네 분식집','김밥천국'])

if store == 'main':
    st.title("분식 메뉴")
    st.write("")
    st.write("")
    st.write("오른쪽 하단의 박스를 클릭해서 메뉴를 선택하세요!")

    st.image('./img/1212.png')
    st.write("분식(粉食)의 본래 의미는 '가루로 만든 음식'이란 뜻으로, 특히 밀가루로 만든 음식을 지칭하는 말이다. ")
    st.write("")
    st.write("1960~70년대 혼분식 장려 운동 당시에 쌀의 소비를 줄이기 위해 밀가루의 사용을 적극 권장했고, 이 과정에서 '분식'이라는 단어가 생겼다. 이것이 지금은 떡볶이나 라면 등 원 의미에 해당하는 분식은 물론, 그렇지 않은 김밥, 순대 등 간단한 음식 또는 길거리 음식을 포함하는 단어로 뜻이 변했다. 따라서 오늘날의 분식은 경양식 등과도 일부 범주가 겹친다.")
    st.write("")
    st.write("일본어로는 코나모노(粉物)라고 한다. 중국에서는 면식(麵食)이라고 하는데, 중국에서는 쌀가루로 만든 면을 분(粉), 밀가루로 만든 것을 면(麵)이라고 표현한다. 영어로는 'Snack bar' 라고 한다.")
    st.write("")
    st.write("분식의 반대말은 입식(粒食)이다. 즉, 쌀이나 보리 등의 곡물을 원형 그대로 익혀낸 음식을 말한다. 그래서 분식집에 파는 김밥, 오므라이스 등은 원래는 분식이 아닌 입식이다.")
    st.write("")
    st.write("------------------------------")

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
        st.session_state.money = st.session_state.money - p
        sql=f"""UPDATE user SET money ="{st.session_state.money}" WHERE username = "{st.session_state.id}"
            """
        cursor.execute(sql)
        conn.commit()

