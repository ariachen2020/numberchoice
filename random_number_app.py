import streamlit as st
import random

# 設置頁面標題和配置
st.set_page_config(
    page_title="隨機數字抽取器",
    page_icon="🎲",
    layout="centered"
)

# 初始化 session state
if 'drawn_numbers' not in st.session_state:
    st.session_state.drawn_numbers = []

# 頁面標題
st.title("🎲 隨機數字抽取器")

# 設定區域
st.subheader("設定")
col1, col2 = st.columns(2)

with col1:
    min_num = st.number_input("最小值", value=1)
with col2:
    max_num = st.number_input("最大值", value=100)

allow_duplicate = st.checkbox("允許重複抽取", value=False)

# 驗證輸入
if min_num >= max_num:
    st.error("最小值必須小於最大值！")
    st.stop()

# 抽取按鈕
if st.button("抽取數字"):
    if not allow_duplicate and len(st.session_state.drawn_numbers) >= (max_num - min_num + 1):
        st.error("所有數字都已被抽取完畢！")
    else:
        while True:
            new_number = random.randint(min_num, max_num)
            if allow_duplicate or new_number not in st.session_state.drawn_numbers:
                st.session_state.drawn_numbers.append(new_number)
                break

# 顯示結果
if st.session_state.drawn_numbers:
    st.subheader("抽取結果")
    
    # 使用列表推導式創建每行3個數字的分組
    rows = [st.session_state.drawn_numbers[i:i+3] for i in range(0, len(st.session_state.drawn_numbers), 3)]
    
    # 顯示數字
    for row in rows:
        cols = st.columns(3)
        for idx, num in enumerate(row):
            with cols[idx]:
                st.markdown(f"<h2 style='text-align: center;'>{num}</h2>", unsafe_allow_html=True)

# 重置按鈕
if st.button("重置"):
    st.session_state.drawn_numbers = []
    st.rerun() 