import streamlit as st
from files.functions import setup, get_todos, add_todos,edit_todos,get_completed, complete_todos,delete_todos,clear_todos,delete_completed
import time


st.set_page_config(layout="centered")
todos_path,completed_path = setup()
time_stamp = [time.strftime("%b %d, %Y - (%H:%M:%S)")]
todos = get_todos(todos_path)
completed = get_completed(completed_path)
app_todos = todos[1::2]
app_completed = completed[1::2]
indexes = []
index = None


if "message" not in st.session_state:
    st.session_state["message"] = "Welcome"
def get_index():
    try:
        index = indexes[0]
        return index
    except IndexError:
        index = None
        return index

def add_todo():
    global area
    to_add = st.session_state["new_todo"]
    message,area = add_todos(todos,app_todos,to_add,time_stamp)
    st.session_state["new_todo"] = area
    st.session_state["message"] = message


def edit_todo():
    global area
    index = get_index()
    todo = st.session_state["new_todo"]
    message,area = edit_todos(todo,todos,app_todos,index,indexes,time_stamp)
    st.session_state["new_todo"] = area
    st.session_state["message"] = message


def complete_todo():
    message = complete_todos(todos,completed,indexes,time_stamp)
    st.session_state["message"] = message


def delete_todo():
    message = delete_todos(todos,indexes)
    st.session_state["message"] = message


def clear_todo():
    message = clear_todos(todos_path)
    st.session_state["message"] = message

st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem !important;
    }
""", unsafe_allow_html=True)
try:
    st.write("")

    st.title("My Todo App")

    st.text_input(label = "Input a todo",placeholder = "Please enter a todo here...", key = "new_todo")

    column1,column2,column3,column4,column5,column6 = st.columns([0.8,0.8,1.3,1,1,3.5])

    with column1:
        st.button("Add", on_click=add_todo)

    with column2:
        st.button("Edit", on_click = edit_todo)

    with column3:
        st.button("Complete", on_click = complete_todo)

    with column4:
        st.button("Delete", on_click = delete_todo)

    with column5:
        st.button("Clear",on_click = clear_todo)

    with column6:
        st.write(st.session_state["message"])

    st.subheader("Your todos")

    for i,item in enumerate(app_todos):
        if st.checkbox(item, key = item):
            actual_todos_index = 2*int(i)+1
            actual_todos_item = i
            indexes.append(actual_todos_index)
    todo = st.session_state["new_todo"]
except:
    print("an error occured")

