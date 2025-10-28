import streamlit as st

st.ssn_page_config(
    page_title="Student Survey"
}

visualize = st.Page{'studentSurvey.py', title='Pencapaian Akademik Pelajar', icon-":material/school:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, visualize]
        }
    )

pg.run()
