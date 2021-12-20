import streamlit as st

# Initialise Session Sate
if "value_two" not in st.session_state:
    st.session_state["value_two"]=20

# for navigation
select=st.sidebar.radio(label="",options=["Setting responsive","Setting persistent","Settings the rigth way"])

if select=="Setting responsive":
    st.info("""
    If you switch to the another settings (or a page in multipage apps) and back, all the input will be restored to constant default value.
     """)

    st.code('''st.number_input(label="Setting One",value=20,key="Key One")''')

    st.session_state["value_one"]=st.number_input(label="Setting One",value=20,key="Key One")

if select == "Setting persistent":
    st.info("""
        Those settings get the default value from the session state, and the setting will remain after changeint the page.
        But try changeing the same value multiple times in sucession. You will notice it changes only every other time""")

    st.code('''st.session_state["value_two"]=st.number_input(label="Setting Two",value=st.session_state["value_two"],key= "Key Two")''')
    st.session_state["value_two"]=st.number_input(label="Setting Two",value=st.session_state["value_two"],key= "Key Two")

def callback():
    pass

if select == "Settings the rigth way":

    value="value_three"
    default_value=20
    key="key three"

    st.info("This has now the behaviour as you would expect.")

    st.code('''    if value not in st.session_state:
        st.session_state[value]=default_value

    def update_value(value,key):
        st.session_state[value] = st.session_state[key]

    if key not in st.session_state:
        st.number_input(label="Setting Three", value=st.session_state[value], key=key)
    else:
        st.number_input(label="Setting Three", on_change=update_value(value,key) ,value=st.session_state[value],key=key)''')

    if value not in st.session_state:
        st.session_state[value]=default_value

    def update_value(value,key):
        st.session_state[value] = st.session_state[key]

    if key not in st.session_state:
        st.number_input(label="Setting Three", value=st.session_state[value], key=key)
    else:
        st.number_input(label="Setting Three", on_change=update_value(value,key) ,value=st.session_state[value],key=key)


st.session_state


