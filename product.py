import streamlit as st
if 'products' not in st.session_state:          #ถ้า products ไม่ได้ได้อยู่ใน st.session_state 
    st.session_state.products = []              #ให้ทำการ st.session_state.products เป็นลิสต์ว่าง

def add_product():                              #เขียนฟังก์ชั่นในการเพิ่มสินค้า
    st.header(f":black[Add Items] :red[below]")         
    name = st.text_input("Name")
    description = st.text_input("Description")
    price = st.text_input("Price")
    link = st.text_input("Link")

    
    if st.button("Add Item"):                    #เขียนให้มีปุ่มเพิ่มสินค้า หากกดปุ่มแล้วจะขึ้นข้อความ Succeed
        new_product = {"name": name, "description": description, "price": price, "link": link}
        st.session_state.products.append(new_product)
        st.success(f"Succeed!")

# แสดงข้อมูลสินค้า
def show_products(products):                    #เขียนฟังก์ชั่นแสดงสินค้า
    st.title(":black[Lists]")
    for product in products:
        st.subheader(product["name"])
        st.write(f"Description: {product['description']}")
        st.write(f"Price: {product['price']} Baht")
        st.write(f"Link: {product['link']}")
        st.write("---------")

bg = """                                       
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images-ext-2.discordapp.net/external/dFZEvcAzhxq_572Xbn0lvMCHWXhn-8dwJTUk8pwfBlM/https/img.freepik.com/free-vector/blue-curve-background_53876-113112.jpg?format=webp&width=782&height=521");
background-size: cover;
}

}
</style>
"""                                       
st.markdown(bg, unsafe_allow_html=True)         #กำหนด BG

st.title(f":black[DSSI66 Shop]")                        
add_product()
show_products(st.session_state.products) 