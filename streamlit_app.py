import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Colorful Sales Dashboard", layout="wide")

# Custom CSS with vibrant colors
st.markdown("""
<style>
    .reportview-container {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
    }
    .big-font {
        font-size: 36px !important;
        font-weight: bold;
        color: #FF6B6B;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .stSelectbox > div > div {
        background-color: #ffffff;
        border-radius: 10px;
        border: 2px solid #FF6B6B;
    }
    .stDateInput > div > div > input {
        background-color: #ffffff;
        border-radius: 10px;
        border: 2px solid #FF6B6B;
    }
    .stButton>button {
        background-color: #FF6B6B;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stTab {
        background-color: #4ECDC4;
        color: white;
        border-radius: 5px 5px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# Title with colorful background
st.markdown('<div style="background-color: #FFD93D; padding: 20px; border-radius: 15px;"><p class="big-font">แสดงผลการรุกล้ำ</p></div>', unsafe_allow_html=True)

# Tabs with custom styling
tab1, tab2 = st.tabs(["🏠 อยู่มุมขวาบน", "📅 อยู่มุมขวาเดือน/ปี"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        start_date = st.date_input("เลือกวันที่", value=datetime(2024, 4, 5))
    with col2:
        time_range = st.selectbox("เลือกช่วงเวลา", ["เลือกช่วงเวลา", "ช่วงเวลาอื่นๆ"])

    col3, col4 = st.columns(2)
    
    with col3:
        selected_date = st.date_input("เลือกวัน", value=datetime(2024, 4, 5))
    with col4:
        end_time = st.selectbox("เลือกช่วงเวลาที่สุด", ["ไม่มี"])

# Generate sample data
dates = pd.date_range(start=start_date, periods=24, freq='H')
sales = [0] * 13 + [2, 4, 7, 19, 3, 7, 2] + [0] * 4
df = pd.DataFrame({'time': dates, 'sales': sales})

# Create the bar chart using Plotly with a vibrant color scheme
fig = px.bar(df, x='time', y='sales', title=f'แสดงจำนวนการรุกล้ำของวันที่ {start_date.strftime("%Y-%m-%d")}')
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#333333', size=14),
    title_font_size=24,
    title_font_color='#FF6B6B',
    xaxis=dict(title='Time', gridcolor='#DDDDDD', tickfont=dict(size=12)),
    yaxis=dict(title='Count', gridcolor='#DDDDDD', tickfont=dict(size=12)),
)
fig.update_traces(marker_color='#6C5CE7', marker_line_color='#FF6B6B', marker_line_width=1.5, opacity=0.8)

# Display the chart with a border
st.markdown('<div style="border: 3px solid #FF6B6B; border-radius: 15px; padding: 10px; background-color: white;">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Download button with custom styling
st.markdown('<div style="display: flex; justify-content: center; margin-top: 20px;">', unsafe_allow_html=True)
st.download_button("📥 ดาวน์โหลด ประวัติการรุกล้ำ", data="Sample data", file_name="sales_data.csv")
st.markdown('</div>', unsafe_allow_html=True)

# Pagination with custom styling
col5, col6, col7 = st.columns([1, 1, 1])
with col6:
    st.markdown('<div style="background-color: #4ECDC4; padding: 10px; border-radius: 10px; text-align: center; color: white; font-weight: bold;">1/2</div>', unsafe_allow_html=True)