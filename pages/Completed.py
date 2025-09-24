import streamlit as st
from files.functions import (
    setup, get_todos,get_completed,
    clear_completed as clear_completed_logic, 
    delete_completed as delete_completed_logic,
    reverse_completed as reverse_completed_logic
    )
import time


st.set_page_config(layout="centered")
todos_path,completed_path = setup()
time_stamp = [time.strftime("%b %d, %Y - (%H:%M:%S)")]


todos = get_todos(todos_path)
completed = get_completed(completed_path)
app_completed = completed[1::2]
completed_indexes = []

if "completed_message" not in st.session_state:
    st.session_state["completed_message"] = ""


def handle_reverse_completed():
    completed_message = reverse_completed_logic(todos,completed,completed_indexes,time_stamp)
    st.session_state["completed_message"] = completed_message


def handle_delete_complete():
    completed_message = delete_completed_logic(completed_path,completed,completed_indexes)
    st.session_state["completed_message"] = completed_message


def handle_clear_completed():
    completed_message = clear_completed_logic(completed_path)
    st.session_state["completed_message"] = completed_message

st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem !important;
    }
""", unsafe_allow_html=True)
try:
    st.write("")

    st.title("My Todo App")

    column1,column2,column3,column4 = st.columns([1.1,1,1,5])

    with column1:
        st.button("Reverse", on_click=handle_reverse_completed)

    with column2:
        st.button("Delete", on_click=handle_delete_complete)

    with column3:
        st.button("Clear", on_click=handle_clear_completed)

    with column4:
        st.write(st.session_state["completed_message"])

    st.subheader("Your completed to-dos")

    for i,item in enumerate(app_completed):
        if st.checkbox(item, key = f"{i}-{item.strip()}"):
            try:
                actual_completed_index = 2*int(i)+1
                actual_completed_item = i
                completed_indexes.append(actual_completed_index)
            except Exception as e:
                print(e)
            
except Exception as e:
    print("an error occured")
    print (e)

