import streamlit as st
from chatbot_graph import *


#设置网页的标题
st.set_page_config(
    page_title="农业咨询",
    layout="wide",
)
#设置标题
st.title("智能农业问答系统展示")





#传递问题,得到问答机器人的回复
def communicate(question):
    chatbot=Chatbotgraph()
    
    response=chatbot.chat_main(question)
    return response


#页面接收用户问题,将问答机器人的回复返回给用户
if openon_input:=st.text_input(""):
    #在页面显示用户的输入
    st.markdown(openon_input)
    
    #得到模型生成的回复
    response=communicate(openon_input)
    

    #将用户输入加入历史
    

    #在页面上显示模型生成的回复
    st.markdown(response)




