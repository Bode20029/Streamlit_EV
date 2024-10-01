import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background-color: #f0f2f6;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .stSelectbox > div > div {
        background-color: #ffffff;
    }
    .stDateInput > div > div > input {
        background-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="big-font">แสดงผลการรุกล้ำ</p>', unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["อยู่มุมขวาบน", "อยู่มุมขวาเดือน/ปี"])

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

# Create the bar chart using Plotly
fig = px.bar(df, x='time', y='sales', title=f'แสดงจำนวนการรุกล้ำของวันที่ {start_date.strftime("%Y-%m-%d")}')
fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(color='black'),
    xaxis=dict(title='Time'),
    yaxis=dict(title='Count')
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Download button
st.download_button("ดาวน์โหลด ประวัติการรุกล้ำ", data="Sample data", file_name="sales_data.csv")

# Pagination
col5, col6, col7 = st.columns([1, 1, 1])
with col6:
    st.markdown("1/2")