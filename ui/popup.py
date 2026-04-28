import streamlit as st

def meeting_popup(open_flag):

    if not open_flag:
        return None, False, False   # ✅ ALWAYS 3 VALUES

    st.markdown("### 📝 Enter Meeting Name")

    name = st.text_input("Meeting Name", key="dialog_name")

    col1, col2 = st.columns(2)

    save_clicked = col1.button("Save Meeting")
    cancel_clicked = col2.button("Cancel")

    return name, save_clicked, cancel_clicked