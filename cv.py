import streamlit as st
import pandas as pd
import hiplot as hip
from nirf import *
from iit import *
import base64
from io import BytesIO
from PIL import Image


st.beta_set_page_config(layout="wide")


my_skills = pd.read_excel("myskills.xlsx",sheet_name =[0,1,2,3,4,5])
#To get the page names
sh_names =pd.ExcelFile("myskills.xlsx")
pages = sh_names.sheet_names

def main():
    #--------------------CV------------------------------------------#
    sel_page = st.sidebar.selectbox("Page", pages[0:5])
    st.sidebar.markdown("---------------")
    if sel_page == pages[0]:
        st.subheader(pages[0])
        sel = st.radio("Select format", ["PDF", "Image"])
        if sel == "Image":
            image = Image.open('bvenkatesh_cv.png')
            st.image(image, caption="Boddu Venkatesh", use_column_width=True)
        if sel == "PDF":
           with open("bvenkatesh_cv.pdf","rb") as f:
               base64_pdf = base64.b64encode(f.read()).decode('utf-8')
               pdf_display = f"""<embed src="data:application/pdf;base64,{base64_pdf}" width="600" height="800" type="application/pdf">"""
               st.markdown(pdf_display, unsafe_allow_html=True)
  
    #--------------------Projects------------------------------------------#
    if sel_page == pages[1]:
        st.subheader(pages[1])
        num = len(my_skills[0]['Project Name'])
        cols = st.beta_columns(num)
        p= [1,2,3,4]
        for i in range(0,num):
            p[i] = cols[i].checkbox(my_skills[0]['Project Name'][i], key =i)
            st.write("----------------------")
            colu1, colu2 = st.beta_columns([4,1])
            with colu2:
                ch = st.radio("Select",["About","Interact"])
            with colu1:
                if p[0]:
                   if ch =="About":
                      about_proj_nirf()
                   if ch =="Interact":
                      get_proj_nirf()
                elif p[1]:
                   if ch =="About":
                      about_proj_iit()
                   if ch =="Interact":
                #st.write(my_skills[0]['Project Name'][1])
                       st.sidebar.markdown(get_table_download_link(getdata()), unsafe_allow_html=True)

                elif p[2]:
                   if ch =="About":
                      about_proj_iit()
                   if ch =="Interact":
                      st.write(my_skills[0]['Project Name'][2])
                elif p[3]:
                     if ch =="About":
                        about_proj_iit()
                     if ch =="Interact":
                        st.write(my_skills[0]['Project Name'][3])


     

    #--------------------Skills------------------------------------------#
    if sel_page == pages[2]:
        st.write(my_skills[2])
       # if st.checkbox("My Skills_raw"):
        #   st.write(my_skills[0])
        if st.checkbox("My Skills"):
            # Create your experiment as usual
             data = [{'Tools': 'git/github', 'Profiency': 3, 'projects': 'PCM'},
                   {'Tools': 'python', 'Profiency': 4, 'projects': 'NIRF Analytics'},
                    {'Tools': 'MYSQL', 'Profiency': 3, 'projects': 'Adam'}]
             xp = hip.Experiment.from_iterable(data)

            # Display with `display_st` instead of `display`
             ret_val = xp.display_st(ret="selected_uids", key="hip")

             st.markdown("hiplot returned " + json.dumps(ret_val))

    #--------------------Blogs------------------------------------------#
     if sel_page == pages[3]:
        st.write("Coming Soon")
     
    #--------------------Ch DS------------------------------------------#
    if sel_page == pages[4]:
        st.write(sel_page)
        my_expander = st.beta_expander("Database")
        my_expander = st.beta_expander("Python Libraries")
        my_expander = st.beta_expander("Articles")
        #with open("bvenkatesh_cv.pdf","rb") as f:
         #  base64_pdf = base64.b64encode(f.read()).decode('utf-8')
          # pdf_display = f"""<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">"""
           #st.markdown(pdf_display, unsafe_allow_html=True)
    #    p1_cols = st.beta_columns([1,4,2])
     #   with p1_cols[1]:
      #      st.markdown("""
       #     Phone: **+91 89256 16584** \n
        #    Email: **bvenkatesh.ai@gmail.com**
          #  """)
         #   Lin = """<p><a href="https://www.linkedin.com/in/bvenkatesh-ai/" title ="My Linkedin">@bvenkatesh-ai</a></p>"""
           # st.markdown(Lin, unsafe_allow_html=True) #Title rendering
            #my_github ="""<p><a href="https://github.com/bvenkatesh-ai" title ="My Github">@bvenkatesh-ai</a></p>"""
          #  st.markdown(my_github, unsafe_allow_html=True) #Title rendering

      #  with p1_cols[2]:
       #     image = Image.open('Boddu_Venkatesh.jpg')
        #    st.image(image, caption="Boddu Venkatesh", width=130)
        #st.write("-----------")

       # if st.checkbox("About me"):
        #    st.subheader("About me")
         #   st.write("I am looking for a position which is more generalist rather +\
          #           than specialist. I am interested in solving a real world problem +\
           #         rather than becoming a specilist in a particular filed. I am more \
            #        on acquiring knowledge on the required tool for the required area")


       # edu=st.checkbox("Education")
       # if edu:
        #    st.write("B.Tech Chemical Engineering (GVP College of Engineering, Vizag)")
         #   st.write("M.E Chemical Engineering (Indian Institute if Science, Bangalore")
        #exp=st.checkbox("Experience")

       # if exp:
        #    st.write("Lecturer")
         #   st.markdown("""Skills acquired: People management, improved communication,Knowledge transfer""")
          #  st.write("Research Assistant")
           # st.write("Assistant Professor")

        #if st.checkbox("My Strengths"):
         #   st.markdown("""Learner, flexible""")
        #if st.checkbox("My google alerts"):
         #   st.markdown("""Creativity, EI, Automation""")

        # if st.checkbox("Download CV"):
            # st.info("To get my conventional/routine CV")

        #Title_html = """
         #   <p><a href="https://drive.google.com/file/d/1nvGSRYx0Awc_EVA6PORFcXE-4aHAoggk/view?usp=sharing/" target="_blank" rel="nofollow">Download CV</a></p>"""
        #st.markdown(Title_html, unsafe_allow_html=True) #Title rendering
if __name__ == "__main__":
    main()
