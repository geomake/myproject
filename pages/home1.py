import streamlit as st
import sqlite3


menu = st.sidebar.selectbox("MENU",['로그인','회원가입','회원정보 수정','탈퇴'])

if menu == '로그인':
    #데이터 베이스 연결
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    #cursor.execute("SELECT * FROM user")

    st.title("로그인")
    id = st.text_input('아이디')
    pw = st.text_input('비번',type='password')
    btn = st.button('로그인')

    if btn:
        cursor.execute(f"SELECT * FROM user WHERE username='{id}'")
        row = cursor.fetchone()
        if row:
            db_id = row[1]
            db_pw = row[2]
        else:
            db_id = ''
            db_pw = ''
        if db_pw == pw:
            st.sidebar.write(f"{id}님 환영합니다")
            st.session_state.money = int(row[4]) 
            st.session_state.id = id
        else:
            st.error("로그인 실패")

 
elif menu =='회원가입':
    #데이터 베이스 연결
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    st.title('회원가입')
    id = st.text_input('아이디')
    pw = st.text_input('비번',type='password')
    pw_2 = st.text_input('비번확인',type='password')
    address = st.text_input('주소')
    btn2 = st.button('회원가입')
    if btn2:
        if pw == pw_2:
            sql=f"""
insert into user(username,password,address,money)values('{id}','{pw}','{address}','50000')"""
            cursor.execute(sql)
            conn.commit()
            st.success('회원가입 성공!')
        else:
            st.error('비밀번호를 다시 확인해 주세요')
    conn.close()

elif menu =='회원정보 수정':
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        st.title("회원정보 수정")
        #아이디
        id = st.text_input("아이디")
        #비밀번호
        pw = st.text_input("비밀번호", type='password')    
        #이메일
        address = st.text_input("주소")
        #회원가입 버튼
        btn = st.button("수정")
        if btn:
            sql=f"""UPDATE user SET password ="{pw}",address="{address}" WHERE username = "{id}"
            """
            cursor.execute(sql)
            conn.commit()
            
elif menu =='탈퇴':
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    st.title("회원탈퇴")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("탈퇴")

    if btn:
        sql = f"""DELETE FROM user WHERE username="{id}"
        """
        cursor.execute(sql)
        conn.commit()