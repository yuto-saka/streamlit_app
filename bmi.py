import streamlit as st

# タイトル
st.title("BMI計算機")

# 身長入力 (cm)
height = st.number_input("身長 (cm)", min_value=0.0, format="%.2f")

# 体重入力 (kg)
weight = st.number_input("体重 (kg)", min_value=0.0, format="%.2f")

if height > 0 and weight > 0:
    # 身長をメートルに変換
    height_m = height / 100
    # BMI計算
    bmi = weight / (height_m ** 2)
    # 結果表示
    st.write(f"あなたのBMIは: {bmi:.2f}")

    # BMIの範囲とアドバイス
    if bmi < 18.5:
        st.write("BMIが18.5未満: こんにちはガリガリ君。バランスの良い食事を心掛けましょう。")
        png_image_path = "garigari.png"  # ここに実際のPNG画像のファイル名を入力してください
        st.image(png_image_path, caption="やせすぎ")
    elif 18.5 <= bmi < 24.9:
        st.write("BMIが18.5〜24.9: 平均よりは太ってますね。健康を維持するためにバランスの良い食事と運動を続けましょう。")
    elif 25.0 <= bmi < 29.9:
        st.write("BMIが25.0〜29.9: でぶですね。健康的な体重を目指してバランスの良い食事と運動を心掛けましょう。")
    else:
        st.write("BMIが30.0以上: デブすぎｗ。")
else:
    st.write("身長と体重を入力してください。")
