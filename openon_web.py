import streamlit as st
from chatbot_graph import *


#设置网页的标题
st.set_page_config(
    page_title="农业咨询",
    layout="wide",
)
#设置标题
st.title("智能农业问答系统展示")

#设置左侧框
with st.sidebar:
    st.text("本问答系统基于自主构建的农业中文知识图谱,可以回复用户关于农业种植基础知识的问题,如种植方法、农作物适宜Ph值等")
    #编写示例
    with st.expander("查看问题示例"):
        st.text("1.芥菜的种植方法")
        st.text("2.芥菜的别名有哪些")
        st.text("3.芥的开花时间")





#传递问题,得到问答机器人的回复
def communicate(question):
    chatbot=Chatbotgraph()
    response=chatbot.chat_main(question)
    return response


#页面接收用户问题,将问答机器人的回复返回给用户
if openon_input:=st.text_input(""):
    #在页面显示用户的输入
    # st.write()
    st.markdown("User:    "+openon_input)
    
    #得到模型生成的回复
    response=communicate(openon_input)

    #将用户输入加入历史
    

    #在页面上显示模型生成的回复
    st.markdown("Assistant:    "+response)

    



