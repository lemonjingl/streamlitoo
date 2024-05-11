#streamlit run ./get_vis.py
import streamlit as st 
import pandas as pd
import numpy as np


D = pd.read_excel('./result.xlsx')
D2 = pd.read_excel('./save_data.xlsx')
def read(data):
    l=[]
    for i in range(1,6):
        count = data.iloc[:,i].value_counts()
        count = pd.DataFrame(count.sort_index())
        count.columns = ['个数']
        count.index.name = '分数' 
        l.append(count)
    return l

l=read(D)
# 设置全局属性
st.set_page_config(
    page_title='竞赛论文自动评阅',
    page_icon=' ',
    layout='wide'
)

def page2(D_index1,D_index2,l_index):
    st.markdown('数据 :')  
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("综合评分:")
        st.write(D_index1)
    with right_column:
        st.subheader("完整性、实质性、摘要、写作水平评分:")
        st.write(D_index2)
    st.markdown('综合评分图示')    		 
    st.bar_chart(l_index)
    
    

app_mode = st.sidebar.selectbox('Select Page',['各项指标展示','论文评分'])
if app_mode == '各项指标展示':
    st.header('指标展示')
    st.image('./图/线条小狗2.jpg')     
    st.sidebar.header("指标选择:")  
    zb=st.sidebar.radio('指标',options=["传统指标","摘要指标","完整性指标","实质性指标","写作水平指标"])
    if zb == "传统指标":
        st.subheader('传统指标展示:') 
        st.markdown('数据 :')      
        st.write(D2.iloc[:,:7])  
    elif zb == "摘要指标":
        st.subheader('摘要指标展示:') 
        st.markdown('数据 :')      
        st.write(D2.iloc[:,[0,7,8]]) 
    elif zb == "完整性指标":
        st.subheader('完整性指标展示:') 
        st.markdown('数据 :')      
        st.write(D2.iloc[:,[0,9,10,11]]) 
    elif zb == "实质性指标":
        st.subheader('实质性指标展示:') 
        st.markdown('数据 :')      
        st.write(D2.iloc[:,[0,12,13,14]]) 
    else :
        st.subheader('写作水平指标展示:') 
        st.markdown('数据 :')      
        st.write(D2.iloc[:,:]) 
        
        
elif app_mode=='论文评分':         
    st.header('论文评分')
    st.sidebar.header("分数段选择:")  
    score=st.sidebar.radio('综合分数',options=["0~10","0~3","4~6","7~10"])
    if score == "0~10":
        st.image('./图/线条小狗1.jpg')    
        st.subheader('0~10分:') 
        st.markdown('数据 :')       
        st.write(D)
        st.markdown('综合评分图示')    		 
        st.bar_chart(l[4]) 
    elif score == "0~3":
        st.image('./图/2.png')
        st.subheader('0~3分:') 
        page2(D.iloc[381:,[0,-1]],D.iloc[381:,:-1],l[4][:4])
        
    elif score == "4~6":
        st.image('./图/1.png')
        st.subheader('4~6分:') 
        page2(D.iloc[13:381,[0,-1]],D.iloc[13:381,:-1],l[4][4:7])
    else:
        st.image('./图/3.png')
        st.subheader('7~10分:') 
        page2(D.iloc[:12,[0,-1]],D.iloc[:12,:-1],l[4][7:])

    
    
    
    
    
    