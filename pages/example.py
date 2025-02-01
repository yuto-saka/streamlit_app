import streamlit as st

# クイズの問題と回答を設定
questions = [
    {"question": "地球の最も高い山は何ですか？", "options": ["エベレスト", "キリマンジャロ", "マッキンリー"], "answer": "エベレスト"},
    {"question": "太陽系で最も大きな惑星は？", "options": ["木星", "土星", "海王星"], "answer": "木星"},
    {"question": "最も早い動物は何ですか？", "options": ["チーター", "鷹", "イルカ"], "answer": "チーター"},
]

st.title("1人プレイ用 クイズゲーム")

# スコアを初期化
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# クイズの質問を表示
current_question = questions[st.session_state.question_index]
st.write(current_question["question"])

# 選択肢を表示
user_answer = st.radio("選択肢を選んでください", current_question["options"])

# 「次へ」ボタンをクリックで回答をチェック
if st.button("次へ"):
    if user_answer == current_question["answer"]:
        st.session_state.score += 1
        st.write("正解です！")
    else:
        st.write("不正解です。正しい答えは", current_question["answer"], "です。")

    st.session_state.question_index += 1

    # 全ての質問が終わったらスコアを表示
    if st.session_state.question_index >= len(questions):
        st.write("クイズ終了！あなたのスコアは", st.session_state.score, "点です。")
        st.session_state.question_index = 0
        st.session_state.score = 0
    else:
        current_question = questions[st.session_state.question_index]

# リセットボタン
if st.button("リセット"):
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.write("ゲームがリセットされました。")
