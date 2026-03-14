import streamlit as st
from dotenv import load_dotenv
from langchain_community.cache import SQLiteCache
from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

set_llm_cache(InMemoryCache(maxsize=16))
content= input('请输入：')
set_llm_cache(SQLiteCache('cache.dbb'))

load_dotenv()

llm=ChatOpenAI(
    base_url='https://api.deepseek.com',
    model='deepseek-chat',
    temperature=0.2,
    max_tokens=1024,
)

prompt =ChatPromptTemplate.from_messages([
    ('system','你是一个专业的翻译助手，擅长给出信达雅的翻译。'),
    ('user','请将下面的内容翻译成{language}:\n{content}')
])

chain= prompt | llm

languages=['英语','日语','德语','法语']
st.write('##多语言翻译助手')

sentence=st.text_input(label='请输入要翻译的句子：')
targets= st.multiselect(label='请选择目标语言：',options=languages,placeholder='')
button=st.button(label='确定',type='primary')
if button and sentence.strip() and targets:
    for target in targets:
        message= chain.invoke({'target':target,'sentence':sentence})
        st.write(f'{target}:{message.content}')
    else:
        st.info('请输入要翻译的句子并选择目标语言！！')





