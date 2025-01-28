import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate 

model_name = "deepseek-r1:1.5b"

model = ChatOllama(model=model_name, base_url="http://localhost:11434")

system_message = SystemMessagePromptTemplate.from_template("Contoh : Kamu adalah seorang penulis hebat yang sudah berpengalaman selama lebih dari 10 tahun.")

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

with st.form("llm-form"):
    text = st.text_area("Masukkan pertanyaan Anda di sini.")
    submit = st.form_submit_button("Kirim")

def generate_response(chat_history):
    chat_template = ChatPromptTemplate.from_messages(chat_history)
    chain = chat_template | model | StrOutputParser()
    response = chain.invoke({})
    return response

def get_history():
    chat_history = [system_message]
    for chat in st.session_state['chat_history']:
        prompt = HumanMessagePromptTemplate.from_template(chat['user'])
        chat_history.append(prompt)

        ai_message = AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.append(ai_message)

    return chat_history

if submit and text:
    with st.spinner("Membuat respons..."):
        prompt = HumanMessagePromptTemplate.from_template(text)
        chat_history = get_history()
        chat_history.append(prompt)

        response = generate_response(chat_history)

        st.session_state['chat_history'].append({'user': text, 'assistant': response})

        st.write(f"**:adult: Pengguna**: {text}")
        st.write(f"**:brain: Asisten**: {response}")
        st.write("---")

st.write('## Riwayat Chat')
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**:adult: Pengguna**: {chat['user']}")
    st.write(f"**:brain: Asisten**: {chat['assistant']}")
    st.write("---")