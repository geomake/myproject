import streamlit as st

st.set_page_config(
    page_title="배달 사이트",
    page_icon="🛵"
)

pages = {
    "홈" : [
        st.Page("./pages/home1.py", title="로그인"),
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