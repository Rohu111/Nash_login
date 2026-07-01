import streamlit as st

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="NASH",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------
# HIDE STREAMLIT DEFAULT UI
# ----------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

[data-testid="stSidebar"]{
display:none;
}

.stApp{
background:linear-gradient(135deg,#050505,#0A0A0A,#111111,#1A1A1A);
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
padding-left:4rem;
padding-right:4rem;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# TITLE
# ----------------------------------------------------

left,right = st.columns([7,3])

with left:

    st.image("logo.png", width=320)

    st.markdown("""
    <h1 style="
    color:white;
    font-size:72px;
    margin-bottom:0px;
    ">
    NASH
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style="
    color:#B8B8B8;
    margin-top:0px;
    font-weight:400;
    ">
    Navigable Autonomous Sensor HealthHub
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="
    color:#8E8E8E;
    font-size:22px;
    ">
    Autonomous Healthcare.
    <br>
    Anytime.
    <br>
    Anywhere.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    st.image("robot.png", width=520)

# ----------------------------------------------------
# LOGIN CARD
# ----------------------------------------------------

with right:

    st.markdown("""
    <div style="
    background:#161616;
    border-radius:20px;
    padding:35px;
    border:1px solid rgba(255,255,255,.08);
    box-shadow:0px 0px 30px rgba(152,9,23,.20);
    ">
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 style="color:white;">
    Welcome Back
    </h2>
    """, unsafe_allow_html=True)

    st.caption("Sign in to continue")

    st.text_input(
        "Email / Patient ID",
        placeholder="Enter your email"
    )

    st.text_input(
        "Password",
        type="password",
        placeholder="••••••••"
    )

    st.checkbox("Remember Me")

    st.button(
        "LOGIN",
        use_container_width=True
    )

    st.write("")

    st.markdown(
        "<center style='color:#888;'>──────── OR ────────</center>",
        unsafe_allow_html=True
    )

    st.write("")

    st.button(
        "Login with QR Code",
        use_container_width=True
    )

    st.write("")

    st.markdown("""
    <center>

    <span style="color:#B8B8B8;">
    Forgot Password?
    </span>

    <br><br>

    <span style="
    color:#980917;
    font-weight:bold;
    cursor:pointer;
    ">
    Create Account
    </span>

    </center>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.write("")
st.write("")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.info("🤖 AI Powered")

with c2:
    st.success("🔒 Secure Data")

with c3:
    st.warning("🏥 Hospital Ready")

with c4:
    st.info("📡 Real-Time Monitoring")
