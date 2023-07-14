import streamlit as st
import pandas as pd
import json
# from database import create_connection,Project

projects=["1","2","3"]
project_manager=["me","you"]
resources=["1","2","3"]

st.header("Onedata Project Updation")
name=st.selectbox(options=projects,label="Select project")
manager=st.selectbox(options=project_manager,label="Select your name")
resources=st.multiselect(options=resources,label="Select Resources")

data=json.dumps(resources)
print(data)

# if st.button("update") and name and manager and resources:
#     conn=create_connection() 
#     data=Project(name=name,manager=manager,resources=resources)
#     conn.add(data)   
#     conn.commit()
#     print("data updated succesfully")
# else:
#     st.write("please provide all deatails")
