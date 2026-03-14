import time

from click import prompt
from dotenv import load_dotenv
from langchain_community.cache import SQLiteCache
from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI



content=input('请输入：')

set_llm_cache(SQLiteCache('cache.dbb'))

load_dotenv()

llm=ChatOpenAI(
    base_url='https://api.deepseek.com',
    model='deepseek-chat',
    temperature=0.2,
    max_tokens=1024,
)

prompt = ChatPromptTemplate.from_messages([
    ('system','你是一个专业的翻译助手，擅长给出信达雅的翻译。'),
    ('user','请将下面的内容翻译成{language}:\n{content}')
])

chain= prompt | llm

for language in ['英语','日语','德语','法语']:
    msg=chain.invoke({'language':language,'content':content})
    print(f'{language}:{msg.content}')



