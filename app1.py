import streamlit as st
#Page Configuration
st.set_page_config(page_title="Agent Builder",layout="wide")
st.title("The Agent configuration Panel")
st.write("Design your Ai person before launching the chat")
#The SideBar
with st.sidebar:
  st.header("security and setting")
  api_key=st.text_input("Groq API Key:",type="password")
  temperature=st.slider("Creativity(Temperature):",min_value=0.0,max_value=10.0,value=0.2)
  st.info("The Slidebar is great for settings that shouldn't clutter the main screen")
#Columns
col1,col2=st.columns(2)
with col1:
  st.subheader("Agent Identity")
  agent_name=st.text_input("Name your Agent:",value="DataBot")
  agent_role=st.selectbox("Select Agent Role:",["Data Analyst","Copywriter","Python","Tutor"])
with col2:
  st.subheader("Agent Behavior")
  system_instructions=st.text_area("Custom System Instructions:",height=110,placeholder="Eg Always answer in bullet points...")
st.write("---")
st.write("PREVIEW TOUR CONGIFURATION")
if agent_name:
 st.success(f"**{agent_name}** is ready to be deployed as a **{agent_role}**.")
#Prompt
st.code(f"""
System Prompt:
You are {agent_name},an expert {agent_role},
You creativity level is set to {temperature},
Additional Instructions :{system_instructions}
                 """,language="text")

