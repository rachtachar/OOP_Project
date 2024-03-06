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

bg = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #F7DED0;
opacity: 0.8;
background-size: 10px 10px;
background-image: repeating-linear-gradient(45deg, #FEECE2 0, #FEECE2 1px, #F7DED0 0, #F7DED0 50%);
}

}
</style>
"""
st.markdown(bg, unsafe_allow_html=True)
st.title("DSSI66 Shop")
add_product()
show_products(st.session_state.products) 