import streamlit as st
import pandas as pd
import hiplot as hip
from nirf import *
#st.beta_set_page_config(layout="wide")


my_skills = pd.read_excel("C://Users//User//examples//my_cv//myskills.xlsx",sheet_name =[0,1,2,3,4,5])
#my_expander = st.beta_expander("Expand", expanded=True)
if st.sidebar.checkbox("Projects"):
    for i in my_skills[0]['Projects']:
        st.beta_expander(i)
        if st.checkbox(i):
            get_proj()

if st.sidebar.checkbox("My Skills_raw"):
    st.write(my_skills[0])
if st.sidebar.checkbox("My Skills"):
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

if st.sidebar.checkbox("Chem Data Science"):
    my_expander = st.beta_expander("Database")
    my_expander = st.beta_expander("Python Libraries")
    my_expander = st.beta_expander("Articles")
if st.sidebar.checkbox("My CV"):
    st.header("Boddu Venkatesh")
    Lin = """<p><a href="https://www.linkedin.com/in/bvenkatesh-ai/"target="_blank" rel="nofollow">Linkedin</a></p>"""
    st.markdown(Lin, unsafe_allow_html=True) #Title rendering
    my_github ="""<p><a href="https://github.com/bvenkatesh-ai"target="_blank" rel="nofollow">Github</a></p>"""
    st.markdown(my_github, unsafe_allow_html=True) #Title rendering
    if st.checkbox("About me"):
        st.subheader("About me")
        st.write("I am looking for a position which is more generalist rather +\
                 than specialist. I am interested in solving a real world problem +\
                rather than becoming a specilist in a particular filed. I am more \
                on acquiring knowledge on the required tool for the required area")


    edu=st.checkbox("Education")
    if edu:
        st.write("B.Tech Chemical Engineering (GVP College of Engineering, Vizag)")
        st.write("M.E Chemical Engineering (Indian Institute if Science, Bangalore")
    exp=st.checkbox("Experience")

    if exp:
        st.write("Lecturer")
        st.markdown("""Skills acquired: People management, improved communication,Knowledge transfer""")
        st.write("Research Assistant")
        st.write("Assistant Professor")

    if st.checkbox("My Strengths"):
        st.markdown("""Learner, flexible""")
    if st.checkbox("My google alerts"):
        st.markdown("""Creativity, EI, Automation""")

    # if st.checkbox("Download CV"):
        # st.info("To get my conventional/routine CV")
    Title_html = """
        <p><a href="https://drive.google.com/file/d/1nvGSRYx0Awc_EVA6PORFcXE-4aHAoggk/view?usp=sharing/" target="_blank" rel="nofollow">Download CV</a></p>"""
    st.markdown(Title_html, unsafe_allow_html=True) #Title rendering
