from groq import Groq
import streamlit as st






st.title("AGENTE DA MUSICA")


client = Groq(api_key = '')

print('------------------------------------------------------')
print()
pergunta = st.text_input('Digite sua pergunta...')
print()
print('------------------------------------------------------')
resposta = client.chat.completions.create(
model=  'openai/gpt-oss-120b',
messages=[
{
    "role":"system",
    'content':"Você é um Profissional em musica, voce é muito inteligente mas é ignorante e xinga todo mundo."
    
},
{

"role": "user",
"content":pergunta 

}    
]
)
st.write(resposta.choices[0].message.content)