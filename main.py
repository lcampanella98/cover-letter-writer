from backend.core import run_llm
import streamlit as st

from streamlit_chat import message

KEY_FORM_STATE = 'form_state'
STATE_INIT_INFO = 1
STATE_CHATTING = 2

st.header("Cover Letter Writer")

def get_form_state():
    return st.session_state[KEY_FORM_STATE]

def set_form_state(new_state):
    st.session_state['form_state'] = new_state

def init_form_state():
    # initialize form state
    if KEY_FORM_STATE not in st.session_state:
        state = STATE_INIT_INFO
        set_form_state(state)

init_form_state()
state = get_form_state()

def create_cover_letter():
    with st.spinner("Generating cover letter..."):
        set_form_state(STATE_CHATTING)
        result = run_llm(text_role, text_resume)
        st.session_state['cover_letter'] = result
    
def reset():
    set_form_state(STATE_INIT_INFO)
    del st.session_state['cover_letter']

if state == STATE_INIT_INFO:
    
    # get and set the resume text
    text_resume = ''
    if 'resume' in st.session_state:
        text_resume = st.session_state['resume']
    text_resume = st.text_area('Your Resume (Remembered):', value=text_resume)
    st.session_state['resume'] = text_resume

    text_role = st.text_area('Role Description:')
    st.button('Create Cover Letter', on_click=create_cover_letter)
elif state == STATE_CHATTING:
    if 'cover_letter' in st.session_state:
        st.markdown(st.session_state['cover_letter'])
    st.button('Reset & Create Another', on_click=reset)
