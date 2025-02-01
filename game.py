import streamlit as st
import random

st.title("日本語単語パズルゲーム")

# 日本語の単語リスト
words = ["さくら", "りんご", "みかん", "とうきょう", "ふじさん"]

# ゲームの初期設定
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)

# シャッフルされた文字を生成
shuffled_word = ''.join(random.sample(st.session_state.word, len(st.session_state.word)))
st.write("シャッフルされた文字:", shuffled_word)

# プレイヤーの回答を受け取る
user_answer = st.text_input("正しい単語を入力してください:")

# 回答を確認するボタン
if st.button("確認"):
    if user_answer == st.session_state.word:
        st.write("正解です！")
        words.remove(st.session_state.word)
        if words:
            st.session_state.word = random.choice(words)
        else:
            st.write("ゲームクリア！全ての単語を解きました。")
            st.session_state.word = None
    else:
        st.write("不正解です。もう一度試してください。")

# リセットボタン
if st.button("リセット"):
    st.session_state.word = random.choice(words)
    st.write("ゲームがリセットされました。")
