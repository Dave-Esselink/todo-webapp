import streamlit as st
import cfun

todos = cfun.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    cfun.write_todos(todos)



st.title("My Todo App")
st.subheader("")
st.write("")




for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        cfun.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key='new_todo')


