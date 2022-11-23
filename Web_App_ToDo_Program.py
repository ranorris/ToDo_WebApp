import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo.title()+"\n")
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
# st.subheader("This is my To-Do App")
st.write("CHECK an entry to mark as complete, and remove from the list.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos) 
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = " ", placeholder = "Add new To-Do ...", on_change = add_todo, key = "new_todo")

# st.session_state