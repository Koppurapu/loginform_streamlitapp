import pymysql as p
import streamlit as st
con = p.connect(
    host="localhost",
    user="root",
    password="1169",
    database="MyDatabase"
)

#create operation of table named form done in sql

#insert operation
# def insert_form(name, email, number):
#     cursor = con.cursor()
#     sql = "INSERT INTO form (name, email, num) VALUES ('%s',' %s', %s)"
#     cursor.execute(sql,(name, email, number))
#     con.commit()
#     cursor.close()
# # d=insert_form(name='sid',email='sid@gmail.com',number='1234567890')
# # Read operation
# def read_forms():
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM form")
#     results = cursor.fetchall()
#     cursor.close()
#     return results

# # Update operation
# def update_form(number, name, email):
#     cursor = con.cursor()
#     sql = "UPDATE form SET name=%s, email=%s WHERE number=%s"
#     cursor.execute(sql, (name, email, number))
#     con.commit()
#     cursor.close()

# # Delete operation
# def delete_form(number):
#     cursor = con.cursor()
#     sql = "DELETE FROM form WHERE number=%s"
#     cursor.execute(sql, (number,))
#     con.commit()
#     cursor.close()


with st.form("signup_form"):
    st.title("Signup Form")
    name = st.text_input("Enter a name")
    email = st.text_input("Enter your email")
    number = st.text_input("Enter your number",type='password')
    submitted = st.form_submit_button("Submit")
    if submitted:
        insert="INSERT INTO form (name, email, number) VALUES (%s, %s, %s)"
        values=(name, email, number)
        cursor = con.cursor()
        cursor.execute(insert, values)
        st.success("Form submitted successfully!")
        con.commit()
st.sidebar.title("Menu")
option = st.sidebar.selectbox("select an option",["Home", "About","login"])
st.divider()