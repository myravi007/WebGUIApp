import streamlit as sl
import functions as f


items_list = f.file_read()
def add_to_do():
    to_do_item = sl.session_state["Add To-Do"] + "\n"
    items_list.append(to_do_item)
    f.file_write(items_list)

sl.title("My To-Do App")
sl.subheader("This is RaviK To-Do App")
sl.write("This exercise is to learn Web GUI")



for index, item in enumerate(items_list):
    checkbox_status = sl.checkbox(item, key=item)
    if checkbox_status:
        items_list.pop(index)
        f.file_write(items_list)
        del sl.session_state[item]
        sl.experimental_rerun()

sl.text_input(label="Enter a To-Do to add:", placeholder="Please add To-Do...", key="Add To-Do", on_change=add_to_do)

