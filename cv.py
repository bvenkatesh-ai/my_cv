import streamlit as st
import pandas as pd
import hiplot as hip

st.title("Boddu Venkatesh")

my_skills = pd.read_excel("C://Users//User//examples//datasets//myskills.xlsx",sheet_name =[0,1,2,3,4,5])
#my_expander = st.beta_expander("Expand", expanded=True)
if st.sidebar.checkbox("My Skills"):
    st.write(my_skills[0])
if st.sidebar.checkbox("My Skills_new"):
    # Create your experiment as usual
    data = [{'Tools': 'git/github', 'Profiency': 3, 'projects': 'PCM'},
            {'Tools': 'python', 'Profiency': 4, 'projects': 'NIRF Analytics'},
            {'Tools': 'MYSQL', 'Profiency': 3, 'projects': 'Adam'}]
    xp = hip.Experiment.from_iterable(data)

    # Display with `display_st` instead of `display`
    ret_val = xp.display_st(ret="selected_uids", key="hip")

    #st.markdown("hiplot returned " + json.dumps(ret_val))
if st.sidebar.checkbox("Blogs"):
    st.write(my_skills[1])
if st.sidebar.checkbox("Projects"):
    for i in my_skills[0]['Projects']:
        st.beta_expander(i)
if st.sidebar.checkbox("Chem Data Science"):
    my_expander = st.beta_expander("Database")
    my_expander = st.beta_expander("Python Libraries")
    my_expander = st.beta_expander("Articles")
if st.sidebar.checkbox("")
