
# # Basic webpage

# import streamlit as st

# st.title("Hello Streamlit 👋")
# st.write("This is your first Streamlit app!")
# st.write("Streamlit makes it easy to turn data scripts into web apps.")

# -------------------- Interactive Widgets -------------------- #

# import streamlit as st

# st.header("🎛️ Interactive Widgets Example")

# # Text input
# name = st.text_input("Enter your name:")

# # Slider
# age = st.slider("Select your age:", 1, 100, 22)

# # Button
# if st.button("Submit"):
#     st.success(f"Hello {name}! You are {age} years old.")


# -------------------- Chart Widgets -------------------- #

# import streamlit as st
# import pandas as pd
# import numpy as np

# st.header("📈 Displaying Data and Charts")

# data = pd.DataFrame(
#     np.random.randn(10, 3),
#     columns=['A', 'B', 'C']
# )

# st.write("### DataFrame:")
# st.dataframe(data)

# st.write("### Line Chart:")
# st.line_chart(data)

# st.write("### Area Chart:")
# st.area_chart(data)


# -------------------- Simple BMI Calculator -------------------- #

# import streamlit as st

# st.title("💪 BMI Calculator")

# weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.5)
# height = st.number_input("Enter your height (m):", min_value=0.5, step=0.01)

# if st.button("Calculate BMI"):
#     bmi = weight / (height ** 2)
#     st.write(f"Your BMI is: **{bmi:.2f}**")
    
#     if bmi < 18.5:
#         st.warning("You are underweight.")
#     elif 18.5 <= bmi < 24.9:
#         st.success("You have a healthy weight!")
#     elif 25 <= bmi < 29.9:
#         st.info("You are overweight.")
#     else:
#         st.error("You are obese.")


# Import the Streamlit library
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# st.title("Streamlit Layout Basics")
# st.write("This app demonstrates how to use columns, rows, and other layout features in Streamlit.")




#     # --- Using Columns ---
# st.header("Columns Example")
# col1, col2, col3, col4 = st.columns(4)

# data =  pd.DataFrame( np.random.randn(10, 3), columns=['A', 'B', 'C'] )
# with col1:
#     st.subheader("Column 1 chart")
#     st.line_chart(data)
# with col2:
#     st.subheader("Column 2 chart")
#     st.bar_chart(data)
# with col3:
#     st.subheader("Column 3 chart")
#     # st.write("This is the third column.")
#     st.area_chart(data)
# with col4:
#     st.subheader("Column 4 chart")
    # st.write("This is the fourth column.")
    # st.dataframe(data.head())
    # fig, ax = plt.subplots()
    # ax.hist(data['B'], bins=10, color='skyblue', edgecolor='black')
    # st.pyplot(fig)
    # fig, ax = plt.subplots()
    # ax.plot([1, 2, 3], [10, 20, 15])
    # ax.set_title("Simple Line Plot")
    # ax.set_xlabel("X-axis")
    # ax.set_ylabel("Y-axis")
    # st.pyplot(fig)

#     # --- Using Sidebar ---
# st.sidebar.header("Sidebar Example")
# st.sidebar.write("You can add widgets and controls here.")
# choice = st.sidebar.selectbox("Choose an option:", ["Home", "About", "Contact"])
# st.sidebar.write(f"You selected: {choice}")

#     # --- Using Containers ---
# st.header("Container Example")
# with st.container():
#     st.write("This content is inside a container.")
#     st.line_chart({"data": [1, 3, 2, 4]})

# st.header("this is outside the container")

#     # --- Expander Section ---
# with st.expander("Click to expand"):
#     st.write("Here you can hide or show content dynamically.")

#     # --- Tabs Example ---
# st.header("Tabs Example")
# tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
# with tab1:
#     st.write("This is content inside Tab 1.")
# with tab2:
#     st.write("This is content inside Tab 2.")import streamlit as st
# import time
# import pandas as pd
# import numpy as np

# st.title("💾 Data Loading Example with st.container()")

# # Create an empty container — acts like a placeholder
# placeholder = st.container()

# # Show initial message
# placeholder.write("⏳ Loading data, please wait...")

# placeholder.write("This is some other content on the page while data is loading.")
# st.write("You can interact with other widgets here.")
# # Simulate a time-consuming task (like fetching from an API or database)
# time.sleep(3)

# # Once data is "loaded", replace the placeholder content
# placeholder.empty()  # clears previous content

# # Now display the results in the same spot
# data = pd.DataFrame(
#     np.random.randn(10, 3),
#     columns=['A', 'B', 'C']
# )
# placeholder.write("✅ Data loaded successfully!")
# placeholder.dataframe(data)

# # Add a chart below
# st.line_chart(data)

# st.header("Using st.expander()")

# with st.expander("See more details"):
#     st.write("Here’s some hidden content.")
#     st.bar_chart({"data": [5, 10, 15, 20]})


import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')