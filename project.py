import streamlit as st

pages = {
    "홈" : [
        st.Page("./pages/home.py", title="홈")
    ],
    "음식" : [
        st.Page("./pages/chicken.py", title="치킨"),
        st.Page("./pages/chinese.py", title="중식"),
        st.Page("./pages/hamburgar.py", title="햄버거"),
        st.Page("./pages/pizza.py", title="피자"),
    ]
}
pg = st.navigation(pages)
pg.run()