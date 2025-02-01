import streamlit as st

# パスワードの設定
password = st.text_input("パスワードを入力してください:", type="password")

# 正しいパスワード
correct_password = "知るか"  # ここに自分が決めたパスワードを入れてね

# パスワードが正しいかチェック
if password == correct_password:
    # タイトル
    st.title("自己紹介")

    # 自己紹介の内容
    st.write("名前: 酒井優音")
    st.write("年齢: 12歳")
    st.write("趣味: ゲーム")
    st.write("好きな食べ物: 米")
    st.write("将来の夢: まだ決まっていない")
else:
    st.write("パスワードが間違っています。再度入力してください。")