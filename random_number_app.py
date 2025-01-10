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
    st.session_state.min_num = 1  # 保存最小值
    st.session_state.max_num = 100  # 保存最大值
    st.session_state.allow_duplicate = False  # 保存重複設置

# 頁面標題
st.title("🎲 隨機數字抽取器")

# 顯示結果區域
if st.session_state.drawn_numbers:
    st.subheader("抽取結果")
    
    # 使用列表推導式創建每行5個數字的分組
    rows = [st.session_state.drawn_numbers[i:i+5] for i in range(0, len(st.session_state.drawn_numbers), 5)]
    
    # 顯示數字
    for row in rows:
        cols = st.columns(5)
        for idx, num in enumerate(row):
            with cols[idx]:
                st.markdown(f"<h2 style='text-align: center;'>{num}</h2>", unsafe_allow_html=True)

# 操作區域
col_action1, col_action2 = st.columns([1, 1])
with col_action1:
    if st.button("抽取數字"):
        # 從 session state 獲取當前設置
        allow_duplicate = st.session_state.allow_duplicate
        min_num = st.session_state.min_num
        max_num = st.session_state.max_num
        
        if not allow_duplicate and len(st.session_state.drawn_numbers) >= (max_num - min_num + 1):
            st.error("所有數字都已被抽取完畢！")
        else:
            with st.spinner('抽取中...'):
                while True:
                    new_number = random.randint(min_num, max_num)
                    if allow_duplicate or new_number not in st.session_state.drawn_numbers:
                        st.session_state.drawn_numbers.append(new_number)
                        break

with col_action2:
    if st.button("重置"):
        st.session_state.drawn_numbers = []
        st.rerun()

# 設定區域
st.subheader("設定")
col1, col2 = st.columns(2)

with col1:
    min_num = st.number_input("最小值", value=st.session_state.min_num)
    st.session_state.min_num = min_num
with col2:
    max_num = st.number_input("最大值", value=st.session_state.max_num)
    st.session_state.max_num = max_num

allow_duplicate = st.checkbox("允許重複抽取", value=st.session_state.allow_duplicate)
st.session_state.allow_duplicate = allow_duplicate

# 驗證輸入
if min_num >= max_num:
    st.error("最小值必須小於最大值！")
    st.stop() 