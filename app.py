import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SIEGE: The Clothing Empire", 
    page_icon="👕", 
    layout="wide"
)

# --- 2. CUSTOM CSS (Store Styling) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .product-card {
        border: 1px solid #eee;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        background-color: #fafafa;
    }
    .stButton>button {
        background-color: #111111;
        color: white;
        border-radius: 20px;
    }
    .stButton>button:hover {
        background-color: #333333;
        border: 1px solid #111111;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE (Shopping Cart) ---
if 'cart' not in st.session_state:
    st.session_state.cart = 0

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛍️ StyleSync")
    page = st.radio("Browse", ["New Arrivals", "Collections", "Your Cart", "Track Order"])
    st.write("---")
    st.metric("Items in Cart", st.session_state.cart)
    if st.button("Clear Cart"):
        st.session_state.cart = 0
        st.rerun()

# --- 5. PAGE: NEW ARRIVALS ---
if page == "New Arrivals":
    st.title("Spring 2026 Collection")
    st.write("Fresh drops for the new season.")
    st.write("---")

    # Product Grid
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500", caption="Essential White Tee")
        st.write("**$25.00**")
        if st.button("Add to Cart", key="item1"):
            st.session_state.cart += 1
            st.toast("Added to cart!")

    with col2:
        st.image("https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500", caption="Midnight Leather Jacket")
        st.write("**$120.00**")
        if st.button("Add to Cart", key="item2"):
            st.session_state.cart += 1
            st.toast("Added to cart!")

    with col3:
        st.image("https://images.unsplash.com/photo-1542272604-787c3835535d?w=500", caption="Classic Slim Denim")
        st.write("**$65.00**")
        if st.button("Add to Cart", key="item3"):
            st.session_state.cart += 1
            st.toast("Added to cart!")

# --- 6. PAGE: COLLECTIONS ---
elif page == "Collections":
    st.title("Explore Categories")
    st.write("---")
    cat_col1, cat_col2 = st.columns(2)
    
    with cat_col1:
        st.header("Streetwear")
        st.image("https://images.unsplash.com/photo-1552066344-24632e293122?w=800")
        st.button("Shop Streetwear")

    with cat_col2:
        st.header("Formal")
        st.image("https://images.unsplash.com/photo-1594932224828-b4b059bdbf6f?w=800")
        st.button("Shop Formal")

# --- 7. PAGE: YOUR CART ---
elif page == "Your Cart":
    st.title("Your Shopping Bag")
    st.write("---")
    
    if st.session_state.cart == 0:
        st.warning("Your cart is empty! Go grab some gear.")
    else:
        st.success(f"You have {st.session_state.cart} items ready for checkout.")
        
        with st.expander("Order Summary"):
            st.write(f"Subtotal: ${st.session_state.cart * 35}.00") # Sample average price
            st.write("Shipping: FREE")
            st.write(f"**Total: ${st.session_state.cart * 35}.00**")
            
        if st.button("Proceed to Checkout"):
            st.balloons()
            st.write("Redirecting to secure payment... (Simulated)")

# --- 8. PAGE: TRACK ORDER ---
elif page == "Track Order":
    st.title("Where is my stuff?")
    order_id = st.text_input("Enter Order ID (e.g., #SS-12345)")
    if st.button("Track"):
        if order_id:
            st.info(f"Order {order_id} is currently: **In Transit** (Arriving Monday)")
        else:
            st.error("Please enter a valid Order ID.")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 StyleSync Clothing | Powered by Python & Streamlit")
