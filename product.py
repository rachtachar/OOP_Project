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
    st.header("รายการสินค้า")
    for product in products:
        st.subheader(product["name"])
        st.write(f"Description: {product['description']}")
        st.write(f"Price: {product['price']} Baht")
        st.write(f"Link: {product['link']}")
        st.write("---------")

def local_css(styles):
    with open(styles) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title("DSSI Shop")
local_css("styles.css")



# add_product()
# show_products(st.session_state.products) 