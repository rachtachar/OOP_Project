import streamlit as st
if 'products' not in st.session_state:
    st.session_state.products = []

def add_product():
    st.header(f"Add Items :red[below]")
    name = st.text_input("Name")
    description = st.text_input("Description")
    price = st.text_input("Price")
    link = st.text_input("Link")

    
    if st.button("Add Item"):
        new_product = {"name": name, "description": description, "price": price, "link": link}
        st.session_state.products.append(new_product)
        st.success(f"Succeed!")

# แสดงข้อมูลสินค้า
def show_products(products):
    st.title("Lists")
    for product in products:
        st.subheader(product["name"])
        st.write(f"Description: {product['description']}")
        st.write(f"Price: {product['price']} Baht")
        st.write(f"Link: {product['link']}")
        st.write("---------")

st.title("DSSI Shop")
add_product()
show_products(st.session_state.products) 