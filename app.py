import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="My Digital Hub", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (Visual Styling) ---
st.markdown("""
    <style>
    /* Main background color */
    .stApp {
        background-color: #f8f9fa;
    }
    /* Style the buttons */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
        border: none;
    }
    /* Style the metric cards */
    [data-testid="stMetricValue"] {
        font-size: 28px;
        color: #007bff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🌐 Menu")
    page = st.radio("Navigate to:", ["Home", "Projects", "About Me", "Contact"])
    st.write("---")
    st.caption("Freshman Dev | AI & Robotics")

# --- 4. PAGE: HOME ---
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.write("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("The Mission")
        st.write("""
        I am a high school freshman and developer building the next generation 
        of AI tools and hardware. My goal is to combine engineering and 
        entrepreneurship to create a true 'Moonshot Factory.'
        """)
        st.success("Currently exploring: Robotics, AI Prototype V10, and Python Backend.")
    
    with col2:
        st.subheader("Current Focus")
        st.metric(label="Academic Standing", value="4.0 GPA")
        st.metric(label="Ongoing Projects", value="12")

# --- 5. PAGE: PROJECTS ---
elif page == "Projects":
    st.title("🛠️ Project Portfolio")
    st.write("---")
    
    project_type = st.tabs(["Software (AI)", "Hardware", "Simulations"])
    
    with project_type[0]:
        st.subheader("AI Software")
        st.write("**Mr. Bunny AI:** A versatile assistant built with Python.")
        st.write("**Nova AI:** A sophisticated chatbot logic system with over 10 versions.")
        
    with project_type[1]:
        st.subheader("Hardware & Engineering")
        st.write("**Nova AI Glasses:** Wearable technology featuring facial recognition.")
        st.info("Status: Prototyping V2")
        
    with project_type[2]:
        st.subheader("Digital Worlds")
        st.write("**United Empire of Koushik (UEK):** A complex geopolitical simulation in Minecraft.")

# --- 6. PAGE: ABOUT ME ---
elif page == "About Me":
    st.title("👤 About Me")
    st.write("---")
    
    st.write("""
    I’m a 14-year-old student passionate about the intersection of high-tech 
    engineering and entrepreneurship. Whether it's coding a new AI version 
    or building a Minecraft legal system, I'm always creating.
    """)
    
    st.subheader("Clubs & Activities")
    st.markdown("- **Robotics Club (FTC)**")
    st.markdown("- **Programming Club**")
    st.markdown("- **AVID Program**")
    st.markdown("- **California Scholarship Federation**")

# --- 7. PAGE: CONTACT ---
elif page == "Contact":
    st.title("📩 Get in Touch")
    st.write("---")
    
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Details")
        
        if submitted:
            if name and email and message:
                st.success(f"Hello {name}! Your message has been received.")
            else:
                st.error("Please fill out all fields.")

# --- 8. FOOTER ---
st.write("---")
st.caption("Built entirely in Python via Streamlit | Last Updated: April 2026")
