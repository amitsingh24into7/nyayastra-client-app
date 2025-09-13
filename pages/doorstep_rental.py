# pages/doorstep_rental.py
import streamlit as st
from datetime import datetime
import random

def show():
    step = st.session_state.get("request_step", "how_it_works")
    req_id = st.session_state.get("request_id", "DRA/MH/2025/001")

    st.subheader("🏠 Doorstep Rental Agreement")
    st.markdown(f"**Request ID:** `{req_id}` | 📍 Maharashtra Only")

    # --- STEP 1: How It Works ---
    if step == "how_it_works":
        st.markdown("### 🔄 How It Works")
        st.markdown("""
        1. **📝 Enter Details** – Fill tenant, landlord & property info  
        2. **✅ Verified by Lawyer** – Our expert reviews and confirms  
        3. **👤 You Confirm** – Approve final draft  
        4. **💳 Make Payment** – ₹999 (includes stamp duty assistance)  
        5. **🖋 e-Stamp Generated** – Legally valid across Maharashtra  
        6. **📄 Get Agreement** – Delivered via courier or email  

        ⏳ Total Time: ~3–5 days
        """)

        if st.button("🚀 I'm Ready! Start Now", type="primary"):
            st.session_state.request_step = "form"
            st.rerun()

    # --- STEP 2: Collect Details ---
    elif step == "form":
        st.markdown("### 📝 Fill Agreement Details")

        st.info("Landlord Details")
        landlord_name = st.text_input("Full Name")
        landlord_phone = st.text_input("Phone Number")
        landlord_address = st.text_area("Permanent Address")

        st.info("Tenant Details")
        tenant_name = st.text_input("Full Name", key="t_name")
        tenant_phone = st.text_input("Phone Number", key="t_phone")
        tenant_aadhar = st.text_input("Aadhar Number (Optional)")

        st.info("Property Details")
        property_addr = st.text_area("Full Property Address")
        monthly_rent = st.number_input("Monthly Rent (₹)", min_value=1000)
        security_deposit = st.number_input("Security Deposit (₹)", min_value=1000)
        agreement_start = st.date_input("Agreement Start Date")
        agreement_end = st.date_input("Agreement End Date")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Back", use_container_width=True):
                st.session_state.request_step = "how_it_works"
                st.rerun()
        with col2:
            if st.button("✅ Submit & Continue", type="primary", use_container_width=True):
                if not landlord_name or not tenant_name or not property_addr:
                    st.error("Please fill all required fields.")
                else:
                    # Save data
                    st.session_state.rental_data = {
                        "req_id": req_id,
                        "landlord": {"name": landlord_name, "phone": landlord_phone, "address": landlord_address},
                        "tenant": {"name": tenant_name, "phone": tenant_phone, "aadhar": tenant_aadhar},
                        "property": {"address": property_addr},
                        "rent": monthly_rent,
                        "deposit": security_deposit,
                        "start": str(agreement_start),
                        "end": str(agreement_end),
                        "submitted_at": datetime.now().isoformat()
                    }
                    st.session_state.request_step = "lawyer_review"
                    st.success("✅ Submitted! Our lawyer will review within 24 hours.")
                    st.balloons()
                    st.rerun()

    # --- STEP 3: Lawyer Review (Simulated) ---
    elif step == "lawyer_review":
        st.markdown("### ⚖️ Under Legal Review")
        st.info("👨‍⚖️ Advocate Mehta is reviewing your agreement…")
        st.write("Estimated time: Within 24 hours")

        # Simulate changes
        if st.checkbox("Show suggested changes (demo mode)"):
            st.warning("🔧 Suggested Change: Add clause for maintenance charges?")
            cols = st.columns(2)
            with cols[0]:
                if st.button("Accept All"):
                    st.session_state.lawyer_approved = True
            with cols[1]:
                if st.button("Request Edit"):
                    st.info("Your request has been sent back to the lawyer.")

        if st.button("✅ Simulate Approval (Dev Mode)", key="approve_lawyer"):
            st.session_state.lawyer_approved = True
            st.session_state.request_step = "user_confirm"
            st.rerun()

    # --- STEP 4: User Confirmation ---
    elif step == "user_confirm":
        data = st.session_state.rental_data
        st.markdown("### ✅ Final Agreement Preview")
        st.markdown(f"**Request ID**: {data['req_id']}")
        st.markdown(f"**Landlord**: {data['landlord']['name']} | {data['landlord']['phone']}")
        st.markdown(f"**Tenant**: {data['tenant']['name']} | {data['tenant']['phone']}")
        st.markdown(f"**Property**: {data['property']['address']}")
        st.markdown(f"**Rent**: ₹{data['rent']}/month | **Deposit**: ₹{data['deposit']}")
        st.markdown(f"**Duration**: {data['start']} to {data['end']}")

        st.divider()
        st.markdown("### 📢 Please Confirm")
        st.write("This is the final version. Once confirmed, you'll proceed to payment.")

        cols = st.columns(2)
        with cols[0]:
            if st.button("↩️ Edit Details", use_container_width=True):
                st.session_state.request_step = "form"
                st.rerun()
        with cols[1]:
            if st.button("✅ I Confirm", type="primary", use_container_width=True):
                st.session_state.user_confirmed = True
                st.session_state.request_step = "payment"
                st.rerun()

    # --- STEP 5: Payment ---
    elif step == "payment":
        st.markdown("### 💳 Secure Payment")
        st.info("Total: ₹999 (Includes Drafting + e-Stamp Support)")
        st.write("Pay securely using UPI, Card, or Net Banking")

        if st.button("🟢 Pay ₹999 Now", type="primary", use_container_width=True):
            st.session_state.payment_done = True
            st.session_state.txn_id = f"NYASTRA-TXN-{random.randint(10000, 99999)}"
            st.session_state.request_step = "stamp_generation"
            st.success(f"✅ Payment Successful! TXN ID: `{st.session_state.txn_id}`")
            st.balloons()
            st.rerun()

    # --- STEP 6: Stamp Generation ---
    elif step == "stamp_generation":
        st.markdown("### 🖋 e-Stamp Certificate Generation")
        st.info("Generating your legally valid e-Stamp certificate…")

        if st.button("✅ Simulate Stamp Issuance", key="gen_stamp"):
            st.session_state.stamp_url = "https://example.com/stamp-cert.pdf"
            st.session_state.agreement_ready = True
            st.session_state.request_step = "delivery"
            st.rerun()

        st.progress(80)

    # --- STEP 7: Delivery ---
    elif step == "delivery":
        st.markdown("### 📦 Agreement Delivery")
        st.success("🎉 Congratulations! Your rental agreement is ready.")
        
        st.markdown("Choose delivery method:")
        delivery = st.radio("", ["📧 Email PDF", "📦 Courier to Address"])

        if st.button("📤 Finalize Delivery", type="primary"):
            tracking = f"DTLC/CTR/{random.randint(100000, 999999)}"
            st.success(f"✅ Agreement dispatched!\n\n📦 Tracking ID: `{tracking}`\n📞 Courier: DTDC / Blue Dart")
            st.session_state.tracking_id = tracking
            st.session_state.request_step = "completed"
            st.rerun()

    # --- STEP 8: Completed ---
    elif step == "completed":
        st.markdown("### ✅ All Done!")
        st.balloons()
        st.success("Your rent agreement is complete and delivered.")
        st.write("Thank you for trusting Nyayastra!")

        st.markdown("---")
        st.markdown("#### 📎 Summary")
        data = st.session_state.rental_data
        st.markdown(f"- **Request ID**: {data['req_id']}")
        st.markdown(f"- **Payment**: ₹999 (TXN: `{st.session_state.txn_id}`)")
        st.markdown(f"- **Tracking ID**: `{st.session_state.tracking_id}`")
        if hasattr(st.session_state, 'stamp_url'):
            st.markdown(f"- [Download e-Stamp Certificate](https://example.com/stamp-cert.pdf)")

    # --- Back to Dashboard ---
    if st.button("🏠 Return to Dashboard", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()

# Render
show()