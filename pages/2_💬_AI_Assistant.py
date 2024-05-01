import streamlit as st
from config import pagesetup as ps, sessionstate as ss
import time
from openai import OpenAI



# Initialize session state as required
ss.initialize_sessionstate()

##### 0. PAGE SETUP #####
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
ps.master_page_display_styled_popmenu(varPageNumber=1)

client = OpenAI(api_key=st.secrets.openai.api_key)
assistantid = st.secrets.openai.assistant_id
thread = client.beta.threads.create()
threadid = thread.id


##### 1. Container SETUP #####
main_container = ps.container_styled2(varKey="main_container")
with main_container:
    backgroundcontainer = ps.container_styled3(varKey="afdad")
    with backgroundcontainer:
        chat_container = st.container(border=True, height=300)
        with chat_container:
            for message in st.session_state.display_messages:
                with st.chat_message(name=message['role']):
                    st.markdown(body=message['content'])

prompt = st.chat_input(placeholder="Type your request here...")
if prompt:
    st.session_state.display_messages.append({"role": "user", "content": prompt})
    with chat_container:
        with st.chat_message(name="user"):
            st.markdown(body=prompt)        

        runstatusbox = st.status(label="Initiating AlmyAI...", expanded=False, state="running")  # Proper use of st.status
        prompt_message = client.beta.threads.messages.create(thread_id=threadid, role="user", content=prompt)
        run = client.beta.threads.runs.create(thread_id=threadid, assistant_id=assistantid)
        while run.status != "completed":
            time.sleep(2)
            run = client.beta.threads.runs.retrieve(run_id=run.id, thread_id=threadid)
            runstatus = run.status
            if runstatus == "completed":
                runstatusbox.update(label="AlmyAI completed!", expanded=False, state="complete")
                messagelist = client.beta.threads.messages.list(thread_id=threadid)
                for msg in messagelist:
                    if msg.role == "assistant" and msg.run_id == run.id:
                        st.session_state.display_messages.append({"role": "assistant", "content": msg.content[0].text.value})
                        with st.chat_message(name="assistant"):
                            st.markdown(body=msg.content[0].text.value)
                break




