import streamlit as st
#1
st.header("Welcome to TekWork Day 4")

#2
st.title("user management")
#3
st.subheader("Manage your users effectively")

#4 any can be written , converted into text
st.text("323")
st.divider()
#5
st.markdown("**-------------------------------------------------------------------------------------------**")
#6
st.write({"name":"sid","rno":32,"cls":"aic"})#dataframes like:dic and list only

# 7 ** -> bold,*->italic,'-' ->bullet points(space after iffen )
st.divider()
#markdown usually like html and css operations done here
st.markdown("<h3 style='color:pink'>pink</h3>",unsafe_allow_html=True)
#8 divides the top and bottom using line
st.divider()
#9 st.code where we can write any language inside """ """
st.code("""
def f(a,b):
        return a;
     """,language="python"   )
st.divider()
#10 here mathematical expression are been written without any complexity
st.latex(r"\frac{a}{b}")
st.divider()
# 11 button()
if st.button("click", key="main_button"):
    st.write("Button clicked!")
    st.success("ok")#show message 
    st.balloons()#this is an animation
else:
    st.write("button is not clicked")
st.divider()
#12 text_input
s=st.text_input("enter ur name")
if not s.isalpha():
    st.write("only strings are accepted")
   
else:
     st.write(s)

#13 text_area-->used for comments,address,description etc..
#14 number_input=>text_input ,but this is for numerics
st.divider()
#15 checkbox
if st.checkbox("check me"):
    st.write("ur verified")

st.divider()
#16 radio button
f=st.radio("Choose an option", ["Option1", "Option2", "Option3"])
st.write(f)
# if f():
#     f.option1
#     st.write("choosed option 1")
# elif f.option2:
#     st.write("choosed option 2")
# elif f.option3:
#     st.write("choosed option 3")
#------------------------------------------------------------------------------------
st.divider()
#17 selectbox and #18 multi-select
s=st.selectbox("Choose an option", ["Option1", "Option2", "Option3"])
st.write(s)

v=st.multiselect("Choose options", ["Option1", "Option2", "Option3"]  )
st.write(v)

#19 slider 
d= st.slider("Select a value", 0, 100)
st.write(d)
st.divider()
#20 uploder
g=st.file_uploader("Upload a file")
st.write(g)

st.divider()
#21 form
with st.form("user form"):
    nm=st.text_input("Enter your name")
    num=st.number_input("enter your number")
    submitted = st.form_submit_button("Submit")#for password type ,type="password"
    if submitted:
        st.write(f"Hello, {nm}!")
        st.write(f"Your number is {num}")
    if submitted==False:
        st.write("submit entered data")
st.divider()
#22 column
c1,c2,c3=st.columns(3)
with c1:
    st.header("column1")
    st.write("c1")
    
with c2:
    st.header("column2")
    st.write("c2")

with c3:
    st.header("column3")
    st.write("c3")

#or
# c1,c2,c3=st.columns(3)
# with c1:
#     st.header("column1")
#     c=input("enter c1")
#     st.write(c)
    
# with c2:
#     st.header("column2")
#     d=input("enter c2")
#     st.write(d)

# with c3:
#     st.header("column3")
#     e=input("enter c3")
#     st.write(e)
#23 container and table
c=st.container()
c.write("coin")
c.button("click", key="container_button")
h={
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']}
st.table(h)
#sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox("select an option",["Home", "About", "Contact"])
st.sidebar.write("You selected:" ,option)
st.divider()
#cache data
@st.cache_data
def load():
    return [1,2,3]
da=load()
st.write(da)


#task:form of registration and next to login
#(same like signup:note->while signup over msg popup that registreation succesfully ,that should come after the signup info is saved in database)
