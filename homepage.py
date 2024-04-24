import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title = None,
    options = ['ภาพรวมผู้โดยสาร', 'COVID', 'Highlight', 'Summary'],
    #icons = [""]
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",


)

if selected == 'ภาพรวมผู้โดยสาร':
    st.title("หา intro ดีๆ")
    st.title("ถ้าไม่มี covid สนามบินจะวุ่นวายขนาดไหน")
    st.sidebar.success("Select a page below")
if selected == 'COVID':
    st.title("กราฟ covid สักอย่าง")
if selected == 'Highlight':
    st.title("insight สำคัญ?")
if selected == 'Summary':
    st.title("หน้าสุดท้าย")

#sidebar menu in each page to interact (point 1 page in option 1 to point 4 page in option 4)