import streamlit as st
from crewai import Agent, Task, LLM, Crew

def translate_to_asturian(text):
    modelo = LLM(
        model="groq/gemma2-9b-it",
        temperature=0.5,
        base_url="https://api.groq.com/openai/v1",
        api_key="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"
    )

    translator_agent = Agent(
        role="Yes un chatbot d'intelixencia artificial n'asturianu llamau Ayia",
        goal="Respondes cualquier pregunta n'asturianu",
        backstory="Yes una ia que fala asturianu",
        llm=modelo
    )

    traductor = Task(
        description=f"Respondes a la siguiente pregunta n'asturianu: {text}",  
        expected_output="Respuestes en correctu asturianu",
        agent=translator_agent
    )

    crew = Crew(
        tasks=[traductor],
        verbose=True
    )

    result = crew.kickoff()
    return result.raw

# Configurar la aplicación Streamlit
st.set_page_config(page_title="Ayia - IA n'asturianu", layout="centered")

st.markdown("""
    <style>
        .chat-bubble {
            padding: 10px;
            border-radius: 15px;
            margin: 5px;
            max-width: 80%;
            display: inline-block;
        }
        .user-bubble {
            background-color: #0078ff;
            color: white;
            align-self: flex-end;
        }
        .ai-bubble {
            background-color: #e5e5ea;
            color: black;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
    </style>
    """, unsafe_allow_html=True)

st.title("Ayia")
col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", width=40)
st.write("L'intelixencia artificial n'asturianu")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    bubble_class = "user-bubble" if message["role"] == "user" else "ai-bubble"
    st.markdown(f'<div class="chat-bubble {bubble_class}">{message["text"]}</div>', unsafe_allow_html=True)

user_input = st.text_input("Escribi equí la to pregunta…", key="user_input")

if st.button("Preguntar") and user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    response = translate_to_asturian(user_input)
    st.session_state.messages.append({"role": "ai", "text": response})
    st.rerun()

st.markdown("""
    <footer style="text-align: center; margin-top: 50px;">
        <p>Un software d'Ayalga</p> 
    </footer>
    """, unsafe_allow_html=True)

