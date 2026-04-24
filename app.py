import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Digital Portfolio", page_icon="🚀", layout="wide")

# --- CUSTOM CSS (To make it look like a 'Full' website) ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_content_type=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "About", "Contact"])

# --- PAGE: HOME ---
if page == "Home":
    st.title("🌐 My Digital Hub")
    st.write("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Welcome!")
        st.write("""
        I am a developer and creator building at the intersection of AI and hardware. 
        This site showcases my journey in engineering, world-building, and code.
        """)
        st.info("💡 Explore the different sections using the sidebar on the left!")
    
    with col2:
        st.subheader("Quick Stats")
        st.metric(label="Current GPA", value="4.0")
        st.metric(label="AI Versions Developed", value="10", delta="+1 this month")

# --- PAGE: PROJECTS ---
elif page == "Projects":
    st.title("🛠️ My Projects")
    st.write("---")
    
    tab1, tab2, tab3 = st.tabs(["AI Software", "Hardware", "Creative"])
    
    with tab1:
        st.header("AI Applications")
        st.write("**Mr. Bunny AI:** A versatile assistant built with Python.")
        st.write("**Nova AI:** A sophisticated chatbot logic system.")
        
    with tab2:
        st.header("Hardware Prototypes")
        st.write("**Nova AI Glasses:** Wearable tech featuring facial recognition.")
        st.progress(75, text="Development Progress")
        
    with tab3:
        st.header("Minecraft & Simulations")
        st.write("**United Empire of Koushik (UEK):** A complex geopolitical simulation.")

# --- PAGE: ABOUT ---
elif page == "About":
    st.title("👤 About Me")
    st.write("---")
    st.write("""
    I am a high school freshman focused on robotics, programming, and entrepreneurship. 
    My goal is to create a 'Moonshot Factory' that merges high-tech engineering with 
    useful consumer products.
    """)
    st.image("https://via.placeholder.com/700x300", caption="Engineering the Future")

# --- PAGE: CONTACT ---
elif page == "Contact":
    st.title("📩 Get in Touch")
    st.write("---")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            st.success(f"Thanks {name}, your message has been 'sent' (simulated)!")

# --- FOOTER ---
st.write("---")
st.caption("Built with Python & Streamlit | 2026")
