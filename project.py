import streamlit as st

pages = {
    "홈" : [
        st.Page("./pages/home1.py", title="로그인"),
        st.Page("./pages/home2.py", title="회원 정보")
    ],
    "음식" : [
        st.Page("./pages/bunsik.py", title="분식"),
        st.Page("./pages/chicken.py", title="치킨"),
        st.Page("./pages/hamburgar.py", title="햄버거"),
        st.Page("./pages/pizza.py", title="피자"),
    ]
}
pg = st.navigation(pages)
pg.run()