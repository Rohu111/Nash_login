import streamlit as st
from pathlib import Path

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="NASH Login",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# LOAD CSS
# ==============================

def load_css():
    css_file = Path("styles/style.css")

    if css_file.exists():
        with open(css_file) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ==============================
# HIDE STREAMLIT
# ==============================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

[data-testid="collapsedControl"]{
display:none;
}

section[data-testid="stSidebar"]{
display:none;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# PAGE
# ==============================

left, right = st.columns([6,4], gap="large")

# =====================================
# LEFT SIDE
# =====================================

with left:

    st.markdown("<div class='hero-section'>", unsafe_allow_html=True)

    st.image(
        "assets/logo.png",
        width=280
    )

    st.markdown("""
    <div class="hero-title">
        NASH
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-subtitle">
        Navigable Autonomous<br>
        Sensor HealthHub
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-text">
        Autonomous Healthcare.<br>
        Anytime.<br>
        Anywhere.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.image(
        "assets/robot.png",
        width=430
    )

    st.markdown("</div>", unsafe_allow_html=True)
    

# =====================================
# RIGHT SIDE
# =====================================

with right:

    st.markdown("""
    <div class="login-card">
        <div class="login-header">
            <h2>Welcome Back</h2>
            <p>Sign in to access your NASH Dashboard</p>
        </div>
    """, unsafe_allow_html=True)

    email = st.text_input(
        "Email / Patient ID",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="••••••••"
    )

    col1, col2 = st.columns([1,1])

    with col1:
        st.checkbox("Remember Me")

    with col2:
        st.markdown(
            "<p class='forgot-link'>Forgot Password?</p>",
            unsafe_allow_html=True
        )

    st.button("LOGIN", use_container_width=True)

    st.markdown(
        "<div class='divider'>──────── OR ────────</div>",
        unsafe_allow_html=True
    )

    st.button("LOGIN WITH QR CODE", use_container_width=True)

    st.markdown("""
        <div class="create-account">
            Don't have an account?
            <span>Create Account</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# FOOTER
# =====================================

st.write("")
st.write("")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        "<div class='footer-box'>🤖 AI Powered</div>",
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        "<div class='footer-box'>🛡 Secure Data</div>",
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        "<div class='footer-box'>🏥 Hospital Ready</div>",
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        "<div class='footer-box'>📡 Real-Time Monitoring</div>",
        unsafe_allow_html=True
    )
