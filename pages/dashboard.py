# pages/dashboard.py
import streamlit as st

def show():
    # Initialize session state for balloons
    if 'balloons_shown' not in st.session_state:
        st.session_state.balloons_shown = False

    # --- QUICK ACCESS CARDS ---
    st.markdown("### 🔍 Quick Actions")

    col1, col2, col3 = st.columns(3)

    # --- CARD 1: Case Tracking ---
    with col1:
        if st.button("✅ Track Your Case", key="case_btn", use_container_width=True):
            st.session_state.current_page = "case_tracking"
            st.rerun()
        st.markdown("<p style='text-align: center; color: #64748B; font-size: 0.9rem;'>Get real-time updates from eCourts</p>", unsafe_allow_html=True)

    # --- CARD 2: AI Chat ---
    with col2:
        if st.button("🤖 AI Legal Help", key="chat_btn", use_container_width=True):
            st.session_state.current_page = "ai"
            st.rerun()
        st.markdown("<p style='text-align: center; color: #64748B; font-size: 0.9rem;'>Ask in Hindi or English</p>", unsafe_allow_html=True)

    # --- CARD 3: Lawyer Connect ---
    with col3:
        if st.button("📞 Talk to a Lawyer", key="lawyer_btn", use_container_width=True):
            st.session_state.current_page = "lawyers"
            st.rerun()
        st.markdown("<p style='text-align: center; color: #64748B; font-size: 0.9rem;'>₹99 for 15-min consult</p>", unsafe_allow_html=True)

    # --- MORE SERVICES ---
    st.markdown("### 🛠️ More Services")
    st.markdown("---")  # Horizontal line

    colA, colB, colC = st.columns(3)

    with colA:
        st.markdown("📄 Document Generator")
        st.markdown("<p style='center; color: #64748B; font-size: 0.9rem;'>Draft Cheque Bounce, notice, divorce petition</p>", unsafe_allow_html=True)
        if st.button("Generate", key="doc_gen" , use_container_width=True):
            st.session_state.current_page = "documents"
            st.rerun()

    with colB:
        st.markdown("📬 Doorstep Rental Agreement")
        st.markdown(
            "<p style='text-align: center; color: #64748B; font-size: 0.9rem;'>"
            "We draft, verify & deliver your rent agreement at home — <strong>zero hassle</strong>"
            "</p>",
            unsafe_allow_html=True
        )
        if st.button("Start Now", key="rental_agreement", use_container_width=True):
            # Generate unique request ID
            import datetime
            req_id = f"DRA/MH/{datetime.datetime.now().year}/{str(st.session_state.get('request_count', 1)).zfill(3)}"
            st.session_state.request_id = req_id
            st.session_state.current_page = "doorstep_rental"
            st.session_state.request_step = "how_it_works"  # Start flow
            st.rerun()

    with colC:
        st.markdown("💰 Recovery Suit")
        st.markdown("<p style='color: #64748B; font-size: 0.9rem;'>Recover money owed to you legally</p>", unsafe_allow_html=True)
        if st.button("File Suit", key="recovery" , use_container_width=True):
            st.session_state.current_page = "document_gen"
            st.session_state.doc_type = "Recovery of Money Suit"
            st.rerun()

    # --- USER STATUS / WELCOME ---
    role = st.session_state.role
    name = st.session_state.name.split()[0]
    
    st.markdown("### 🎯 What's Next?")
    if role == "admin":
        st.success("🧑‍💼 Admin Panel: Manage users, cases, AI settings")
    elif role == "lawyer":
        st.success(f"👨‍⚖️ Welcome back, {name}! View your clients & schedule.")
    elif role == "client":
        st.success(f"🎯 You're all set, {name}! Start with AI or track your case.")

    # --- BALLOONS ONCE ---
    if not st.session_state.balloons_shown:
        st.balloons()
        st.session_state.balloons_shown = True